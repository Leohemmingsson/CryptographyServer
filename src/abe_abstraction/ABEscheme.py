from abc import ABC, abstractmethod


class ABEscheme(ABC):
    __slots__ = ["attributes", "policy", "pk", "msk"]

    def __init__(self, attributes: list[str], policy: str):
        self.attributes = attributes
        self.policy = policy
        self.pk = None
        self.msk = None
        self.sk = None

    @abstractmethod
    def encrypt(self, plaintext: str, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def decrypt(self, ciphertext: str, *args, **kwargs) -> str:
        pass

    @abstractmethod
    def load_static_keys_from_sql(self, sql_handle) -> None:
        pass

    @abstractmethod
    def generate_static_keys(self) -> None:
        pass

    def load_pk_msk(self, sql_handle, scheme):
        pk, msk = sql_handle.get_public_and_master_key(scheme)
        if pk is None or msk is None:
            raise TypeError("Error, public- and master keys not found in database")

        return pk, msk

    def load_gk(self, sql_handle, scheme):
        gk = sql_handle.get_global_key(scheme)
        if gk is None:
            raise TypeError("Error, global key not found in database")
        return gk[0]

    def set_policy(self, policy: str) -> None:
        self.policy = policy

    def set_attributes(self, attributes: list[str]) -> None:
        self.attributes = attributes
