import click

from build_svelte_types.generators.typescript_gen import gen_typescript_defines


@click.group()
def cli():
    pass


@cli.command(name="typescript")
def gen_typescript():
    """Generate the typescript interfaces for all models in
    the models folder
    """
    gen_typescript_defines()


if __name__ == "__main__":
    cli()
