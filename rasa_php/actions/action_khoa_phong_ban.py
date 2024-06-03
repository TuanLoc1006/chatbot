from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher

from .handleDB import handleDB
from .constants import Constant

from customs.ghi_log_file_no_response.write_file import write_file

# loc
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import UserUtteranceReverted
import requests 
import re
import logging
from datetime import datetime
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
# phuong

handledb = handleDB()
get_connect = handledb.get_connect()
get_nganh = handledb.get_nganh()



class actionHoiThongTinKhoa(Action):
    def name(self):
        return "action_hoi_thong_tin_khoa"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        infor_khoa = next(tracker.get_latest_entity_values('infor_khoa'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi info khoa: " + user_input)
        logging.info("{}{}".format('Call action_hoi_thong_tin_khoa: ', infor_khoa))

        if infor_khoa: 
            try:
                infor_khoa = infor_khoa.lower()
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(infor_khoa)
                
                if infor_khoa_phong_ban_db:
                    ten_khoa = infor_khoa_phong_ban_db[0][1]
                    dia_chi = infor_khoa_phong_ban_db[0][2]
                    sdt = infor_khoa_phong_ban_db[0][3]
                    email = infor_khoa_phong_ban_db[0][4]
                    dispatcher.utter_message(text=f"</br>Địa điểm của {ten_khoa} nằm ở {dia_chi}</br>Số điện thoại: {sdt}</br>Email: {email}")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy địa điểm cho khoa {infor_khoa}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu.")
                logging.error(f"Error querying database khoa: {e}")
           
        else:
            dispatcher.utter_message(text=f"Thông tin khoa không có hoặc không tìm thấy.")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_hoi_thong_tin_khoa: '+user_input)
        return []
    


class actionHoiDiaDiemKhoa(Action):
    def name(self):
        return "action_hoi_dia_diem_khoa"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        diaDiem_entity = next(tracker.get_latest_entity_values('location_khoa'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi địa điểm khoa: " + user_input)
        logging.info("{}{}".format('Call action_dia_diem_khoa: ', diaDiem_entity))

        if diaDiem_entity: 
            try:
                diaDiem_entity = diaDiem_entity.lower()
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(diaDiem_entity)
                
                if infor_khoa_phong_ban_db:
                    ten_khoa = infor_khoa_phong_ban_db[0][1]
                    dia_chi = infor_khoa_phong_ban_db[0][2]
                    dispatcher.utter_message(text=f"Địa điểm của {ten_khoa} nằm ở {dia_chi}.")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy địa điểm {diaDiem_entity}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu.")
                logging.error(f"Error querying database khoa: {e}")
           
        else:
            dispatcher.utter_message(text=f"Địa điểm không có hoặc không tìm thấy, bạn vui lòng mô tả chi tiết hơn.")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_dia_diem_khoa: '+user_input)
        return []
    


class actionHoiEmailKhoa(Action):
    def name(self):
        return "action_hoi_email_khoa"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        email_entity = next(tracker.get_latest_entity_values('email_khoa'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi email khoa: " + user_input)
        logging.info("{}{}".format('Call action_email_khoa: ', email_entity))

       
        if email_entity: 
            try:
                email_entity = email_entity.lower()
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(email_entity)
                
                if infor_khoa_phong_ban_db:
                    ten_khoa = infor_khoa_phong_ban_db[0][1]
                    email = infor_khoa_phong_ban_db[0][4]
                    dispatcher.utter_message(text=f"Email của {ten_khoa} là: {email}.")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy email cho khoa {email_entity}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu email khoa.")
                logging.error(f"Error querying database khoa: {e}")
           
        else:
            dispatcher.utter_message(text=f"Email khoa không có hoặc không tìm thấy.")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_email_khoa: '+user_input)
        return []



class actionHoiSoDienThoaiKhoa(Action):
    def name(self):
        return "action_hoi_sdt_khoa"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        sdt_entity = next(tracker.get_latest_entity_values('sdt_khoa'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi sdt khoa: " + user_input)
        logging.info("{}{}".format('Call action_sdt_khoa: ', sdt_entity))

        
        if sdt_entity: 
            try:
                sdt_entity = sdt_entity.lower()
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(sdt_entity)
                
                if infor_khoa_phong_ban_db:
                    ten_khoa = infor_khoa_phong_ban_db[0][1]
                    sdt = infor_khoa_phong_ban_db[0][3]
                    dispatcher.utter_message(text=f"Số điện thoại của {ten_khoa} là: {sdt}.")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy số điện thoại khoa {sdt_entity}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu sdt khoa.")
                logging.error(f"Error querying database khoa: {e}")
           
        else:
            dispatcher.utter_message(text=f"Số điện thoại khoa không có hoặc không tìm thấy.")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_sdt_khoa: '+user_input)
        return []




class actionHoiThongTinPhong(Action):
    def name(self):
        return "action_hoi_thong_tin_phong"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        infor_phong = next(tracker.get_latest_entity_values('infor_phong'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi info phòng ban: " + user_input)
        logging.info("{}{}".format('Call action_hoi_thong_tin_phong: ', infor_phong))

        if infor_phong: 
            try:
                infor_phong = infor_phong.lower()
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(infor_phong)
                
                if infor_khoa_phong_ban_db:
                    ten_phong = infor_khoa_phong_ban_db[0][1]
                    dia_chi = infor_khoa_phong_ban_db[0][2]
                    sdt = infor_khoa_phong_ban_db[0][3]
                    email = infor_khoa_phong_ban_db[0][4]
                    dispatcher.utter_message(text=f"</br>Địa điểm của {ten_phong} nằm ở {dia_chi}</br>Số điện thoại: {sdt}</br>Email: {email}")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy địa điểm cho phòng ban {infor_phong}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu.")
                logging.error(f"Error querying database khoa: {e}")
           
        else:
            dispatcher.utter_message(text=f"Thông tin phòng ban không có hoặc không tìm thấy.")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_hoi_thong_tin_phong: '+user_input)
        return []

class actionHoiDiaDiemPhong(Action):
    def name(self):
        return "action_hoi_dia_diem_phong"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        diaDiem_entity = next(tracker.get_latest_entity_values('location_phong'), None)
        user_input = tracker.latest_message['text']
        print("Người dùng hỏi địa điểm phòng: " + user_input)
        logging.info("{}{}".format('Call action_dia_diem_phong: ', diaDiem_entity))

        
        if diaDiem_entity:
            try:
                diaDiem_entity = diaDiem_entity.lower()
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(diaDiem_entity)
                
                if infor_khoa_phong_ban_db:
                    ten_phong = infor_khoa_phong_ban_db[0][1]
                    dia_chi = infor_khoa_phong_ban_db[0][2]
                    dispatcher.utter_message(text=f"Địa điểm của {ten_phong} nằm ở {dia_chi}.")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy địa điểm cho phòng {diaDiem_entity}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu.")
                logging.error(f"Error querying database phong: {e}")
        else:
            dispatcher.utter_message(text="Địa điểm không có hoặc không tìm thấy, bạn vui lòng mô tả chi tiết hơn.")
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_dia_diem_phong: ' + user_input)
        
        return []





class actionHoiEmailPhong(Action):
    def name(self):
        return "action_hoi_email_phong"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        email_entity = next(tracker.get_latest_entity_values('email_phong'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi email phong: " + user_input)
        logging.info("{}{}".format('Call action_email_phong: ', email_entity))
        
       
        if email_entity: 
            try:
                email_entity = email_entity.lower()
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(email_entity)
                
                if infor_khoa_phong_ban_db:
                    ten_phong = infor_khoa_phong_ban_db[0][1]
                    email = infor_khoa_phong_ban_db[0][4]
                    dispatcher.utter_message(text=f"Email của {ten_phong} là: {email}.")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy email cho phòng {email_entity}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu email phòng.")
                logging.error(f"Error querying database phòng: {e}")
           
        else:
            dispatcher.utter_message(text=f"Email phòng không có hoặc không tìm thấy.")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_email_phong: '+user_input)
        return []
    

class actionHoiSoDienThoaiPhong(Action):
    def name(self):
        return "action_hoi_sdt_phong"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        sdt_entity = next(tracker.get_latest_entity_values('sdt_phong'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi sdt phòng: " + user_input)
        logging.info("{}{}".format('Call action_sdt_phong: ', sdt_entity))
        
        if sdt_entity: 
            try:
                sdt_entity = sdt_entity.lower()
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(sdt_entity)
                
                if infor_khoa_phong_ban_db:
                    ten_phong = infor_khoa_phong_ban_db[0][1]
                    sdt = infor_khoa_phong_ban_db[0][3]
                    dispatcher.utter_message(text=f"Số điện thoại của {ten_phong} là: {sdt}.")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy số điện thoại phòng {sdt_entity}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu sdt phòng.")
                logging.error(f"Error querying database phòng: {e}")
           
        else:
            dispatcher.utter_message(text=f"Số điện thoại phòng không có hoặc không tìm thấy.")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_sdt_phòng: '+user_input)
        return []
    
