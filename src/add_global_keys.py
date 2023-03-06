import os
import mysql.connector
from dotenv import load_dotenv


def add_global_keys(
    scheme, public_key="placeholder", master_key="placeholder", global_key="placeholder"
):
    """
    Adds the public key and master key to the database.
    """
    mydb = get_connection()
    cursor = mydb.cursor()

    sql = "INSERT INTO GlobalValues (scheme, public_key, master_key, global_key) VALUES (%s, %s, %s, %s)"
    val = (scheme, public_key, master_key, global_key)

    cursor.execute(sql, val)
    mydb.commit()

    return True


def get_connection():
    load_dotenv()
    mydb = mysql.connector.connect(
        host=os.getenv("SERVER_IP"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DATABASE"),
    )
    return mydb


## ADD GLOBAL KEYS ##
add_global_keys("ABE", "public_key", "master_key", "global_key")
