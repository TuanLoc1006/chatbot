
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .handleDB import handleDB
from .constants import Constant

constant = Constant()
NGANH = constant.get_nganh_hoc()
HOCPHI = constant.get_hoc_phi()
CTDT = constant.getCTDT()

handledb = handleDB()
get_connect = handledb.get_connect()
get_nganh = handledb.get_nganh()

# class action_nganh(Action):
#     def name(self):
#         return "action_nganh"
#     def run(self, dispatcher: CollectingDispatcher,
#                 tracker: Tracker,
#                 domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#             nganh = NGANH
            
#             user_input = tracker.latest_message['text']
#             print(user_input)
#             dispatcher.utter_message(text="Danh sách các ngành:")
#             log_connect = get_connect
#             print(log_connect)
#             for item in nganh:
#                 dispatcher.utter_message(text="- " + item.capitalize())
                
#             return []

class action_nganh(Action):
    def name(self):
        return "action_nganh"
    def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            nganh = get_nganh
            print(nganh)
            
            user_input = tracker.latest_message['text']
            print(user_input)
            dispatcher.utter_message(text="Danh sách các ngành có trong chương trình đào tạo của Đại học Y Dược Cần Thơ:")
            log_connect = get_connect
            print(log_connect)
            for item in nganh:
                dispatcher.utter_message(text="- " + item[0].capitalize())
                
            return []
        
class action_hocphi(Action):
    def name(self):
        return "action_hoc_phi"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        hocphi = next(tracker.get_latest_entity_values('hocphi'), None)
        user_input = tracker.latest_message['text']
        print(user_input)
        if hocphi:
            hocphi = HOCPHI
            dispatcher.utter_message(text="Danh sách mức học phí (1 năm):")
            for keys, value in hocphi.items():
                dispatcher.utter_message(text=f"{keys} : {value} VND")
                
        return []
    
class action_chuongtrinhdaotao(Action):
    def name(self):
        return "action_chuong_trinh_dao_tao"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nganh_list = NGANH
        user_input = tracker.latest_message['text']
        print(user_input)
        nganh_entity = next(tracker.get_latest_entity_values('nganh'), None)
        ctdt = CTDT
        if nganh_entity:
            for key, value in ctdt.items():
                if nganh_entity == key:
                    dispatcher.utter_message(text=f"Tham khảo chương trình đào tạo của ngành {nganh_entity} tại đây '{value}'")
        else : dispatcher.utter_message(text=f"Bạn cần biết chương trình đào tạo của ngành nào?")
        return []
    
