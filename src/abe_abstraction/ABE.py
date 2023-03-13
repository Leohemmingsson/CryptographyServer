from typing import Type

from .CPAc17 import CPAc17
from .KPAc17 import KPAc17
from .AW11 import AW11


class ABE:
    implementedTypes: list[Type] = {"kpac17": KPAc17, "cpac17": CPAc17}

    # This is run before init and expects a return value
    def __new__(
        self: "ABE", scheme: Type, attributes: list[str] = None, policy: str = None
    ):
        scheme = scheme.lower()
        if scheme not in self.implementedTypes:
            raise Exception(ValueError("No such scheme"))

        return self.implementedTypes[scheme](attributes, policy)
