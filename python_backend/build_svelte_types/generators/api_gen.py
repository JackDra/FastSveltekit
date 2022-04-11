import inspect
import os
from string import Template
from typing import Callable

from fastapi import APIRouter

BACKEND = "http://localhost:8000/"

GET_REQUEST_TEMPLATE = os.path.join(
    os.path.dirname(__file__), "templates", "get_request.template"
)

GET_SVELTE_TEMPLATE = os.path.join(
    os.path.dirname(__file__), "templates", "get_svelte.template"
)

SVELTE_ROUTES = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "sveltekit_frontend", "src", "routes"
)


class TSTemplate(Template):

    delimiter = "$$"


def create_get_svelte_file(file_name: str, class_name: str, arg_id: str):
    with open(GET_SVELTE_TEMPLATE, "r") as f:
        template = TSTemplate(f.read())

    replace_dict = {"file_name": file_name, "class_name": class_name}
    filled_template = template.safe_substitute(replace_dict)

    # svelte_frontend/src/routes/{file_name}/[{id}].ts
    output_file = os.path.join(SVELTE_ROUTES, file_name, f"[{arg_id}].svelte")

    with open(output_file, "w") as f:
        f.write(filled_template)


def create_get_request_file(file_name: str, class_name: str, arg_id: str):
    with open(GET_REQUEST_TEMPLATE, "r") as f:
        template = TSTemplate(f.read())

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


if __name__ == "__main__":
    from routes.item import ItemRoutes

    mock_route = APIRouter()
    item_routes = ItemRoutes(mock_route)

    route_methods = {
        get_api_type(imethod): imethod
        for imethod in item_routes.__dict__.values()
        if (callable(imethod) and getattr(imethod, "_REST", False))
    }

    if "get" in route_methods.keys():
        get_arg_name, get_arg_type = inspect_get_request(route_methods["get"])
        file_path = inspect.getfile(ItemRoutes)
        file_name, _ = os.path.splitext(os.path.basename(file_path))
        create_get_request_file(file_name, ItemRoutes.data_model.__name__, get_arg_name)
        create_get_svelte_file(file_name, ItemRoutes.data_model.__name__, get_arg_name)
