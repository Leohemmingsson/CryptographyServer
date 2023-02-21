# std lib
import os

# pip packages
import mysql.connector
from dotenv import load_dotenv


def connect_to_db():
    """
    Creates the connection to the DB through mysql connector.
    All environmental variables are loaded from .env file.
    """
    load_dotenv()

    mydb = mysql.connector.connect(
        host=os.getenv("SERVER_IP"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DATABASE"),
    )

    return mydb


def execute_queries(cursor):
    """
    Creates the two tables with all the different columns, setting PK, FK and AUTO_INCREMENT
    """
    queries = """
       CREATE TABLE `GlobalValues` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `public_key` LONGTEXT,
        `master_key` LONGTEXT,
        `global_key` LONGTEXT,
        PRIMARY KEY (`id`)
        );

        CREATE TABLE `Content` (
        `id` INT NOT  NULL AUTO_INCREMENT,
        `user_id` INT,
        `name` VARCHAR(255),
        `content` LONGTEXT,
        `content_type` VARCHAR(255),
        `global_values` INT NOT NULL,
        PRIMARY KEY (`id`),
        FOREIGN KEY (`global_values`) REFERENCES `GlobalValues`(`id`)
        );
    """

    cursor.execute(queries)
    return cursor


def create_tables_in(mydb):
    """
    Returns decent error messages if needed.
    """

    cursor = mydb.cursor()
    try:
        execute_queries(cursor)
        print("Successfully created tables")
    except mysql.connector.Error as err:
        print(f"{err}")


### RUN ###
mydb = connect_to_db()
create_tables_in(mydb)
mydb.close()
