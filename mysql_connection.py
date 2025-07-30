import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def insert_appointment(name, time):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO appointments (name, time) VALUES (%s, %s)", (name, time))
    conn.commit()
    cursor.close()
    conn.close()