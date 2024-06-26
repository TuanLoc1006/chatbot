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
        print(f"\nEntities từ input: \n{entities}")
        
        # Tạo dictionary ánh xạ các role với thông điệp tương ứng
        infor_hoi_dong_truong = {
            "thông tin":"HỘI ĐỒNG TRƯỜNG GỒM:</br>- TỔ THƯ KÝ GIÚP VIỆC</br>- BAN ĐT-NCKH-KCB</br>- BAN TỔ CHỨC-NS</br>- BAN TÀI CHÍNH-CSVC",
            "chủ tịch": "</br>CHỦ TỊCH HỘI ĐỒNG TRƯỜNG ĐẠI HỌC Y DƯỢC CẦN THƠ NHIỆM KÌ 2020-2025</br>PGS.TS.BS Nguyễn Minh Phương</br>Email: nmphuong@ctump.edu.vn</br>NĂM 2017</br>- Phó bí thư Đảng ủy</br>- Trưởng phòng Đào tạo Đại học</br>NĂM 2018-2019</br>- Phó bí thư Đảng ủy</br>- Phó Hiệu Trưởng</br>NĂM 2020-2021</br>- Bí thư Đảng ủy</br>- Phó Hiệu Trưởng</br>NĂM 2022</br>- Bí thư Đảng ủy</br>- Chủ tịch hội đồng Trường",
            "thành viên":"</br>PGS.TS.Nguyễn Minh Phương - Chủ tịch hội đồng trường và danh sách thành viên Hội đồng Trường nhiệm kì 2020-2025</br>- GS.TS. Nguyễn Trung Kiên - Thành viên Hội đồng trường</br>- PGS.TS. Nguyễn Thành Tấn - Thành viên Hội đồng trường</br>- TS. Nguyễn Minh Lợi - Thành viên Hội đồng trường</br>- PGS.TS. Nguyễn Văn Lâm - Thành viên Hội đồng trường</br>- PGS.TS. Đàm Văn Cương - Thành viên Hội đồng trường</br>- PGS.TS. Trần Viết An - Thành viên Hội đồng trường</br>- BS.CK2. Lại Văn Nông - Thành viên Hội đồng trường</br>- PGS.TS. Trương Nhựt Khuê - Thành viên Hội đồng trường</br>- PGS.TS. Phạm Thanh Suối - Thành viên Hội đồng trường</br>- TS. Ngô Văn Truyền - Thành viên Hội đồng trường</br>- ThS. Nguyễn Văn Tám - Thành viên Hội đồng trường</br>- TS. Nguyễn Thị Quyên Thanh - Thành viên Hội đồng trường</br>- BS.CK2. Nguyễn Minh Vũ - Thành viên Hội đồng trường</br>- BS.CK2. Từ Quốc Tuấn - Thành viên Hội đồng trường</br>- BS.CK2. Phạm Phú Trường Giang - Thành viên Hội đồng trường</br>- TS. Trần Thanh Hùng - Thành viên Hội đồng trường</br>- SV. Triệu Phương Hằng - Thành viên Hội đồng trường</br>- TS. Võ Phạm Minh Thư - Thư ký Hội đồng Trường</br>",
            "sơ đồ tổ chức":'Sơ đồ tổ chức trường đại học y dược cần thơ gồm:</br>- Đảng ủy trường</br>- Hội đồng trường</br>- Ban giám hiệu</br>- Các hội đồng tư ván</br> Công đoàn, Đoàn TN-Hội SV, Hội cựu chiến binh và các đơn vị hỗ trợ khác... http://www.ctump.edu.vn/Default.aspx?tabid=229',
            "nhiệm vụ":"CHỨC NĂNG NHIỆM VỤ</br>Chức năng, nhiệm vụ và quyền hạn của Hội đồng Trường thực hiện theo: Luật Giáo dục đại học số 08/2012/QH13; Quyết định số 70/2014/QĐ- TTg Điều lệ trường đại học; Quyết định số 455/QĐ-TTg ngày 13/04/2017 của Thủ tướng Chính phủ về việc phê duyệt Đề án thí điểm đổi mới cơ chế hoạt động của Trường Đại học Y Dược Cần Thơ; Quyết định số 3329/QĐ-BYT ngày 19/7/2017 của Bộ Y tế về việc thành lập Hội đồng trường thuộc Trường Đại học Y Dược Cần Thơ;</br>Nhiệm vụ và quyền hạn của Hội đồng trường</br>1. Quyết định chiến lược, quy hoạch, kế hoạch phát triển và quy chế về tổ chức và hoạt động của nhà trường;</br>2. Quyết nghị phương hướng hoạt động đào tạo, khoa học và công nghệ, hợp tác quốc tế, đảm bảo chất lượng giáo dục;</br>3. Quyết nghị và có các chủ trương, biện pháp nhằm duy trì và phát triển của nhà trường;</br>4. Quyết định về việc thành lập, sáp nhập, chia, tách, giải thể các tổ chức của nhà trường;</br>5. Giám sát việc thực hiện các nghị quyết của Hội đồng trường, việc thực hiện quy chế dân chủ trong các hoạt động của nhà trường;</br>6. Định kỳ hàng năm hoặc đột xuất báo cáo, giải trình với Bộ Y tế, Bộ Giáo dục và Đào tạo về các điều kiện đảm bảo chất lượng, các kết quả hoạt động, việc thực hiện các cam kết và tài chính của nhà trường;</br>7. Kiến nghị cơ quan có thẩm quyền thông qua phương án bổ sung, miễn nhiệm hoặc thay thế các thành viên của hội đồng trường;</br>8. Thông qua quy chế tổ chức và hoạt động, quy chế tài chính, vị trí việc làm; việc tuyển dụng, quy định mức thu, chi, học phí, lệ phí tuyển sinh, chính sách học bổng của nhà trường;</br>9. Đề nghị Bộ Y tế công nhận và miễn nhiệm hiệu trưởng, giám đốc bệnh viện thực hành trực thuộc trường; Giám sát hoạt động của hiệu trưởng. Bãi bỏ quyết định của hiệu trưởng, các phó hiệu trưởng, giám đốc bệnh viện thực hành trái với nghị quyết của hội đồng trường. Tổ chức đánh giá hiệu trưởng hằng năm và định kỳ theo quy định của Bộ Y tế và pháp luật. Đề nghị Bộ Y tế kiểm tra việc hoàn thành nhiệm vụ của hiệu trưởng, các phó hiệu trưởng. Kiến nghị Bộ Y tế miễn nhiệm hiệu trưởng, các phó hiệu trưởng không hoàn thành nhiệm vụ hiệu trưởng, phó hiệu trưởng giữa nhiệm kỳ hoặc đột xuất trong trường hợp cần thiết;</br>10. Yêu cầu hiệu trưởng giải trình về những vấn đề chưa được thực hiện đúng, không thực hiện hoặc thực hiện trái với nghị quyết của hội đồng trường (nếu có). Nếu hội đồng trường không đồng ý với giải trình của hiệu trưởng thì báo cáo Bộ Y tế xem xét, quyết định.</br>",
            "thư ký":"TS. Võ Phạm Minh Thư</br>THƯ KÝ HỘI ĐỒNG TRƯỜNG</br>(Từ tháng 11/2018 đến nay)",
            
        }
        
        input_value = None
        
        for entity in entities:
            if entity.get('entity') == "hoi_dong_truong":
                input_value = entity.get('value')
                print("----"+input_value)
        if input_value in infor_hoi_dong_truong:
            response = infor_hoi_dong_truong[input_value]
        else:
            response= "Xin lỗi, tôi không có thông tin về câu hỏi của bạn."
        dispatcher.utter_message(text=response)
        return []

