class rabe:
    def __init__(self, type):
        self.type = type

    def secret(self):
        return "THIS IS secret"

    def encrypt(self, data, attributes, secret_key):
        return "VERY Encrypted data"

    def decrypt(self, encrypted_data, policy, secret_key):
        return "EXTREMLY Decrypted data"
