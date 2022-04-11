# type: ignore [no-redef]
import os

import models
from pydantic2ts import generate_typescript_defs

# Where the model files are located that will be converted
MODEL_DIR = os.path.dirname(models.__file__)
# Where the output svelte directory
SVELTE_BASE_DIR = "../sveltekit_frontend/src/"
SVELTE_TYPE_DIR = f"{SVELTE_BASE_DIR}lib/apiTypes"


def gen_typescript_defines():
    """Scrape the MODEL_DIR directory, generate typescript files for each
    file, then output them to the SVELTE_TYPE_DIR
    """
    for ifile in os.listdir(MODEL_DIR):
        model_name, _ = os.path.splitext(os.path.basename(ifile))
        if model_name.startswith("_"):
            continue

        generate_typescript_defs(
            f"models.{model_name}",
            f"{SVELTE_TYPE_DIR}/{model_name}.ts",
            json2ts_cmd="npm run json2ts",
        )


if __name__ == "__main__":
    gen_typescript_defines()
