from fastapi import APIRouter, FastAPI

from routes.items import ItemRoutes


def main() -> FastAPI:

    app = FastAPI()

    ItemRoutes.generate_routes(app)

    return app


if __name__ == "__main__":
    main()
