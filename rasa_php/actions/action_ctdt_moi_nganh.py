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



handledb = handleDB()
get_connect = handledb.get_connect()
get_nganh = handledb.get_nganh()



class actionNganh(Action):
    def name(self):
        return "action_thong_tin_nganh"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        nganh_database = get_nganh
        user_input = tracker.latest_message['text']
        print("Người dùng hỏi ngành học: " + user_input)
        logging.info("Call action_thong_tin_nganh: {}".format(nganh_database))
        
        message = "</br>Danh sách các ngành có trong chương trình đào tạo của Đại học Y Dược Cần Thơ, tìm hiểu kĩ hơn bạn có thể nhắn tên ngành cho mình:\n"
        for item in nganh_database:
            message += "- Ngành " + item[0].capitalize() + "</br>"
        
        dispatcher.utter_message(text=message)
        
        return []


class actionChuongTrinhDaoTao(Action):
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
                nganh_entity = nganh_entity.lower()
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
            dispatcher.utter_message(text="Bạn muốn tìm hiểu chương trình đào tạo ngành nào?")
            # Tạo một đối tượng write_file và ghi log nếu không tìm thấy entity
            try:
                file_writer = write_file()
                file_writer.get_ghi_log_file(f'Action ctdt: {user_input}')
            except Exception as e:
                logging.error(f"Error writing log file: {e}")
        
        return []