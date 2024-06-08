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

class actionThongTinTruong(Action):
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
            "thông tin trường này",
            "thông tin trường",
            
        }
        
        if universityy_entity and universityy_entity.lower() in related_terms:
            # Trả lời thông tin về trường Đại học Y Dược Cần Thơ
            dispatcher.utter_message(
                text=(
                    "Trường Đại học Y Dược Cần Thơ là trường đại học Khoa học Sức khỏe hệ công lập "
                    "trực thuộc Bộ Y tế duy nhất tại Đồng bằng sông Cửu Long, Việt Nam.\n"
                    "Trường Đại học Y Dược Cần Thơ cũng là một trong những trường đào tạo Y Dược tốt nhất "
                    "Việt Nam nói chung và khu vực Đồng bằng Sông Cửu Long nói riêng."
                )
            )
        else:
            # Trả lời rằng không có thông tin về trường này
            dispatcher.utter_message(
                text="Xin lỗi, hiện tại chưa có thông tin về trường bạn yêu cầu."
            )
            file_writer = write_file()
            file_writer.get_ghi_log_file('Action học phí: '+user_input)
        
        return []