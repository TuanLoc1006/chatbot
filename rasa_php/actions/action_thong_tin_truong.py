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
    def name(self):
        return "action_thong_tin_truong"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Lấy entities từ câu chat của người dùng
        entities = tracker.latest_message.get('entities', [])
        print(f"\nEntities từ input:\n {entities}")
        
        # Tạo dictionary ánh xạ các role với thông điệp tương ứng
        role_messages = {
            "thông tin": "Trường Đại học Y Dược Cần Thơ là trường đại học Khoa học Sức khỏe hệ công lập, trực thuộc Bộ Y tế duy nhất tại Đồng bằng sông Cửu Long, Việt Nam, Trường Đại học Y Dược Cần Thơ cũng là một trong những trường đào tạo Y Dược tốt nhất Việt Nam nói chung và khu vực Đồng bằng Sông Cửu Long nói riêng.",
            "lịch sử":"Lịch sử hình thành và phát triển trường đại học y dược cần thơ http://www.ctump.edu.vn/Default.aspx?tabid=2048"
        }
        
        message = ""
        
        # Phân loại các role từ entities và thêm thông điệp tương ứng
        for entity in entities:
            role = entity.get('role')
            if role in role_messages:
                message = role_messages[role]
        
        if message:
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Xin lỗi, hiện tại chưa có thông tin về trường bạn yêu cầu.")
       
        return []
# class actionThongTinTruong(Action):
#     def name(self) -> Text:
#         return "action_thong_tin_truong"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         universityy_entity = next(tracker.get_latest_entity_values('university'), None)
#         user_input = tracker.latest_message['text']
#         print("người dùng hỏi thông tin trường: "+user_input)
#         logging.info("{}{}".format('Call action_thong_tin_truong: ', universityy_entity))
#         # Tạo từ điển các từ liên quan đến "Đại học Y Dược Cần Thơ"
#         related_terms = {
#             "ctump", 
#             "đại học y dược cần thơ", 
#             "đại học y",
#             "y dược cần thơ", 
#             "trường này", 
#             "trường",
#             "ctu medical and pharmaceutical university",
#             "can tho university of medicine and pharmacy",
#             "dhydct",
#             "dh y duoc can tho",
#             "can tho y duoc",
#             "can tho y duoc university",
#             "trường đại học y dược",
#             "đại học y cần thơ",
#             "đại học y dược ct",
#             "y dược ct",
#             "thông tin trường này",
#             "thông tin trường",
            
#         }
        
#         if universityy_entity and universityy_entity.lower() in related_terms:
#             # Trả lời thông tin về trường Đại học Y Dược Cần Thơ
#             dispatcher.utter_message(
               
#                 text=f"Trường Đại học Y Dược Cần Thơ là trường đại học Khoa học Sức khỏe hệ công lập, trực thuộc Bộ Y tế duy nhất tại Đồng bằng sông Cửu Long, Việt Nam, Trường Đại học Y Dược Cần Thơ cũng là một trong những trường đào tạo Y Dược tốt nhất Việt Nam nói chung và khu vực Đồng bằng Sông Cửu Long nói riêng. "
#             )
#         else:
#             # Trả lời rằng không có thông tin về trường này
#             dispatcher.utter_message(
#                 text="Xin lỗi, hiện tại chưa có thông tin về trường bạn yêu cầu."
#             )
#             file_writer = write_file()
#             file_writer.get_ghi_log_file('Action học phí: '+user_input)
        
#         return []
    
# /////////////////////////////

class actionSuMangTamNhinTrietLyGiaoDuc(Action):
    def name(self):
        return "action_sm_tn_gtcl_tlgd"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Lấy entities từ câu chat của người dùng
        entities = tracker.latest_message.get('entities', [])
        print(f"\nEntities từ input:\n {entities}")
        
        # Tạo dictionary ánh xạ các role với thông điệp tương ứng
        role_messages = {
            "sứ mạng": "Sứ mạng: Trường Đại học Y Dược Cần Thơ có sứ mạng Đào tạo nguồn nhân lực y tế chất lượng cao; nghiên cứu khoa học, ứng dụng và chuyển giao công nghệ; bảo vệ, chăm sóc và nâng cao sức khỏe Nhân dân.</br>",
            "tầm nhìn": "Tầm nhìn: Đến năm 2025: Là một trong 05 trường đại học khoa học sức khỏe hàng đầu Việt Nam và xếp hạng trong 500 trường đại học hàng đầu Đông Nam Á.Đến năm 2030: Là một trong 05 trường đại học khoa học sức khỏe hàng đầu Việt Nam và xếp hạng trong 1000 trường đại học hàng đầu Châu Á.</br>",
            "giá trị cốt lỗi":"Giá trị cốt lỗi: Trách nhiệm - Chất lượng - Phát triển - Hội nhập</br>",
            "triết lý giáo dục":"Triết lý giáo dục: Trí tuệ - Y đức - Sáng tạo</br>",
            "mục tiêu":"I. Mục tiêu chung</br>Trường Đại học Y Dược Cần Thơ là trường đại học trọng điểm quốc gia và xếp hạng trong 500 trường đại học hàng đầu Đông Nam Á.</br>II. Mục tiêu cụ thể</br>1) Đảm bảo tiêu chuẩn đầu vào và đầu ra chất lượng cao.</br>2) Đảm bảo sự hài lòng của các bên liên quan.</br>3) Đa dạng hóa loại hình đào tạo, chương trình đào tạo và dịch vụ.</br>4) Nâng cao hiệu quả ứng dụng khoa học công nghệ.</br>5) Quản lý và khai thác hiệu quả thông tin dữ liệu quản trị Trường.</br>6) Sử dụng công nghệ số trong vận hành các hoạt động của Trường.</br>7) Phát triển nguồn nhân lực đáp ứng yêu cầu hội nhập.</br>8) Cải tiến liên tục mọi hoạt động của Trường.</br>9) Đổi mới phương thức quản trị, nâng cao văn hóa tổ chức.</br>10) Đa dạng hóa nguồn thu, tối ưu hóa chi phí hoạt động và nâng cao hiệu quả.</br>11) Phát triển Bệnh viện trường thành bệnh viện hiện đại, kỹ thuật cao của khu vực.</br>",
            "slogan":"Khẩu hiệu của trường: Tri thức cho bạn - sức khỏe cho đời"
        }
        
        message = ""
        
       
        for entity in entities:
            role = entity.get('role')
            if role in role_messages:
                message += role_messages[role]
        
        if message:
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Xin lỗi, hiện tại chưa có thông tin bạn yêu cầu.")
       
        return []