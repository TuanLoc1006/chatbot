import mysql.connector

def connectDB():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="chatbot_rasa",
    port=3306,
    )
    return mydb

def nganh():
    handle_db = handleDB()
    db_connection = handle_db.get_connect()
    cursor = db_connection.cursor()
    cursor.execute("SELECT ten_nganh FROM nganh")
    result = cursor.fetchall()
    return result
class handleDB:
    def __init__(self):
        pass
    def get_connect(self):
        return connectDB()
    def get_nganh(self):
        return nganh()
