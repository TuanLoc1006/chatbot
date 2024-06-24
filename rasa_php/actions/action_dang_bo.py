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



class ActionDangBo(Action):
    def name(self):
        return "action_dang_bo"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Lấy entities từ câu chat của người dùng
        entities = tracker.latest_message.get('entities', [])
        print(f"Entities từ input: {entities}")
        
        # Tạo dictionary ánh xạ các role với thông điệp tương ứng
        role_messages = {
            'thông tin': "</br>Đảng bộ cấp trên: Đảng bộ thành phố Cần Thơ</br>Tên: Đảng bộ Trường Đại học Y Dược Cần Thơ</br>Địa chỉ: Số 179, đường Nguyễn Văn Cừ, phường An Khánh, quận Ninh Kiều, thành phố CầThơ</br>Liên hệ:</br>Số điện thoại: 0292.3600376</br>Số fax: 0292.740221</br>Website: http://www.ctump.edu.vn</br> Email: vpdu@ctump.edu.vn</br>",
            'lịch sử': "</br>Đảng bộ cơ sở Trường Đại học Y Dược Cần Thơ được thành lập theo Quyết định số 212-QĐ/ĐUK ngày 26/05/2003 trực thuộc Đảng bộ Khối Cơ quan Dân chính Đảng thành phố Cần Thơ.</br>Ngày 06/02/2012, Đảng bộ Trường đã được Thành ủy Cần Thơ trao quyết định số 498-QĐ/TU ngày 02/02/2012 về việc chuyển Đảng bộ cơ sở Trường Đại học Y Dược Cần Thơ trực thuộc Đảng bộ thành phố Cần Thơ và được giao một số quyền của Đảng bộ cấp trên cơ sở.</br>Ngày 19/11/2021, Đảng bộ Trường đã được Thành ủy Cần Thơ trao quyết định số 383-QĐ/TU ngày 17/11/2021 về việc thành lập Đảng bộ Trường Đại học Y Dược Cần Thơ trực thuộc Thành ủy Cần Thơ có tư cách pháp nhân, có con dấu và tài khoản riêng.</br>",
            'ban chấp hành đảng bộ': "</br>Ban chấp hành đảng bộ nhiệm kì 2020-2025</br>- Đ/c Trần Viết An</br>- Đ/c Trần Trương Ngọc Bích</br>- Đ/c Trần Thanh Hùng</br>- Đ/c Trần T. Thanh Hương</br>- Đ/c Lê Minh Hữu</br>- Đ/c Phạm Hoàng Khánh</br>- Đ/c Trương Nhật Khuê</br>- Đ/c Lê Văn Minh</br>- Đ/c Phạm Thành Suôi</br>- Đ/c Nguyễn Thành Tấn</br>- Đ/c Đỗ Châu Minh Vĩnh Thọ</br>- Đ/c Võ Phạm Minh Thư</br>- Đ/c Nguyễn Thị Thu Trâm</br>- Đ/c Nguyễn Triều Việt</br>"
            
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


class ActionDangUy(Action):
    def name(self):
        return "action_dang_uy"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Lấy entities từ câu chat của người dùng
        entities = tracker.latest_message.get('entities', [])
        print(f"Entities từ input: {entities}")
        
        # Tạo dictionary ánh xạ các role với thông điệp tương ứng
        role_messages = {
            'thông tin': "</br>Thông tin cơ bản đảng ủy gôm:</br>- Văn phòng</br>- Ban tổ chức</br> - Ban tuyên giáo</br> - Ủy ban kiểm tra",
            'cơ cấu tổ chức': "</br>Đảng ủy gồm 2 chi bộ đó là:</br>CHI BỘ CƠ SỞ:</br>- Chi bộ Hành chính</br>- Chi bộ Tổ chức -  Khoa học</br>- Chi bộ Tài chính</br>- Chi bộ Quản trị thiết bị</br>- Chi bộ Đào tạo</br>- Chi bộ Thông tin -  Thư viện</br>- Chi bộ Giáo dục y học</br>- Chi bộ Trung tâm Đào tạo theo nhu cầu</br>- Chi bộ Khoa học cơ bản</br>ĐẢNG BỘ CƠ SỞ</br>- Đảng bộ bệnh viện</br>- Đảng bộ Khoa Y</br>- Đảng bộ Chính quy Y</br>- Đảng bộ Liên thông Y</br>- Đảng bộ Răng Hàm Mặt</br>- Đảng bộ Dược</br>- Đảng bộ Y tế công cộng</br>- Đảng bộ Điều dưỡng</br>- Đảng bộ Y học cổ truyền",
            'bí thư': "</br>Bí thư qua các thời kì</br>Nhiệm kỳ 2005-2008: Đồng chí Lê Thế Thự</br>Nhiệm kỳ 2008-2010: Đồng chí Phạm Văn Đại</br>Nhiệm kỳ 2010-2015: Đồng chí Phạm Văn Linh</br>Nhiệm kỳ 2015-2020: Đồng chí Nguyễn Trung Kiên</br>Nhiệm kỳ 2020-2025: Đồng chí Nguyễn Minh Phương</br>",
            'ban thường vụ': "</br>Ban thường vụ đảng ủy nhiệm kì 2020-2025</br>Đ/c Nguyễn Trung Kiên: Phó Bí thư Đảng ủy Hiệu trưởng</br> Đ/c Nguyễn Minh Phương: Bí thư Đảng ủy Chủ tịch Hội đồng Trường</br> Đ/c Nguyễn Văn Lâm: Phó Bí thư Đảng ủy Phó Hiệu trưởng</br> Đ/c Lại Văn Nông: Ủy viên Ban Thường vụ Đảng ủy Giám đốc Bệnh viện</br> Đ/c Nguyễn Văn Tám: Ủy viên Ban Thường vụ Đảng ủy Phó Giám đốc Bệnh viện",
            'vị trí': "</br>Đảng ủy Trường Đại học Y Dược Cần Thơ trực thuộc Thành ủy Cần Thơ, là cấp ủy cấp trên trực tiếp của tổ chức cơ sở đảng; chịu sự lãnh đạo chỉ đạo trực tiếp, thường xuyên của Ban Chấp hành, Ban Thường vụ Thành ủy.",
            'chức năng': "</br>Lãnh đạo việc thực hiện nhiệm vụ chính trị, công tác tổ chức cán bộ, công tác xây dựng Đảng, xây dựng đơn vị và công tác quần chúng; tham mưu đề xuất với Thành ủy, Ban Cán sự Đảng Bộ Y tế và các ban, ngành có liên quan về các giải pháp lãnh đạo thực hiện nhiệm vụ chính trị, công tác xây dựng Đảng trong toàn đảng bộ; lãnh đạo tổ chức đảng trực thuộc phát huy vai trò hạt nhân chính trị, lãnh đạo cán bộ, đảng viên chấp hành đường lối và thực hiện, chủ trương của Đảng, chính sách, pháp luật của Nhà nước, hoàn thành tốt nhiệm vụ chính trị của đơn vị, xây dựng tổ chức đảng trong sạch, vững mạnh gắn với xây dựng chính quyền và đoàn thể trong đơn vị vững mạnh.</br>Lãnh xây dựng và thực hiện nhiệm vụ công tác đào tạo nguồn nhân lực y tế; nghiên cứu khoa học, ứng dụng, chuyển giao công nghệ và chăm sóc sức khỏe nhân dân.",
            'nhiệm vụ': "</br>Lãnh đạo thực hiện nhiệm vụ chính trị</br>Lãnh đạo thực hiện công tác giáo dục chính trị, tư tưởng</br>Lãnh đạo công tác xây dựng tổ chức đảng và đảng viên</br>Lãnh đạo công tác tổ chức, cán bộ</br>Lãnh đạo và thực hiện công tác kiểm tra, giám sát</br>Lãnh đạo các đoàn thể chính trị - xã hội</br>Lãnh đạo công tác bảo vệ chính trị nội bộ</br>"
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

    





class ActionLanhDaoDangDoanThe(Action):
    def name(self):
        return "action_lanh_dao_dang_doan_the"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message['text']
        print("người dùng hỏi về lãnh đạo: " + user_input)
        # Lấy entities từ câu chat của người dùng
        entities = tracker.latest_message.get('entities', [])
        print(f"Entities từ input: {entities}")
        
        # Tạo dictionary ánh xạ các role với thông điệp tương ứng
        role_messages = {
            'hội đồng trường':'PGS.TS. BS. Nguyễn Minh Phương, Chủ tịch, Email: nmphuong@ctump.edu.vn',
            'đảng và các đoàn thể': "</br>PGS.TS. BS. Nguyễn Minh Phương, Bí thư Đảng ủy, Email: nmphuong@ctump.edu.vn</br>TS. BS. Trần Thanh Hùng, Chủ tịch công đoàn Trường, Email: tthung@ctump.edu.vn</br>TS. BS. Phạm Hoàng Khánh, Bí thư Đoàn TNCSHCM Trường, Email: phkhanh@ctump.edu.vn</br>PGS.TS. BS. Lê Thành Tài, Chủ tịch Hội cựu chiến binh, Email: lttai@ctump.edu.vn</br>",
            "khoa y":"Khoa Y</br>TS.BS. Lê Văn Minh, Trưởng Khoa, Email: lvminh@ctump.edu.vn</br>TS.BS. Trần Thái Thanh Tâm, Phó Trưởng Khoa, Email: ttttam@ctump.edu.vn</br>TS. BS. Nguyễn Như Nghĩa, Phó Trưởng Khoa, Email: nnnghia@ctump.edu.vn</br>",
            "khoa dược":"Khoa Dược</br>PGS.TS. DS Phạm Thành Suôl, Trưởng Khoa, Email: ptsuol@ctump.edu.vn</br>PGS.TS.DS. Đỗ Châu Minh Vĩnh Thọ, Phó Trưởng Khoa, email: dcmvtho@ctump.edu.vn</br>TS. DS Phạm Thị Tố Liên, Phó Trưởng Khoa, Email: pttlien@ctump.edu.vn</br>",
            "khoa răng hàm mặt":"Khoa Răng hàm mặt</br>PGS.TS. BS Trương Nhựt Khuê, Trưởng Khoa, Email: tnkhue@ctump.edu.vn</br>PGS.TS.BS. Lê Nguyên Lâm, Phó Trưởng Khoa, Email: lnlam@ctump.edu.vn</br>TS. BS. Đỗ Thị Thảo, Phó Trưởng Khoa, Email: dtthao@ctump.edu.vn</br>",
            "khoa y tế công cộng":"Khoa Y Tế Công Cộng</br>TS. BS. Lê Minh Hữu, Trưởng Khoa , Email: lmhuu@ctump.edu.vn</br>TS. BS. Nguyễn Tấn Đạt, Phó Trưởng Khoa, Email: ntdat@ctump.edu.vn</br>",
            "khoa điều dưỡng":"Khoa Điều dưỡng</br>TS. BS Nguyễn Hồng Phong, Trưởng Khoa , Email: nhphong@ctump.edu.vn</br>TS. ĐD. Nguyễn Thị Thanh Trúc, Phó Trưởng Khoa, Email: ntttruc@ctump.edu.vn</br>",
            "khoa kỹ thuật y học":"Khoa Kỹ thuật y học</br>TS. BS Nguyễn Hồng Phong, Trưởng Khoa , Email: nhphong@ctump.edu.vn</br>TS. ĐD. Nguyễn Thị Thanh Trúc, Phó Trưởng Khoa, Email: ntttruc@ctump.edu.vn</br>",
            "khoa học cơ bản":"Khoa học cơ bản</br>PGS.TS. Nguyễn Thị Thu Trâm, Trưởng Khoa, Email: ntttram@ctump.edu.vn</br>ThS. Nguyễn Thanh Hùng, Phó Trưởng Khoa, Email: nthung@ctump.edu.vn</br>TS. Trần Thị Hồng Lê, Phó Trưởng Khoa, Email: tthle@ctump.edu.vn</br>",
            "khoa y học cổ truyền":"Khoa Y học cổ truyền</br>TS. BS. Lê Minh Hoàng , Trưởng Khoa, Email: lmhoang@ctump.edu.vn</br>ThS. BS. Nguyễn Ngọc Chi Lan , Phó Trưởng  Khoa, Email: nnclan@ctump.edu.vn</br>",
            
            "phòng thông tin và truyền thông":"Phòng Thông tin và Truyền thông</br>ThS. Châu Minh Khoa, Trưởng Phòng, Email: cmkhoa@ctump.edu.vn</br>ThS. Trần Thị Bích Phương, Phó Trưởng Phòng, Email: ttbphuong@ctump.edu.vn</br>",
            "phòng công tác sinh viên":"Phòng Công tác sinh viên</br>ThS. Ngô Phương Thảo, Trưởng phòng, Email: npthao@ctump.edu.vn</br>ThS. Võ Văn Quyền, Phó Trưởng phòng, Email: vvquyen@ctump.edu.vn</br>",
            "phòng đảm bảo chất lượng":"Phòng đảm bảo chất lượng</br>ThS. BS. Phạm Thị Mỹ Ngọc, Trưởng Phòng, Email: ptmngoc@ctump.edu.vn</br>",
            "phòng đào tạo đại học":"Phòng Đào tạo Đại học</br>TS. BS. Phạm Kiều Anh Thơ, Trưởng phòng, Email: pkatho@ctump.edu.vn</br>TS. BS. Trần Quang Khải, Phó Trưởng phòng, Email: tqkhai@ctump.edu.vn</br>",
            "phòng đào tạo sau đại học":"Phòng Đào tạo Sau đại học</br>GS.TS. BS Võ Huỳnh Trang, Trưởng phòng, Email: vhtrang@ctump.edu.vn</br>TS. BS. Nguyễn Hồng Hà, Phó Trưởng phòng, Email: nhha@ctump.edu.vn</br>TS. DS Đặng Duy Khánh, Phó Trưởng phòng , Email: ddkhanh@ctump.edu.vn</br>",
            "phòng hành chính tổng hợp":"Phòng Hành chính tổng hợp</br>ThS. Phạm Trương Yến Nhi , Trưởng phòng, Email: ptynhi@ctump.edu.vn</br>ThS. Phạm Thị Minh, Phó Trưởng phòng, Email: ptminh@ctump.edu.vn</br>CN. Nguyễn Văn Bộ, Phó Trưởng phòng, Email: nvbo@ctump.edu.vn</br>",
            "phòng khảo thi":"Phòng Khảo thí</br>ThS. Phan Thị Tuyết Nhung, Trưởng Phòng, Email: pttnhung@ctump.edu.vn</br>Ths. DS. Lê Thị Minh Ngọc, Phó Trưởng Phòng, Email: ltmngoc@ctump.edu.vn</br>",
            "phòng khoa học công nghệ và quan hệ đối ngoại":"Phòng Khoa học công nghệ và Quan hệ đối ngoại</br>PGS. TS. DS. Nguyễn Thị Ngọc Vân, Trưởng phòng, Email:  ntnvan@ctump.edu.vn</br>PGS.TS. DS. Nguyễn Thắng, Phó Trưởng phòng, Email: nthang@ctump.edu.vn</br>TS. BS. Hoàng Minh Tú, Phó Trưởng phòng, Email: hmtu@ctump.edu.vn</br>",
            "phòng quản trị thiết bị":"Phòng Quản trị thiết bị</br>ThS. Nguyễn Văn Tám, Trưởng phòng, Email: nvtam@ctump.edu.vn</br>ThS. Huỳnh Trường Hiệp, Phó Trưởng phòng, Email: hthiep@ctump.edu.vn</br>",
            "phòng tài chính kế toán":"Phòng Tài chính kế toán</br>ThS. Võ Nhật Nhân Tuyền, Trưởng phòng, Email: vnntuyen@ctump.edu.vn</br>CN. Hứa Kim Chi, Phó Trưởng phòng, Email: hkchi@ctump.edu.vn</br>",
            "phòng tổ chức cán bộ":"Phòng Tổ chức Cán bộ</br>ThS. Trần Trương Ngọc Bích, Trưởng Phòng, Email:  ttnbich@ctump.edu.vn</br>ThS. Hà Bảo Trân, Phó Trưởng phòng, Email: hbtran@ctump.edu.vn</br>",
            "phòng thanh tra pháp chế":"Phòng Thanh tra - Pháp chế</br>TS. BS. Bùi Quang Nghĩa, Trưởng Phòng, Email: bqnghia@ctump.edu.vn</br>CN. Nguyễn Hiệp Phúc, Phó Trưởng phòng, Email: nhphuc@ctump.edu.vn</br>",
            "ban quản lý dự án":"Ban Quản lý dự án</br>KS. Nguyễn Chí Trung, Phó Trưởng Ban, Email: nctrung@ctump.edu.vn</br>",
            "trung tâm dịch vụ và đào tạo theo nhu cầu xã hội":"Trung tâm Dịch vụ và Đào tạo theo nhu cầu xã hội</br>TS. BS. Nguyễn Triều Việt, Giám đốc, Email: ntviet@ctump.edu.vn</br>TS. Phan Thị Luyện, Phó Giám đốc, Email: ptluyen@ctump.edu.vn</br>",
            "trung tâm giáo dục y học và huấn luyện kỹ năng y khoa":"Trung tâm Giáo dục y học và Huấn luyện kỹ năng y khoa</br>ThS. BS Phạm Thị Mỹ Ngọc, Trưởng Trung tâm, Email: ptmngoc@ctump.edu.vn</br>ThS. BS. Trần Xuân Quỳnh, Phó Trưởng Trung tâm, Email: txquynh@ctump.edu.vn</br>",
            "thư viện":"Thư viện</br>TS. BS. Nguyễn Thị Hải Yến, Giám đốc, Email: nthyen@ctump.edu.vn</br>TS.BS. Lê Thị Hoàng Mỹ , Phó Giám đốc, Email: lthmy@ctump.edu.vn</br>",
            "bệnh viện":"BỆNH VIỆN</br>BSCKII. Lại Văn Nông, Giám đốc, Email: lvnong@ctump.edu.vn.</br>PGS. TS.BS. Nguyễn Thành Tấn, Phó Giám đốc, Email: nttan@ctump.edu.vn</br>ThS. Nguyễn Văn Tám, Phó Giám đốc, Email: nvtam@ctump.edu.vn</br>TS. BS. Võ Phạm Minh Thư, Phó Giám đốc, Email: vpmthu@ctump.edu.vn</br>"
            

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
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_thanh_phi_bao_hiem_tai_nan: '+user_input)
        
        return []
