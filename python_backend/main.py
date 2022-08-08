from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.item import ItemRoutes
from routes.rand import RandRoutes


def main() -> FastAPI:

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    ItemRoutes.generate_routes(app)
    RandRoutes.generate_routes(app)

    return app


if __name__ == "__main__":
    main()
