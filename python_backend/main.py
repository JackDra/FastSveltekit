from fastapi import FastAPI

from routes.items import generate_item_endpoints


def main() -> FastAPI:

    app = FastAPI()

    generate_item_endpoints(app)

    return app


if __name__ == "__main__":
    main()
