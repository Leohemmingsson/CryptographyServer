class DB:
    def __init__(self) -> None:
        pass

    def get_handle(self):
        """
        Returns the DB handle
        """
        pass

    def post(self, *args, **kwargs):
        """
        Stores file on specified id.
        """
        pass

    def create_file(self, *args, **kwargs):
        """
        Creates a content instance, with no content.
        """
        pass

    def delete_file(self, *args, **kwargs):
        """
        Deletes the content instance, with specified id.
        """
        pass
    def get_public_key(self):
        """
        Returns the public key.
        """
        pass

    def close(self):
        """
        Closes the connection to the database.
        """
        pass
