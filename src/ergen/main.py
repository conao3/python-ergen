import jinja2
import pathlib
from . import types

current_dir = pathlib.Path(__file__).resolve().parent

fileSystemLoader = jinja2.FileSystemLoader(searchpath=current_dir / "template")
env = jinja2.Environment(loader=fileSystemLoader)


def main(data: types.ErdType):
    template = env.get_template('erd.dot.jinja')
    return template.render(**data.model_dump())


def generate_erd(data: types.ErdType) -> str:
    template = env.get_template('erd.dot.jinja')
    return template.render(**data.model_dump())


if __name__ == "__main__":
    main()
