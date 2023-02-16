from rabe_py import aw11
from .ABEscheme import ABEscheme


class Aw11(ABEscheme):
    """
    Python wrapper for the Aw11 schceme implemented in (rabe::schemes::aw11)
    """

    def encrypt(self, plaintext: str):
        """
        This function encrypts plaintext data using a given JSON string policy and a list of attributes
        and produces a ciphertext if successfull
        Arguments:
        * plaintext - The plaintext data given as a string
        Returns:
        * cipheretext - The ciphertext generated by aw11.encrypt()
        """

        ciphertext = aw11.encrypt(self.gk, self.pk, self.policy, plaintext)
        return ciphertext

    def decrypt(self, ciphertext):
        """
        This function decrypts the ciphertext if the attributes in msk match the policy of ct.
        Arguments:
        * ciphertext - The ciphertext generated by aw11.encrypt()
        Returns:
        * plaintext - The decrypted ciphertext as a list of u8's, generated by aw11.decrypt()
        """

        plaintext = aw11.decrypt(self.gk, self.sk, ciphertext)
        return plaintext

    def generate_static_keys(self):
        """
        This function generates a static key, the global key (gk).
        """
        self.gk = aw11.setup()

    def load_static_keys(self, gk):
        """
        This function loads a new static key.
        Arguments:
        * gk - A Global Parameters Key, generated by aw11.setup()
        """
        self.gk = gk

    def load_static_keys_from_sql(self, sql_handle):
        """
        This function loads new static keys from a SQL database.
        Arguments:
        * sql_handle - A SQL database handle

        Returns:
        * True if the keys were loaded successfully, False otherwise
        """
        try:
            gk = super().load_gk(sql_handle)
        except TypeError:
            return False

        self.gk = gk
        return True

    def keygen(self, user_name: str, user_attribute: list[str]):
        """
        This function generates all non-static keys, public key(pk), master secret key(msk) and a secret key(sk).
        Arguments:
        * user_name       - The name of the user the key is associated with, must be unique
        * user_attributes - A list of string attributes assigned to this user
        """

        (pk, msk) = aw11.authgen(self.gk, self.attributes)
        sk = aw11.keygen(self.gk, msk, user_name, user_attribute)
        self.pk = pk
        self.sk = sk
