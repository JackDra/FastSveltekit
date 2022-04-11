from fastapi import FastAPI

from routes.item import ItemRoutes
from routes.rand import RandRoutes


def main() -> FastAPI:

    app = FastAPI()

    ItemRoutes.generate_routes(app)
    RandRoutes.generate_routes(app)

    return app


if __name__ == "__main__":
    main()
