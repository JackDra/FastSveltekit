import inspect
import os
import sys
from typing import Callable

from build_svelte_types.templates.svelte_template import SvelteTemplate
from fastapi import APIRouter
from routes.base_route import BaseRoute

BACKEND = "http://localhost:8000/"

GET_REQUEST_TEMPLATE = os.path.join(
    os.path.dirname(__file__), "..", "templates", "get_request.template"
)

GET_SVELTE_TEMPLATE = os.path.join(
    os.path.dirname(__file__), "..", "templates", "get_svelte.template"
)

SVELTE_ROUTES = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "sveltekit_frontend", "src", "routes"
)

ROUTES_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "routes")


def create_get_svelte_file(file_name: str, class_name: str, arg_id: str):
    """Given a file name, class name and get request id, generate a
    templated svelte file for a simple get request using slug

    Parameters
    ----------
    file_name : str
        Name of the file of the route. Typically lowercase
    class_name : str
        Name of the data class that the get request is getting.
        Typically upper case version of file_name
    arg_id : str
        Unique identifier of the class to fetch the data for.
    """
    with open(GET_SVELTE_TEMPLATE, "r") as f:
        template = SvelteTemplate(f.read())

    replace_dict = {"file_name": file_name, "class_name": class_name}
    filled_template = template.safe_substitute(replace_dict)

    # svelte_frontend/src/routes/{file_name}/[{id}].ts
    output_file = os.path.join(SVELTE_ROUTES, file_name, f"[{arg_id}].svelte")

    with open(output_file, "w") as f:
        f.write(filled_template)


def create_get_request_file(file_name: str, class_name: str, arg_id: str):
    """Given a file name, class name and get request id, generate a
    templated ts get fetch request file for a simple get request using slug

    Parameters
    ----------
    file_name : str
        Name of the file of the route. Typically lowercase
    class_name : str
        Name of the data class that the get request is getting.
        Typically upper case version of file_name
    arg_id : str
        Unique identifier of the class to fetch the data for.
    """
    with open(GET_REQUEST_TEMPLATE, "r") as f:
        template = SvelteTemplate(f.read())

    replace_dict = {
        "file_name": file_name,
        "class_name": class_name,
        "arg_id": arg_id,
    }
    filled_template = template.safe_substitute(replace_dict)

    # svelte_frontend/src/routes/{file_name}/[{id}].ts
    output_file = os.path.join(SVELTE_ROUTES, file_name, f"[{arg_id}].ts")

    with open(output_file, "w") as f:
        f.write(filled_template)


def inspect_get_request(function: Callable) -> tuple[str, type]:
    """Get the get requests id slug and its type

    Parameters
    ----------
    function : Callable
        Function of get request to inspect to see what its
        signatures id and type of id

    Returns
    -------
    arg_name: str
        Name of input argument
    arg_type: type
        Type of the input argument
    """
    _, param = dict(inspect.signature(function).parameters).popitem()
    arg_name, arg_type = param.name, param.annotation
    return arg_name, arg_type


def get_api_type(function: Callable) -> str:
    """Returns list of decorators names

    Notes
    -----
    router variable name must contain "router" in it
    """
    source = inspect.getsource(function)
    index = source.find("def ")
    all_dectorators = [
        line.strip().split()[0]
        for line in source[:index].strip().splitlines()
        if line.strip().startswith("@") and "router" in line
    ]
    # Assume the last decorator is the route one
    rest_type = all_dectorators[-1].split(".")[2].split("(")[0]
    return rest_type


def gen_svelte_files(route_class: type[BaseRoute]):
    """Given a class derived from BaseRoute, generate all svelte
    request and svelte files for the REST functions defined

    Parameters
    ----------
    route_class : type[BaseRoute]
        Route class to generate svelte files for
    """
    mock_route = APIRouter()
    item_routes = route_class(mock_route)

    route_methods = {
        get_api_type(imethod): imethod
        for imethod in item_routes.__dict__.values()
        if (callable(imethod) and getattr(imethod, "_REST", False))
    }

    if "get" in route_methods.keys():
        get_arg_name, get_arg_type = inspect_get_request(route_methods["get"])
        file_path = inspect.getfile(route_class)
        file_name, _ = os.path.splitext(os.path.basename(file_path))
        os.makedirs(os.path.join(SVELTE_ROUTES, file_name), exist_ok=True)
        create_get_request_file(
            file_name, route_class.data_model.__name__, get_arg_name
        )
        create_get_svelte_file(file_name, route_class.data_model.__name__, get_arg_name)


def get_all_classes() -> list[type[BaseRoute]]:
    """Get all defined routes in the routes folder

    Returns
    -------
    list[type[BaseRoute]]
        Imported classes from all routes defined in the
        routes folder
    """
    class_list = []
    for py in [
        f[:-3]
        for f in os.listdir(ROUTES_PATH)
        if f.endswith(".py") and f not in ["__init__.py", "base_route.py"]
    ]:
        mod = __import__(".".join(["routes", py]), fromlist=[py])
        module_name = mod.__name__.split(".")[-1]
        # Assumes class name is capitalized version of file name
        # Appended with Routes
        # E.g. item.py route has routes class ItemRoutes
        class_list.append(getattr(mod, module_name.title() + "Routes"))
    return class_list


if __name__ == "__main__":

    for iclass in get_all_classes():
        gen_svelte_files(iclass)
