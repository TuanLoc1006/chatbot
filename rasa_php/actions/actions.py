
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .handleDB import handleDB
from .constants import Constant


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
            print(user_input)
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
        print(user_input)
        
        if hocphi_entity:
            hoc_phi_database = get_hoc_phi
            # print(hoc_phi_database)
            dispatcher.utter_message(text="Mức học phí ước tính 1 năm của các ngành học là: ")
            for value in hoc_phi_database:
                dispatcher.utter_message(text=f"{value[0]} : {value[1]} VND")
        else:
            dispatcher.utter_message
        return []
    
class action_chuongtrinhdaotao(Action):
    def name(self):
        return "action_chuong_trinh_dao_tao"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message['text']
        print(user_input)
        
        nganh_entity = next(tracker.get_latest_entity_values('nganh'), None)
        if nganh_entity:
            CTDT = get_CTDT
            # print(CTDT)
            
            for item in CTDT:
                if item[0].lower() == nganh_entity.lower():
                    dispatcher.utter_message(text=f"Tham khảo chương trình đào tạo ngành {item[0]} tại: '{item[1]}'")
        else : dispatcher.utter_message(text=f"Bạn cần biết chương trình đào tạo của ngành nào?")
        return []
    
class action_khong_the_tra_loi(Action):
    def name(self):
        return "action_khong_biet"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        university_entity = next(tracker.get_latest_entity_values('university'), None).lower()
        
        if university_entity:
            dispatcher.utter_message(text="Rất tiếc tôi không có thông tin về trường bạn yêu cầu.")
        elif(university_entity=='ctump' or university_entity=='y dược cần thơ' or university_entity=='đại học y dược cần thơ' or university_entity=='trường y dược cần thơ' or university_entity=='trường này'):
            dispatcher.utter_message(text="Bạn cần biết thông tin gì?")
        else :
            dispatcher.utter_message(text="Rất tiếc tôi không có thông tin về trường bạn yêu cầu.")
        return []
    
    ##################################################
    