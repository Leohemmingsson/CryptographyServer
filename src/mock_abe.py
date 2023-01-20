class rabe:
    def __init__(self, type):
        self.type = type

    def secret(self):
        return "secret"

    def encrypt(self, data, attributes, secret_key):
        return "Encrypted data"

    def decrypt(self, encrypted_data, policy, secret_key):
        return "Decrypted data"
