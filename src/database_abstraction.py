class DB:
    def __init__(self) -> None:
        pass

    def get_handle(self):
        """
        Returns the DB handle
        """
        pass

    def post(self, id: int, name: str, file: str):
        """
        Stores file on specified id.
        """
        pass

    def create_file(self, id: int):
        """
        Creates a content instance, with no content.
        """
        pass

    def delete_file(self, id: int):
        """
        Deletes the content instance, with specified id.
        """
        pass

    def close(self):
        """
        Closes the connection to the database.
        """
        pass
