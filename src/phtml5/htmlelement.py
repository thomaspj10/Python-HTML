from __future__ import annotations
from typing import Any

class HTMLElement:

    _tag: str
    _attributes: dict[str, Any]
    _children: list[HTMLElement | str]
    
    def __init__(self, tag: str, attributes: dict[str, Any], children: list[HTMLElement | str]) -> None:
        self._tag = tag
        self._attributes = attributes
        self._children = children

    def __str__(self) -> str:
        attributes_str = " ".join([f'{item[0].removeprefix("_").removesuffix("_").replace("_", "-")}="{item[1]}"' for item in self._attributes.items() if item[1] != None])
        if len(attributes_str) > 0:
            attributes_str = " " + attributes_str

        children_str = "".join([str(item) for item in self._children])

        return f"<{self._tag}{attributes_str}>{children_str}</{self._tag}>"

    def get_children_from_args(self, args: Any) -> list[HTMLElement | str]:
        children: list[HTMLElement | str] = []
        for element in args:
            if isinstance(element, list):
                for list_item in element: # type: ignore
                    children.append(list_item) # type: ignore
            else:
                children.append(element)

        return children
