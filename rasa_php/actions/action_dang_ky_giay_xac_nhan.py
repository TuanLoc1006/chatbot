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

###############

class actionDangKyGiayXacNhan(Action):
    def name(self):
        return "action_dang_ky_giay_xac_nhan"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message['text']
        conffident = tracker.latest_message['intent'].get('confidence')
        print('INTENT')
        conffident = tracker.latest_message['intent']
        print(user_input)
        print(conffident)
        
        #tất cả các giấy xác nhận
        dispatcher.utter_message(text=f"SV điền thông tin và PHIẾU ĐĂNG KÝ ở phòng Công tác sinh viên.")

        return []