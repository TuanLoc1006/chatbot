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

# from .action_thong_tin_truong import actionThongTinTruong

# from .action_hoc_phi import actionHocPhi, actionHocPhiCoTangKhong, actionCacPhuongThucThanhToan, actionHoTroVayTienHoc

# from .action_ctdt_moi_nganh import actionNganh, actionChuongTrinhDaoTao

# from .action_khoa_phong_ban import actionHoiThongTinKhoa, actionHoiDiaDiemKhoa, actionHoiEmailKhoa, actionHoiSoDienThoaiKhoa, actionHoiThongTinPhong, actionHoiDiaDiemPhong, actionHoiEmailPhong, actionHoiSoDienThoaiPhong

# from .action_dang_ky_giay_xac_nhan import actionDangKyGiayXacNhan


# # phuong
# handledb = handleDB()
# get_connect = handledb.get_connect()
# get_nganh = handledb.get_nganh()


# """  liên quan học phí    """

# class ActionHocPhi(actionHocPhi):
#     pass

# class ActionHocPhiCoTangKhong(actionHocPhiCoTangKhong):
#     pass

# class ActionCacPhuongThucThanhToan(actionCacPhuongThucThanhToan):
#     pass

# class ActionHoTroVayTienHoc(actionHoTroVayTienHoc):
#     pass

# """  liên quan thông tin khoa   """

# class ActionHoiThongTinKhoa(actionHoiThongTinKhoa):
#     pass

# class ActionHoiDiaDiemKhoa(actionHoiDiaDiemKhoa):
#     pass

# class ActionHoiEmailKhoa(actionHoiEmailKhoa):
#     pass

# class ActionHoiSoDienThoaiKhoa(actionHoiSoDienThoaiKhoa):
#     pass


# """  liên quan thông tin phòng ban   """

# class ActionHoiThongTinPhong(actionHoiThongTinPhong):
#     pass

# class ActionHoiDiaDiemPhong(actionHoiDiaDiemPhong):
#     pass

# class ActionHoiEmailPhong(actionHoiEmailPhong):
#     pass

# class ActionHoiSoDienThoaiPhong(actionHoiSoDienThoaiPhong):
#     pass



# """ liên quan trường"""

# class ActionThongTinTruong(actionThongTinTruong):
#     pass



# """  ngành và chương trình đào tạo  """
# class actionNganh(actionNganh):
#     pass

# class actionChuongTrinhDaoTao(actionChuongTrinhDaoTao):
#     pass






    

