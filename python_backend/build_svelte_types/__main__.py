import logging

import click

from build_svelte_types.generators.api_gen import gen_svelte
from build_svelte_types.generators.typescript_gen import gen_typescript_defines


@click.command(name="svelte")
def gen_svelte_click():
    """Generate the svelte files from the routes defined for FastAPI"""
    click.echo("Generating typescript defines")
    gen_typescript_defines()
    click.echo("Generating svelte files")
    gen_svelte()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    gen_svelte_click()
