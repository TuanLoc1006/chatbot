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



class ActionBanGiamHieu(Action):
    def name(self):
        return "action_ban_giam_hieu"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Lấy entities từ câu chat của người dùng
        entities = tracker.latest_message.get('entities', [])
        print(f"Entities từ input: {entities}")
        
        # Tạo dictionary ánh xạ các role với thông điệp tương ứng
        role_messages = {
            'thông tin':"</br>GS.TS Nguyễn Trung Kiên - Hiệu Trưởng</br>Email: ntkien@ctump.edu.vn</br>PGS.TS Nguyễn Văn Lâm - Phó Hiệu Trưởng</br>Email: nvlam@ctump.edu.vn</br>PGS.TS Trần Viết An - Phó Hiệu Trưởng</br>Email: tvan@ctump.edu.vn</br>PGS.TS Nguyễn Thành Tấn - Phó Hiệu Trưởng</br>Email: nttan@ctump.edu.vn</br>",
            'hiệu trưởng': "</br>GS.TS Nguyễn Trung Kiên - Hiệu Trưởng</br>Email: ntkien@ctump.edu.vn</br>Phụ trách các lĩnh vực:</br>Phụ trách chung, lãnh đạo toàn diện mọi mặt hoạt động và công tác của Trường; quản lý trường, phó các đơn vị thuộc và trực thuộc.</br>Trực tiếp chỉ đạo các lĩnh vực:</br>- Công tác quy hoạch; xây dựng chiến lược, kế hoạch phát triển dài hạn, trung hạn, ngắn hạn trong các mặt công tác.</br>- Công tác chính trị tư tưởng và bảo vệ chính trị nội bộ.</br> - Công tác tổ chức cán bộ, thi đua khen thưởng, chế độ chính sách, đảm bảo chất lượng, thanh tra pháp chế.",
        
            'phó hiệu trưởng':"</br>PGS.TS Nguyễn Văn Lâm - Phó Hiệu Trưởng</br>Email: nvlam@ctump.edu.vn</br>Phụ trách các lĩnh vực:</br>Giúp Hiệu trưởng chỉ đạo và phụ trách các lĩnh vực sau:</br>- Quản lý và đổi mới công tác đào tạo, phát triển chương trình đào tạo và liên kết đào tạo sau đại học.</br>- Các chương trình, kế hoạch, học tác quốc tế và đối ngoại.- Nghiên cứu và ứng dụng chuyên sâu.</br>Thư viện.</br>PGS.TS Trần Viết An - Phó Hiệu Trưởng</br>Email: tvan@ctump.edu.vn</br>Phụ trách các lĩnh vực:</br>Giúp Hiệu trưởng chỉ đạo và phụ trách các lĩnh vực sau:</br>- Quản lý và đổi mới công tác đào tạo, phát triển chương trình đào tạo và liên kết đào tạo đại học.</br>- Khảo thí.</br>- Quản lý và hỗ trợ người học.</br>- Dịch vụ và đào tạo theo nhu cầu xã hội.</br>- Thông tin và truyền thông.</br>PGS.TS Nguyễn Thành Tấn - Phó Hiệu Trưởng</br>Email: nttan@ctump.edu.vn</br>Phụ trách các lĩnh vực:</br>- Giúp Hiệu trưởng chỉ đạo và phụ trách các lĩnh vực sau:</br>- Cải cách hành chính; đầu tư mua sắm; xây dựng cơ sở hạ tầng.</br>- An ninh trật tự, an toàn, phòng chống cháy nổ.</br>- Hoạt động đoàn thể chính trị xã hội.</br>- Công tác đối ngoại liên đới với bệnh viện trường.</br>- Đảm bảo quyền lợi của người học, công đoàn và bảo vệ quyền lợi chính đáng cho người lao động.</br>- Đặc biệt phát ngôn và quan hệ công chúng, đối ngoại và truyền thông, tổ chức chỉ đạo.</br>",
            "các thành viên":"</br>GS. TS. BS. Nguyễn Trung Kiên , Hiệu trưởng, Email: ntkien@ctump.edu.vn</br>PGS.TS. BS. Nguyễn Văn Lâm, Phó Hiệu Trưởng, Email: nvlam@ctump.edu.vn</br>PGS. TS. BS. Trần Viết An, Phó Hiệu Trưởng, Email: tvan@ctump.edu.vn</br>PGS.TS. BS. Nguyễn Thành Tấn, Phó Hiệu Trưởng, Email: nttan@ctump.edu.vn</br>"
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
            dispatcher.utter_message(text="Không tìm thấy thông tin phù hợp.")
        
        return []

