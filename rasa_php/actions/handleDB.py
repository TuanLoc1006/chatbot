import mysql.connector
import datetime
#DB Lộc (chạy thì mở ra)
def connectDB():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="chatbot_rasa",
    port=3306,
    )
    return mydb

#Phương
# def connectDB():
#     mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="rasa_chatbot",
#     port=3308,
#     )
#     return mydb

def get_current_year():
    now = datetime.datetime.now()
    return now.year

def nganh():
    db_connection = handleDB().get_connect()
    cursor = db_connection.cursor()
    cursor.execute("SELECT DISTINCT ten_nganh FROM nganh")
    result = cursor.fetchall()
    return result

# def getHocPhi(nam=None, loai_hinh_dt=None,ten_nganh_dt=None):
#     db_connection = handleDB().get_connect()
#     cursor = db_connection.cursor()
    
#     if nam is None and loai_hinh_dt is None and ten_nganh_dt is None:
#         current_year = get_current_year()
#         cursor.execute("""
#         SELECT DISTINCT n.ten_nganh, h.gia_tien
#         FROM nganh n
#         JOIN hoc_phi h ON n.ma_nganh = h.ma_nganh
#         JOIN chuong_trinh_dao_tao c ON c.ma_nganh = n.ma_nganh
#         WHERE h.nam_hoc = %s AND c.loai_hinh_dao_tao = %s 
#         """, (current_year, 'đại học'))
#     else:
#        cursor.execute("""
#         SELECT DISTINCT n.ten_nganh, h.gia_tien
#         FROM nganh n
#         JOIN hoc_phi h ON n.ma_nganh = h.ma_nganh
#         JOIN chuong_trinh_dao_tao c ON c.ma_nganh = n.ma_nganh
#         WHERE h.nam_hoc = %s AND c.loai_hinh_dao_tao = %s AND n.ten_nganh LIKE %s
#         """, (nam, loai_hinh_dt, f"%{ten_nganh_dt}%"))
    
#     result = cursor.fetchall()
#     return result

def getHocPhi(nam=None, loai_hinh_dt=None, ten_nganh_dt=None):
    db_connection = handleDB().get_connect()
    cursor = db_connection.cursor()

    # current_year = get_current_year()
    # default_loai_hinh = 'đại học'
   
    # if nam is None:
    #     nam = current_year
    # if loai_hinh_dt is None:
    #     loai_hinh_dt = default_loai_hinh

    if ten_nganh_dt is None:
        query = """
            SELECT DISTINCT n.ten_nganh, h.gia_tien
            FROM nganh n
            JOIN hoc_phi h ON n.ma_nganh = h.ma_nganh
            JOIN chuong_trinh_dao_tao c ON c.ma_nganh = n.ma_nganh
            WHERE h.nam_hoc = %s AND c.loai_hinh_dao_tao = %s
        """
        params = (nam, loai_hinh_dt)
    else:
        query = """
            SELECT DISTINCT n.ten_nganh, h.gia_tien
            FROM nganh n
            JOIN hoc_phi h ON n.ma_nganh = h.ma_nganh
            JOIN chuong_trinh_dao_tao c ON c.ma_nganh = n.ma_nganh
            WHERE h.nam_hoc = %s AND c.loai_hinh_dao_tao = %s AND n.ten_nganh LIKE %s
        """
        params = (nam, loai_hinh_dt, f"%{ten_nganh_dt}%")

    # Execute the query with the constructed parameters
    cursor.execute(query, params)
    result = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    db_connection.close()
    
    return result


def getChuongTrinhDaoTao(entity):
    db_connection = handleDB().get_connect()
    cursor = db_connection.cursor()
    query = "SELECT n.ten_nganh ,c.chuong_trinh_dao_tao FROM `nganh` n JOIN chuong_trinh_dao_tao c on n.ma_nganh=c.ma_nganh WHERE n.ten_nganh LIKE %s"
    cursor.execute(query, ('%' + entity + '%',))
    result = cursor.fetchall()
    return result


def getThongTinKhoaPhongBan(entity):
    db_connection = handleDB().get_connect()
    cursor = db_connection.cursor()
    query = "SELECT `ma_khoa_phong_ban`, `ten_khoa_phong_ban`, `dia_chi_khoa_phong_ban`, `dien_thoai_khoa_phong_ban`, `email_khoa_phong_ban`, `fax` FROM `khoa_phong_ban` WHERE `ten_khoa_phong_ban` LIKE %s"
    cursor.execute(query, ('%' + entity + '%',))
    result = cursor.fetchall()
    return result


class handleDB:
    def __init__(self):
        pass
    def get_connect(self):
        return connectDB()
    def get_nganh(self):
        return nganh()
    
    def get_hoc_phi(self, nam=None, loai_hinh_dt=None,ten_nganh_dt=None):
        return getHocPhi(nam, loai_hinh_dt, ten_nganh_dt)
    
    def get_chuong_trinh_dao_tao(self, entity):
        return getChuongTrinhDaoTao(entity)
    
    def get_khoa_phong_ban(self, entity):
        return getThongTinKhoaPhongBan(entity)
    