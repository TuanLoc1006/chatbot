
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

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
# phuong

handledb = handleDB()
get_connect = handledb.get_connect()
get_nganh = handledb.get_nganh()
get_hoc_phi = handledb.get_hoc_phi()
# get_CTDT = handledb.get_chuong_trinh_dao_tao()
# get_khoa_phong_ban = handledb.get_khoa_phong_ban()

class ActionThongTinTruong(Action):
    def name(self) -> Text:
        return "action_thong_tin_truong"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        universityy_entity = next(tracker.get_latest_entity_values('university'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi thông tin trường: "+user_input)
        logging.info("{}{}".format('Call action_thong_tin_truong: ', universityy_entity))
        # Tạo từ điển các từ liên quan đến "Đại học Y Dược Cần Thơ"
        related_terms = {
            "ctump", 
            "đại học y dược cần thơ", 
            "đại học y",
            "y dược cần thơ", 
            "trường này", 
            "trường",
            "ctu medical and pharmaceutical university",
            "can tho university of medicine and pharmacy",
            "dhydct",
            "dh y duoc can tho",
            "can tho y duoc",
            "can tho y duoc university",
            "trường đại học y dược",
            "đại học y cần thơ",
            "đại học y dược ct",
            "y dược ct",
            "địa điểm này",
            "địa điểm"
        }
        
        if universityy_entity and universityy_entity.lower() in related_terms:
            # Trả lời thông tin về trường Đại học Y Dược Cần Thơ
            dispatcher.utter_message(
                text="Trường Đại học Y Dược Cần Thơ là trường đại học Khoa học Sức khỏe hệ công lập trực thuộc Bộ Y tế duy nhất tại Đồng bằng sông Cửu Long, Việt Nam. Trường Đại học Y Dược Cần Thơ cũng là một trong những trường đào tạo Y – Dược tốt nhất Việt Nam nói chung và khu vực Đồng bằng Sông Cửu Long nói riêng."
            )
        else:
            # Trả lời rằng không có thông tin về trường này
            dispatcher.utter_message(
                text="Xin lỗi, hiện tại chưa có thông tin về trường bạn yêu cầu."
            )
            file_writer = write_file()
            file_writer.get_ghi_log_file('Action học phí: '+user_input)
        
        return []


class action_nganh(Action):
    def name(self):
        return "action_thong_tin_nganh"
    def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            nganh_database = get_nganh
            # print(nganh_database)
            user_input = tracker.latest_message['text']
            print("người dùng hỏi ngành học: "+user_input)
            logging.info("{}{}".format('Call action_thong_tin_nganh: ', nganh_database))
            dispatcher.utter_message(text="Danh sách các ngành có trong chương trình đào tạo của Đại học Y Dược Cần Thơ, tìm hiểu kĩ hơn bạn có thể nhắn tên ngành cho minh:")
            for item in nganh_database:
                dispatcher.utter_message(text="- " + item[0].capitalize())            
            return []

class ActionChuongTrinhDaoTao(Action):
    def name(self):
        return "action_chuong_trinh_dao_tao"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_input = tracker.latest_message['text']
        logging.info(f"Người dùng hỏi ctdt: {user_input}") 
        
        nganh_entity = next(tracker.get_latest_entity_values('nganh'), None)
        logging.info(f"Call action_ctdt: {nganh_entity}")
        
        if nganh_entity:
            try:
                # Khởi tạo đối tượng handledb
                handledb_instance = handleDB()
                ctdt_cua_nganh = handledb_instance.get_chuong_trinh_dao_tao(nganh_entity)
                
                if ctdt_cua_nganh:
                    ctdt = ctdt_cua_nganh[0][1]
                    dispatcher.utter_message(text=f"Tham khảo chương trình đào tạo ngành {nganh_entity} tại {ctdt}")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy chương trình đào tạo ngành {nganh_entity}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu ctdt")
                logging.error(f"Error querying database ctdt: {e}")
        else:
            dispatcher.utter_message(text="Không tìm thấy chương trình đào tạo cho ngành được yêu cầu.")
            # Tạo một đối tượng write_file và ghi log nếu không tìm thấy entity
            try:
                file_writer = write_file()
                file_writer.get_ghi_log_file(f'Action ctdt: {user_input}')
            except Exception as e:
                logging.error(f"Error writing log file: {e}")
        
        return []
    
class action_hocphi(Action):
    def name(self):
        return "action_hoc_phi"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hocphi_entity = next(tracker.get_latest_entity_values('hocphi'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi học phí: " + user_input)
        logging.info("{}{}".format('Call action_hoc_phi: ', hocphi_entity))
        if hocphi_entity:
            hoc_phi_database = get_hoc_phi
            dispatcher.utter_message(text="Mức học phí ước tính 1 năm của các ngành học là: ")
            for value in hoc_phi_database:
                dispatcher.utter_message(text=f"{value[0]} : {value[1]} VND")
        else:
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('Action học phí: '+user_input)
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
                # Khởi tạo đối tượng handledb
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(diaDiem_entity)
                
                if infor_khoa_phong_ban_db:
                    dia_chi = infor_khoa_phong_ban_db[0][2]
                    dispatcher.utter_message(text=f"Địa điểm của khoa {diaDiem_entity} nằm ở {dia_chi}.")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy địa điểm cho khoa {diaDiem_entity}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu.")
                logging.error(f"Error querying database khoa: {e}")
           
        else:
            dispatcher.utter_message(text=f"Địa điểm không có hoặc không tìm thấy.")
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
                # Khởi tạo đối tượng handledb
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(email_entity)
                
                if infor_khoa_phong_ban_db:
                    email = infor_khoa_phong_ban_db[0][4]
                    dispatcher.utter_message(text=f"Email của khoa là: {email}.")
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
        
        email_entity = next(tracker.get_latest_entity_values('sdt_khoa'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi sdt khoa: " + user_input)
        logging.info("{}{}".format('Call action_sdt_khoa: ', email_entity))
        if email_entity: 
            try:
                # Khởi tạo đối tượng handledb
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(email_entity)
                
                if infor_khoa_phong_ban_db:
                    sdt = infor_khoa_phong_ban_db[0][3]
                    dispatcher.utter_message(text=f"Số điện thoại của khoa là: {sdt}.")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy số điện thoại khoa {email_entity}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu sdt khoa.")
                logging.error(f"Error querying database khoa: {e}")
           
        else:
            dispatcher.utter_message(text=f"Số điện thoại khoa không có hoặc không tìm thấy.")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_sdt_khoa: '+user_input)
        return []
    



class ActionHoiDiaDiemPhong(Action):
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
                # Khởi tạo đối tượng handledb
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(diaDiem_entity)
                
                if infor_khoa_phong_ban_db:
                    dia_chi = infor_khoa_phong_ban_db[0][2]
                    dispatcher.utter_message(text=f"Địa điểm của phòng {diaDiem_entity} nằm ở {dia_chi}.")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy địa điểm cho phòng {diaDiem_entity}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu.")
                logging.error(f"Error querying database phong: {e}")
        else:
            dispatcher.utter_message(text="Địa điểm không có hoặc không tìm thấy.")
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
                # Khởi tạo đối tượng handledb
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(email_entity)
                
                if infor_khoa_phong_ban_db:
                    email = infor_khoa_phong_ban_db[0][4]
                    dispatcher.utter_message(text=f"Email của phòng là: {email}.")
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
        
        email_entity = next(tracker.get_latest_entity_values('sdt_phong'), None)
        
        
        user_input = tracker.latest_message['text']
        print("người dùng hỏi sdt phòng: " + user_input)
        logging.info("{}{}".format('Call action_sdt_phong: ', email_entity))
        if email_entity: 
            try:
                # Khởi tạo đối tượng handledb
                handledb_instance = handleDB()
                infor_khoa_phong_ban_db = handledb_instance.get_khoa_phong_ban(email_entity)
                
                if infor_khoa_phong_ban_db:
                    sdt = infor_khoa_phong_ban_db[0][3]
                    dispatcher.utter_message(text=f"Số điện thoại của phòng là: {sdt}.")
                else:
                    dispatcher.utter_message(text=f"Không tìm thấy số điện thoại phòng {email_entity}.")
            except Exception as e:
                dispatcher.utter_message(text="Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu sdt phòng.")
                logging.error(f"Error querying database phòng: {e}")
           
        else:
            dispatcher.utter_message(text=f"Số điện thoại phòng không có hoặc không tìm thấy.")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_sdt_phòng: '+user_input)
        return []
    



class ActionChatGPTFallback(Action):
    def name(self) -> str:
        return "action_chatgpt_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_message = tracker.latest_message.get('text')
        print("user_ask: "+user_message)
        # logging.info("{}{}".format('Call action_fall_back: ', user_message))
        try:
            response = requests.post(
                'https://api.openai.com/v1/engines/davinci-codex/completions',
                headers={
                    'Authorization': f'Bearer YOUR_OPENAI_API_KEY',
                    'Content-Type': 'application/json'
                },
                json={
                    'prompt': user_message,
                    'max_tokens': 150
                }
            )
            response_data = response.json()

            if 'choices' in response_data and len(response_data['choices']) > 0:
                chatgpt_reply = response_data['choices'][0]['text'].strip()
            else:
                chatgpt_reply = "action fallback: Xin lỗi tôi chưa hiểu ý bạn, bạn vui lòng mô tả chi tiết hơn được không?"

        except Exception as e:
            chatgpt_reply = f"action fallback: Đã xảy ra lỗi: {str(e)}"
        
        dispatcher.utter_message(text=chatgpt_reply)
        
        # Ngăn vòng lặp bằng cách hoàn nguyên trạng thái người dùng
        return [UserUtteranceReverted()]


# class acction_tuyen_sinh(Action):
#     def name(self):
#         return "action_tuyen_sinh"
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         return []
    
##################################################

# class ActionSayData(Action):

#     def name(self) -> Text:
#         return "action_say_data"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         email = tracker.("email")
#         phone = tracker.get_slot("phone")
#         logging.info("{}{}".format('Call action_say_data: '))

#         dispatcher.utter_message(text=f"Email bạn cung cấp là: {email},số điện thoại là: {phone}")

#         return []
    


# class ValidateSimpleForm(FormValidationAction):

#     def name(self) -> Text:
#         return "validate_simple_form"

#     def validate_phone(
#         self,
#         value: Text,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         if len(value) == 10 and value.isdigit():
#             # Trả về số điện thoại hợp lệ
#             return {"phone": value}
#         else:
#             # Trả về None nếu số điện thoại không hợp lệ
#             dispatcher.utter_message(text="Số điện thoại không hợp lệ")
#             return {"phone": None}

#     def validate_email(
#         self,
#         value: Text,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#         if re.match(email_regex, value):
#             # Trả về email hợp lệ
#             return {"email": value}
#         else:
#             # Trả về None nếu email không hợp lệ
#             dispatcher.utter_message(text="Email không hợp lệ!")
#             return {"email": None}

##########################################################
#######  PHUONG
# 5.	Cơ hội thực tập và nghiên cứu.

class action_yeu_to_xet_hoc_bong(Action):
    def name(self):
        return "action_yeu_to_xet_hoc_bong"
    def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            dispatcher.utter_message(f"1. Đăng ký học và thi tối thiểu 10 tín chỉ mỗi kỳ, hoặc số tín chỉ tối đa mở theo khóa/ngành (không tính Giáo dục Thể chất và Giáo dục quốc phòng - An ninh). 2.Điểm trung bình chung học tập từ 3.0 trở lên.
Điểm thi/kiểm tra lần đầu không có điểm dưới 2.0 hoặc kiểm tra hết môn không đạt. 3.Điểm rèn luyện từ loại tốt trở lên.
Không bị kỷ luật từ mức khiển trách trở lên. 4.Đóng học phí và kinh phí đào tạo đúng thời hạn trong học kỳ xét học bổng.");
            return []
