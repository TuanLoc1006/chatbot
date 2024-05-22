
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .handleDB import handleDB
from .constants import Constant

from customs.ghi_log_file_no_response.write_file import write_file

# loc
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import requests 
import re
# phuong

handledb = handleDB()
get_connect = handledb.get_connect()
get_nganh = handledb.get_nganh()
get_hoc_phi = handledb.get_hoc_phi()
get_CTDT = handledb.get_chuong_trinh_dao_tao()



class action_nganh(Action):
    def name(self):
        return "action_nganh"
    def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            nganh_database = get_nganh
            # print(nganh_database)
            
            user_input = tracker.latest_message['text']
            print("action hỏi ngành học: "+user_input)
            dispatcher.utter_message(text="Danh sách các ngành có trong chương trình đào tạo của Đại học Y Dược Cần Thơ:")
            for item in nganh_database:
                dispatcher.utter_message(text="- " + item[0].capitalize())            
            return []
    
class action_hocphi(Action):
    def name(self):
        return "action_hoc_phi"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hocphi_entity = next(tracker.get_latest_entity_values('hocphi'), None)
        user_input = tracker.latest_message['text']
        print("action hoc phi: " + user_input)
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

class ActionChuongTrinhDaoTao(Action):
    def name(self):
        return "action_chuong_trinh_dao_tao"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_input = tracker.latest_message['text']
        print(f"action hỏi ctdt: {user_input}") 
        
        nganh_entity = next(tracker.get_latest_entity_values('nganh'), None)
        
        if nganh_entity:
            CTDT = get_CTDT
            for item in CTDT:
                if item[0].lower() == nganh_entity.lower():
                    dispatcher.utter_message(text=f"Tham khảo chương trình đào tạo ngành {item[0]} tại: {item[1]}")
                    break
            else:
                dispatcher.utter_message(text=f"Không tìm thấy chương trình đào tạo cho ngành {nganh_entity}.")
        else:
            dispatcher.utter_message(text="Bạn cần biết chương trình đào tạo của ngành nào?")
        
        return []


class action_khong_the_tra_loi(Action):
    def name(self):
        return "action_khong_biet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        university_entity = next(tracker.get_latest_entity_values('university'), None)
        user_input = tracker.latest_message['text']
        print("action khong biet: " + user_input)
        if university_entity:
            university_entity = university_entity.lower()
            predefined_universities = [
                'ctump', 
                'y dược cần thơ', 
                'đại học y dược cần thơ', 
                'trường y dược cần thơ', 
                'trường này'
            ]
            
            if any(uni in university_entity for uni in predefined_universities):
                dispatcher.utter_message(text="Bạn cần biết thông tin gì?")
            else:
                dispatcher.utter_message(text="action khong biet: Rất tiếc tôi không có thông tin về trường bạn yêu cầu")
        else:
            dispatcher.utter_message(text="Rất tiếc tôi không có thông tin về trường bạn yêu cầu.")
        
        return []

    
class acction_tuyen_sinh(Action):
    def name(self):
        return "action_tuyen_sinh"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return []
    
    ##################################################

class ActionSayData(Action):

    def name(self) -> Text:
        return "action_say_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.get_slot("email")
        phone = tracker.get_slot("phone")
        
        dispatcher.utter_message(text=f"Email bạn cung cấp là: {email},số điện thoại là: {phone}")

        return []
    


class ValidateSimpleForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_simple_form"

    def validate_phone(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if len(value) == 10 and value.isdigit():
            # Trả về số điện thoại hợp lệ
            return {"phone": value}
        else:
            # Trả về None nếu số điện thoại không hợp lệ
            dispatcher.utter_message(text="Số điện thoại không hợp lệ")
            return {"phone": None}

    def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_regex, value):
            # Trả về email hợp lệ
            return {"email": value}
        else:
            # Trả về None nếu email không hợp lệ
            dispatcher.utter_message(text="Email không hợp lệ!")
            return {"email": None}


class ActionChatGPTFallback(Action):
    def name(self) -> str:
        return "action_chatgpt_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_message = tracker.latest_message.get('text')
        print("user_ask: "+user_message)
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
                chatgpt_reply = "action fallback: Xin lỗi, tôi không thể đưa ra câu trả lời vào lúc này."

        except Exception as e:
            chatgpt_reply = f"action fallback: Đã xảy ra lỗi: {str(e)}"
        
        dispatcher.utter_message(text=chatgpt_reply)
        
        # Ngăn vòng lặp bằng cách hoàn nguyên trạng thái người dùng
        return [UserUtteranceReverted()]
