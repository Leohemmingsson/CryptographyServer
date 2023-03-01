from typing import Type

from .CPAc17 import CPAc17
from .KPAc17 import KPAc17
from .AW11 import AW11


class ABE:
    valid_types: list[Type] = [AW11, KPAc17, CPAc17]

    # This is run before init and expects a return value
    def __new__(
        self: "ABE", scheme: Type, attributes: list[str] = None, policy: str = None
    ):
        if scheme not in self.valid_types:
            raise Exception(ValueError("No such scheme"))
        return scheme(attributes, policy)
