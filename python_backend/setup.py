import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="python_backend",
    version="0.0.1",
    author="Jack Dragos",
    author_email="jack.dragos@gmail.com",
    description=("python backend for fastapi"),
    keywords="python",
    url="https://github.com/JackDra/FastSveltekit",
    packages=["build_svelte_types", "models", "routes"],
)
