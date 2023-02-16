class ABEscheme:
    def __init__(self, attributes: list[str], policy: str):
        self.attributes = attributes
        self.policy = policy
        self.pk = None
        self.msk = None
        self.sk = None

    def encrypt(self, plaintext: str) -> None:
        pass

    def decrypt(self, ciphertext: str) -> str:
        pass

    def keygen(self) -> None:
        pass

    def load_pk_msk(self, sql_handle):
        pk, msk = sql_handle.get_public_and_master_key()
        if pk is None or msk is None:
            raise TypeError
        return pk, msk

    def load_gk(self, sql_handle):
        gk = sql_handle.get_global_keys()
        return gk

    def set_policy(self, policy: str) -> None:
        self.policy = policy

    def set_attributes(self, attributes: list[str]) -> None:
        self.attributes = attributes
