class rabe:
    def __init__(self, type):
        self.type = type

    def setup(self):
        return ("Public key", "Master key")

    def encrypt(self, *args, **kwargs):
        return "VERY Encrypted data"

    def decrypt(self, *args, **kwargs):
        return "EXTREMLY Decrypted data"


if __name__ == "__main__":
    print("oo")
    import cryptography
