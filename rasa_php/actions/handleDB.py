import mysql.connector

def connectDB():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="rasa_data",
    port=3306,
    )
    return mydb

def nganh():
    db_connection = handleDB().get_connect()
    cursor = db_connection.cursor()
    cursor.execute("SELECT ten_nganh FROM nganh")
    result = cursor.fetchall()
    return result

def getHocPhi():
    db_connection = handleDB().get_connect()
    cursor = db_connection.cursor()
    # cursor.execute("SELECT gia_tien FROM hoc_phi")
    cursor.execute("SELECT a.ten_nganh, b.gia_tien FROM nganh AS a JOIN hoc_phi AS b ON a.ma_nganh = b.ma_nganh")
    result = cursor.fetchall()
    return result

def getChuongTrinhDaoTao():
    db_connection = handleDB().get_connect()
    cursor = db_connection.cursor()
    cursor.execute("SELECT a.ten_nganh, b.chuong_trinh_dao_tao FROM nganh AS a JOIN chuong_trinh_dao_tao AS b ON a.ma_nganh = b.ma_nganh")
    result = cursor.fetchall()
    return result

class handleDB:
    def __init__(self):
        pass
    def get_connect(self):
        return connectDB()
    def get_nganh(self):
        return nganh()
    def get_hoc_phi(self):
        return getHocPhi()
    def get_chuong_trinh_dao_tao(self):
        return getChuongTrinhDaoTao()