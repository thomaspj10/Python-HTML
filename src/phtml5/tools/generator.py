import json

# Generate Python code which represents the html tags as specified in html5.json

with open("html5.json", "r") as f:
    specification = json.load(f)

with open("../tags.py", "w") as f:
    f.write("from __future__ import annotations\n\n")
    f.write("from typing import Any\n")
    f.write("from phtml5.htmlelement import HTMLElement\n\n")

    for element in specification["elements"]:
        name: str = element["name"]
        capitalized_name = name.capitalize()
        text: bool = element["text"]
        children: list[str] = element["children"]

        types = " | ".join([child.capitalize() for child in children] + (["str"] if text else []))
        
        f.write(f"class {capitalized_name}(HTMLElement):\n")

        if len(children) == 0:
            f.write("    pass\n\n")
        else:
            f.write(f"\n    def __call__(self: {capitalized_name}, *args: {types} | list[{types}]) -> {capitalized_name}:\n")
            f.write(f"        return {capitalized_name}(self._tag, self._attributes, self.get_children_from_args(args))\n\n")

        f.write(f"def {name}(_class: str | None = None, **kwargs: Any) -> {capitalized_name}:\n")
        f.write("    arguments = { 'class': _class }\n")
        f.write(f"    return {capitalized_name}('{name}', arguments | kwargs, [])\n\n")

    for element_group in specification["element_groups"]:
        name = element_group["name"].capitalize()
        types = " | ".join([child.capitalize() for child in element_group["elements"]])

        f.write(f"{name} = {types}\n")

with open("../__init__.py", "w") as f:
    element_functions = ", ".join([element["name"] for element in specification["elements"]])
    element_classes = ", ".join([element["name"].capitalize() for element in specification["elements"]])
    f.write(f"# type: ignore\nfrom tags import {element_functions}\nfrom tags import {element_classes}\n")
