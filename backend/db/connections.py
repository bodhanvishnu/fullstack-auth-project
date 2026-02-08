import pymysql
from mysql.connector import Error
import os

def get_db_connection():
    try:
       connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if not connection.is_connected():
            raise Error("Database connection failed")

        return connection

     except Error as e:
        print(f"Database connection error: {e}")
        return None
