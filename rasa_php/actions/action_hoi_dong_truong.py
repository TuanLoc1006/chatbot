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



class ActionHoiDongTruong(Action):
    def name(self):
        return "action_hoi_dong_truong"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Lấy entities từ câu chat của người dùng
        entities = tracker.latest_message.get('entities', [])
        print(f"Entities từ input: {entities}")
        
        # Tạo dictionary ánh xạ các role với thông điệp tương ứng
        role_messages = {
            'chủ tịch': "</br>CHỦ TỊCH HỘI ĐỒNG TRƯỜNG ĐẠI HỌC Y DƯỢC CẦN THƠ NHIỆM KÌ 2020-2025</br>PGS.TS.BS Nguyễn Minh Phương</br>Email: nmphuong@ctump.edu.vn</br>NĂM 2017</br>- Phó bí thư Đảng ủy</br>- Trưởng phòng Đào tạo Đại học</br>NĂM 2018-2019</br>- Phó bí thư Đảng ủy</br>- Phó Hiệu Trưởng</br>NĂM 2020-2021</br>- Bí thư Đảng ủy</br>- Phó Hiệu Trưởng</br>NĂM 2022</br>- Bí thư Đảng ủy</br>- Chủ tịch hội đồng Trường",
            
            'thành viên':"</br>PGS.TS.Nguyễn Minh Phương - Chủ tịch hội đồng trường và danh sách thành viên Hội đồng Trường nhiệm kì 2020-2025</br>- GS.TS. Nguyễn Trung Kiên - Thành viên Hội đồng trường</br>- PGS.TS. Nguyễn Thành Tấn - Thành viên Hội đồng trường</br>- TS. Nguyễn Minh Lợi - Thành viên Hội đồng trường</br>- PGS.TS. Nguyễn Văn Lâm - Thành viên Hội đồng trường</br>- PGS.TS. Đàm Văn Cương - Thành viên Hội đồng trường</br>- PGS.TS. Trần Viết An - Thành viên Hội đồng trường</br>- BS.CK2. Lại Văn Nông - Thành viên Hội đồng trường</br>- PGS.TS. Trương Nhựt Khuê - Thành viên Hội đồng trường</br>- PGS.TS. Phạm Thanh Suối - Thành viên Hội đồng trường</br>- TS. Ngô Văn Truyền - Thành viên Hội đồng trường</br>- ThS. Nguyễn Văn Tám - Thành viên Hội đồng trường</br>- TS. Nguyễn Thị Quyên Thanh - Thành viên Hội đồng trường</br>- BS.CK2. Nguyễn Minh Vũ - Thành viên Hội đồng trường</br>- BS.CK2. Từ Quốc Tuấn - Thành viên Hội đồng trường</br>- BS.CK2. Phạm Phú Trường Giang - Thành viên Hội đồng trường</br>- TS. Trần Thanh Hùng - Thành viên Hội đồng trường</br>- SV. Triệu Phương Hằng - Thành viên Hội đồng trường</br>- TS. Võ Phạm Minh Thư - Thư ký Hội đồng Trường</br>"
        }
        
        message = ""
        
        # Phân loại các role từ entities và thêm thông điệp tương ứng
        for entity in entities:
            role = entity.get('role')
            if role in role_messages:
                message += role_messages[role]
        
        if message:
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Không tìm thấy thông tin phù hợp.")
        
        return []

