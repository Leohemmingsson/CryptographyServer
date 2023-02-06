database = {}


class DB:
    def __init__(self) -> None:
        pass

    def get_handle(self):
        """
        Returns the DB handle
        """
        return True

    def post(self, user_id="", file_name="", content="", *args, **kwargs):
        """
        Stores file on specified id.
        """
        if file_name not in database.keys():
            return False
        database[file_name] = content
        return True

    def create_file(self, user_id, file_name, *args, **kwargs):
        """
        Creates a content instance, with no content.
        """
        database[file_name] = ""

        return True

    def delete_file(self, user_id, file_name, *args, **kwargs):
        """
        Deletes the content instance, with specified id.
        """
        if file_name not in database.keys():
            return False
        database.pop(file_name)
        return True

    def get_public_key(self):
        """
        Returns the public key.
        """
        return True

    def get(self, user_id="", file_name="", attributes=""):
        """
        Returns the file content
        """
        return database.get(file_name, "")

    def close(self):
        """
        Closes the connection to the database.
        """
        return True
