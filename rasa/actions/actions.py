# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action
from .custom import Custom

class actionGiayxacnhan(Action):
    def name(self):
        return "action_giay_xac_nhan"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # lấy entities từ câu chat của người dùng
        entities = tracker.latest_message['entities']
        print(f"Entities từ input: {entities} ")
        
        #lấy ra slots
        giayxacnhan = tracker.get_slot('giayxacnhan')
        ask = tracker.get_slot('ask')
        print(f"Slot giayxacnhan: {giayxacnhan}")
        print(f"Slot ask: {ask}")
        
        #mảng role 
        giayxacnhan_roles = []
        ask_roles = []
        
        #phân loại các role từ entities
        for entity in entities:
            if entity.get('entity') == 'giayxacnhan':
                giayxacnhan_roles.append(entity.get('role'))
            elif entity.get('entity') == 'ask':
                ask_roles.append(entity.get('role'))
        
        print(f"Roles của giayxacnhan: {giayxacnhan_roles}")
        print(f"Roles của ask: {ask_roles}")

        default_response = "- SV nhận phiếu đăng ký & nộp trực tiếp tại phòng Công tác sinh viên từ thứ hai-thứ sáu (trong giờ hành chính) và nhận kết quả sau 1 ngày làm việc. </br> - Tháng 9 (thời điểm nhận HS sinh viên khóa mới), chỉ nhận đăng ký vào thứ hai & thứ ba; trả đơn vào các buổi chiều thứ năm và thứ sáu."

        response = ""
        for giayxacnhan_role in giayxacnhan_roles:
            if giayxacnhan_role == "GiayVayVon":
                for ask_role in ask_roles:
                    if ask_role == "where":
                        response += default_response + " (Hỏi vị trí cho GiayVayVon)\n"
                    elif ask_role == "how":
                        response += default_response + " (Hỏi cách thức cho GiayVayVon)\n"
                    else:
                        response += "Xin lỗi, tôi không có thông tin về câu hỏi của bạn.\n"
            elif giayxacnhan_role == "GiayTamHoanNghiaVu":
                for ask_role in ask_roles:
                    if ask_role == "where":
                        response += default_response + " (Hỏi vị trí cho GiayTamHoanNghiaVu)\n"
                    elif ask_role == "how":
                        response += default_response + " (Hỏi cách thức cho GiayTamHoanNghiaVu)\n"
                    else:
                        response += "Xin lỗi, tôi không có thông tin về câu hỏi của bạn.\n"
            else:
                response += "Xin lỗi, tôi không tìm thấy thông tin về loại giấy tờ bạn yêu cầu.\n"

        if not response:
            response = "Xin lỗi, tôi không thể trả lời câu hỏi của bạn vào lúc này."

        dispatcher.utter_message(text=response)
        return []

class actionThongTinKhoa(Action):
    def name(self):
        return "action_thong_tin_khoa"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #lấy ra entity từ câu chat
        entities = tracker.latest_message['entities']
        print(f"Entities từ input: {entities} ")
        
        #lấy ra slot của input nhập vào
        ask_slot= tracker.get_slot('ask')
        khoa_slot = tracker.get_slot('khoa_phong')
        print(f"ask_slot là : {ask_slot}")
        print(f"khoa_slot là: {khoa_slot}")
        
        ask_roles = []
        #phân loại role
        for entity in entities:
            if entity.get('entity') == 'ask':
                ask_roles.append(entity.get('role'))
        print(f"ask_role : {ask_roles}")
        
        dispatcher.utter_message(text=f"{ask_slot} của {khoa_slot} bạn cần tìm là: ")
        return []
    
