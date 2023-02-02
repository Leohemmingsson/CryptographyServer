# std lib
import os

# pip packages
import mysql.connector
from dotenv import load_dotenv


def connect_to_db():
    load_dotenv()

    mydb = mysql.connector.connect(
        host=os.getenv("SERVER_IP"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DATABASE"),
    )

    return mydb


def execute_queries(cursor):
    queries = """
        CREATE TABLE `GlobalValues` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `public_key` VARCHAR(4096),
        `master_key` VARCHAR(4096),
        `global_key` VARCHAR(4096),
        PRIMARY KEY (`id`)
        );

        CREATE TABLE `Content` (
        `id` INT NOT  NULL AUTO_INCREMENT,
        `user_id` INT,
        `name` VARCHAR(255),
        `content` LONGTEXT,
        `content_type` VARCHAR(255),
        `gloabl_values` INT NOT NULL,
        PRIMARY KEY (`id`),
        FOREIGN KEY (`gloabl_values`) REFERENCES `GlobalValues`(`id`)
        );
    """

    cursor.execute(queries)
    return cursor

def create_tables_in(mydb):
    cursor = mydb.cursor()
    try:
        execute_queries(cursor)
        print("Successfully created tables")
    except mysql.connector.Error as err:
        print(f"{err}")


mydb = connect_to_db()

create_tables_in(mydb)

mydb.close()
