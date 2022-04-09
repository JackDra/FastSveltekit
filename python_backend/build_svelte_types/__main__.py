# type: ignore [no-redef]
import os

import models
from pydantic2ts import generate_typescript_defs

for ifile in os.listdir(os.path.dirname(models.__file__)):
    model_name, _ = os.path.splitext(os.path.basename(ifile))
    if model_name == "__init__":
        continue

    generate_typescript_defs(
        f"models.{model_name}",
        f"../sveltekit_frontend/src/lib/apiTypes/{model_name}.ts",
        json2ts_cmd="npm run json2ts",
    )
