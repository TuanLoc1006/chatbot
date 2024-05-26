
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
get_CTDT = handledb.get_chuong_trinh_dao_tao()
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
        print(f"người dùng hỏi ctdt: {user_input}") 
        
        nganh_entity = next(tracker.get_latest_entity_values('nganh'), None)
        logging.info("{}{}".format('Call action_ctdt: ', nganh_entity))
        if nganh_entity:
            CTDT = get_CTDT
            for item in CTDT:
                if item[0].lower() == nganh_entity.lower():
                    dispatcher.utter_message(text=f"Tham khảo chương trình đào tạo ngành {item[0]} tại: {item[1]}")
                    break
            else:
                dispatcher.utter_message(text=f"Không tìm thấy chương trình đào tạo cho ngành {nganh_entity}.")
                file_writer = write_file()
                file_writer.get_ghi_log_file('Action ctdt: '+user_input)
        else:
            dispatcher.utter_message(text="Bạn cần biết chương trình đào tạo của ngành nào?")
        
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








    

# class action_chuongtrinhdaotao(Action):
#     def name(self):
#         return "action_chuong_trinh_dao_tao"
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         user_input = tracker.latest_message['text']
#         print("action hỏi ctdt: "+user_input) 
#         nganh_entity = next(tracker.get_latest_entity_values('nganh'), None)
#         if nganh_entity:
#             CTDT = get_CTDT
#             print(CTDT)
#             for item in CTDT:
#                 if item[0].lower() == nganh_entity.lower():
#                     dispatcher.utter_message(text=f"Tham khảo chương trình đào tạo ngành {item[0]} tại: {item[1]}")
#         else : dispatcher.utter_message(text=f"Bạn cần biết chương trình đào tạo của ngành nào?")
#         return []




# class action_khong_the_tra_loi(Action):
#     def name(self):
#         return "action_khong_biet"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         university_entity = next(tracker.get_latest_entity_values('university'), None)
#         user_input = tracker.latest_message['text']
#         print("action khong biet: " + user_input)
#         if university_entity:
#             university_entity = university_entity.lower()
#             predefined_universities = [
#                 'ctump', 
#                 'y dược cần thơ', 
#                 'đại học y dược cần thơ', 
#                 'trường y dược cần thơ', 
#                 'trường này'
#             ]
            
#             if any(uni in university_entity for uni in predefined_universities):
#                 dispatcher.utter_message(text="Bạn cần biết thông tin gì?")
#             else:
#                 dispatcher.utter_message(text="action khong biet: Rất tiếc tôi không có thông tin về trường bạn yêu cầu")
#         else:
#             dispatcher.utter_message(text="Rất tiếc tôi không có thông tin về trường bạn yêu cầu.")
        
#         return []

    
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
#         email = tracker.get_slot("email")
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