class actionCapLaiEmailSv(Action):
    def name(self):
        return "action_cap_lai_email_sv"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cap_lai_email_entity = next(tracker.get_latest_entity_values('cap_lai_email_sv'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi cấp email: " + user_input)
        logging.info("{}{}".format('Call action_cap_lai_email_sv: ', cap_lai_email_entity))
        
        if cap_lai_email_entity:  
            dispatcher.utter_message(text=f"</br>Sinh viên liên hệ thầy Xô (Trung tâm CNTT), hoặc qua email: tvxo@ctump.edu.vn")  
        else:
            dispatcher.utter_message(text=f"Đã xảy ra lỗi khi yêu cầu cấp lại email sinh viên")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_email_sv: '+user_input)
        return []
    

class actionCapLaiBaohiemTaiNan(Action):
    def name(self):
        return "action_cap_lai_thanh_phi_bao_hiem_tai_nan"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        bhtn_entity = next(tracker.get_latest_entity_values('cap_lai_thanh_phi_bao_hiem_tai_nan'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi về bảo hiểm tai nạn: " + user_input)
        logging.info("{}{}".format('Call action_cap_lai_thanh_phi_bao_hiem_tai_nan: ', bhtn_entity))
        
        if bhtn_entity:  
            dispatcher.utter_message(text=f"</br>Sinh viên liên hệ Cô Linh (phòng đào tạo)</br> Địa chỉ: Tầng trệt, Khoa Y, Trường Đại học Y Dược Cần Thơ</br> Điện thoại: 0292. 3 831 531</br>Email: daotao@ctump.edu.vn")  
        else:
            dispatcher.utter_message(text=f"Đã xảy ra lỗi khi yêu cầu cấp lại bảo hiểm tai nạn cho sinh viên")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_thanh_phi_bao_hiem_tai_nan: '+user_input)
        return []


class actionCapLaiTkQuanLyDaoTao(Action):
    def name(self):
        return "action_cap_lai_tai_khoan_quan_ly_dao_tao"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        tkdt_entity = next(tracker.get_latest_entity_values('cap_lai_tai_khoan_quan_ly_dao_tao'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi về bảo hiểm tai nạn: " + user_input)
        logging.info("{}{}".format('Call action_cap_lai_tai_khoan_quan_ly_dao_tao: ', tkdt_entity))
        
        if tkdt_entity:  
            dispatcher.utter_message(text=f"</br>Sinh viên liên hệ Thầy Hiệp (phòng đào tạo đại học)</br> Địa chỉ: Tầng trệt, Khoa Y, Trường Đại học Y Dược Cần Thơ</br> Điện thoại: 0292. 3 831 531</br>Email: daotao@ctump.edu.vn")  
        else:
            dispatcher.utter_message(text=f"Đã xảy ra lỗi khi yêu cầu cấp lại tài khoản quản lý đào tạo")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_tai_khoan_quan_ly_dao_tao: '+user_input)
        return []


class actionCapLaiTheSv(Action):
    def name(self):
        return "action_cap_lai_the_sv"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        theSv_entity = next(tracker.get_latest_entity_values('cap_lai_the_sv'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi cấp lại thẻ sinh viên: " + user_input)
        logging.info("{}{}".format('Call action_cap_lai_the_sv: ', theSv_entity))
        
        if theSv_entity:  
            dispatcher.utter_message(text=f"</br>Để cấp lại thẻ sinh viên, bạn vui lòng xem đầy đủ thông tin tại đây http://www.ctump.edu.vn/?tabid=3130&ndid=18047&key=Quy_trinh_cap_lai_the_sinh_vien")  
        else:
            dispatcher.utter_message(text=f"Đã xảy ra lỗi khi yêu cầu cấp lại thẻ sinh viên")
            # Tạo một đối tượng write_file
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_the_sv: '+user_input)
        return []


class ActionChatGPTFallback(Action):
    def name(self) -> str:
        return "action_chatgpt_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_message = tracker.latest_message.get('text')

        print("user_ask: "+user_message)
        # logging.info("{}{}".format('Call action_fall_back: ', user_message))
        try:
            response = requests.post(
                'https://api.openai.com/v1/engines/davinci-codex/completions',
                headers={
                    'Authorization': f'Bearer YOUR_OPENAI_API_KEY',
                    'Content-Type': 'application/json'
                },
                json={
                    'prompt': user_message,
                    'max_tokens': 150
                }
            )
            response_data = response.json()

            if 'choices' in response_data and len(response_data['choices']) > 0:
                chatgpt_reply = response_data['choices'][0]['text'].strip()
            else:
                chatgpt_reply = "Xin lỗi tôi chưa hiểu ý bạn, bạn vui lòng mô tả chi tiết hơn được không hoặc bạn có thể bấm vào chat Admin để được tư vấn"

        except Exception as e:
            chatgpt_reply = f"action fallback: Đã xảy ra lỗi: {str(e)}"
        
        dispatcher.utter_message(text=chatgpt_reply)
        
        # Ngăn vòng lặp bằng cách hoàn nguyên trạng thái người dùng
        return [UserUtteranceReverted()]


# class acction_tuyen_sinh(Action):
#     def name(self):
#         return "action_tuyen_sinh"
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         return []
    
##################################################

# class ActionSayData(Action):

#     def name(self) -> Text:
#         return "action_say_data"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         email = tracker.("email")
#         phone = tracker.get_slot("phone")
#         logging.info("{}{}".format('Call action_say_data: '))

#         dispatcher.utter_message(text=f"Email bạn cung cấp là: {email},số điện thoại là: {phone}")

#         return []
    


# class ValidateSimpleForm(FormValidationAction):

#     def name(self) -> Text:
#         return "validate_simple_form"

#     def validate_phone(
#         self,
#         value: Text,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         if len(value) == 10 and value.isdigit():
#             # Trả về số điện thoại hợp lệ
#             return {"phone": value}
#         else:
#             # Trả về None nếu số điện thoại không hợp lệ
#             dispatcher.utter_message(text="Số điện thoại không hợp lệ")
#             return {"phone": None}

#     def validate_email(
#         self,
#         value: Text,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#         if re.match(email_regex, value):
#             # Trả về email hợp lệ
#             return {"email": value}
#         else:
#             # Trả về None nếu email không hợp lệ
#             dispatcher.utter_message(text="Email không hợp lệ!")
#             return {"email": None}


# """   PHUONG  """

# class actionDangKyGiayXacNhan(actionDangKyGiayXacNhan):
#     pass
