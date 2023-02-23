# std lib
import os

# pip packages
import mysql.connector
from dotenv import load_dotenv


class DB:
    def __init__(self) -> None:
        load_dotenv()
        self.mydb = mysql.connector.connect(
            host=os.getenv("SERVER_IP"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DATABASE"),
        )
        self.cursor = self.mydb.cursor()

    def post_file(self, user_id, file_name, content):
        """
        Stores file on specified id.
        """

        global_values_id = "1"

        sql = "INSERT INTO Content (user_id, name, content, content_type, global_values) VALUES (%s, %s, %s, %s, %s)"
        val = (user_id, file_name, content, "text/plain", global_values_id)

        self.cursor.execute(sql, val)
        self.mydb.commit()

        return True

    def get_file(self, user_id, file_name):
        """
        Returns the content instance, with specified id.
        """
        self.cursor.execute(
            "SELECT content FROM Content WHERE user_id = %s AND name = %s",
            (user_id, file_name),
        )

        result = self.cursor.fetchone()

        return result[0]

    def delete_file(self, user_id, file_name):
        """
        Deletes the content instance, with specified id.
        """
        sql = "DELETE FROM Content WHERE user_id = %s AND name = %s"
        val = (user_id, file_name)

        self.cursor.execute(sql, val)
        self.mydb.commit()

        return True

    def get_public_and_master_key(self, scheme) -> tuple[str, str]:
        """
        Returns the public key.
        """
        self.cursor.execute(
            "SELECT public_key, master_key FROM GlobalValues WHERE scheme = %s",
            ([scheme]),
        )

        result = self.cursor.fetchone()

        return result

    def get_global_key(self, scheme):
        """
        Returns the global key.
        """

        self.cursor.execute(
            "SELECT global_key FROM GlobalValues WHERE scheme = %s",
            ([scheme]),
        )

        result = self.cursor.fetchone()

        return result

    def update_pk_msk(self, pk, msk, scheme):
        """
        Updates the public key and master key.
        """

        sql = (
            "UPDATE GlobalValues SET public_key = %s, master_key = %s WHERE scheme = %s"
        )
        values = (pk, msk, scheme)

        self.cursor.execute(sql, values)
        self.mydb.commit()

    def update_gk(self, gk, scheme):
        """
        Updates the global key.
        """
        sql = "UPDATE GlobalValues SET global_key = %s WHERE scheme= %s"
        values = (gk, scheme)

        self.cursor.execute(sql, values)
        self.mydb.commit()

    def close(self):
        """
        Closes the connection to the database.
        """

        self.cursor.close()
        self.mydb.close()
