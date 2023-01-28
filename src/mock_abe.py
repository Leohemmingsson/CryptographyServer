class rabe:
    def __init__(self, type):
        self.type = type

    def setup(self):
        return ("Public key", "Master key")

    def encrypt(self, content, policy, secret_key):
        return "VERY Encrypted data"

    def decrypt(self, encrypted_data, policy, secret_key):
        return "EXTREMLY Decrypted data"
