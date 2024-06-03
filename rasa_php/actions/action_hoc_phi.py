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
# phuong

handledb = handleDB()
get_connect = handledb.get_connect()
get_nganh = handledb.get_nganh()



class actionHocPhi(Action):
    def name(self):
        return "action_hoc_phi"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hocphi_entity = next(tracker.get_latest_entity_values('hocphi'), None)
        nam_entity = next(tracker.get_latest_entity_values('year'), None)
        loai_hinh_dt_entity = next(tracker.get_latest_entity_values('loai_hinh_dt'), None)
        user_input = tracker.latest_message['text']
        
        logging.info(f"Call action_hoc_phi: {hocphi_entity}")
        logging.info(f"Call action_hoc_phi_nam: {nam_entity}")
        logging.info(f"Call action_hoc_phi_loai_hinh_dt: {loai_hinh_dt_entity}")
        
        current_year = datetime.now().year
        nam_yeu_cau = {
            "hiện tại": current_year,
            "bây giờ": current_year,
            "năm hiện tại": current_year,
            "1": current_year,
            "năm nay": current_year,
            "năm rồi": current_year - 1,
            "năm trước": current_year - 1,
        }
        
        hinh_thuc_dt = {
            "liên thông": "liên thông",
            "liên thông đại học": "liên thông",
            "liên thông cao đẳng": "liên thông",
            "làm bằng liên thông": "liên thông",
            "sau đại học": "sau đại học",
            "sau đại": "sau đại học",
            "sau đại học thạc sĩ": "sau đại học",
            "sau đại học tiến sĩ": "sau đại học",
            # Các biến thể khác của liên thông và sau đại học có thể được thêm vào đây
        }
        
        if hocphi_entity:
            if nam_entity :
                nam = nam_entity
            else:
                nam = current_year
            loai_hinh_dt = hinh_thuc_dt.get(loai_hinh_dt_entity.lower(), 'đại học') if loai_hinh_dt_entity else 'đại học'
            
            handledb_instance = handleDB()
            hoc_phi_database = handledb_instance.get_hoc_phi(nam, loai_hinh_dt)

            if hoc_phi_database:
                if loai_hinh_dt == "liên thông":
                    message = f"Mức học phí trình độ liên thông năm {nam} của các ngành học là:<br/>"
                elif loai_hinh_dt == "sau đại học":
                    message = f"Mức học phí trình độ sau đại học năm {nam} của các ngành học là:<br/>"
                else:
                    message = f"Mức học phí trình độ đại học năm {nam} của các ngành học là:<br/>"
                    # print(loai_hinh_dt+"  "+str(nam))
                message += "<br/>".join([f"{value[0]}: {value[1]} VND" for value in hoc_phi_database])
                dispatcher.utter_message(text=message)
            else:
                dispatcher.utter_message(text="Không tìm thấy thông tin học phí cho năm và loại hình đào tạo được yêu cầu.")
        else:
            # Ghi log lại câu hỏi của người dùng nếu không có entity 'hocphi'
            file_writer = write_file()
            file_writer.get_ghi_log_file(f'Action học phí: {user_input}')


        return []
    


class actionHocPhiCoTangKhong(Action):
    def name(self):
        return "action_hoc_phi_co_tang_khong"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # hocphi_entity = next(tracker.get_latest_entity_values('hocphi'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi học phí có tăng không: " + user_input)
        # logging.info("{}{}".format('Call action_hoc_phi: ', hocphi_entity))
        # if hocphi_entity:
            # hoc_phi_database = get_hoc_phi
        dispatcher.utter_message(text="Có tăng theo từng năm nha bạn ơi")
        
        return []
    



class actionCacPhuongThucThanhToan(Action):
    def name(self):
        return "action_phuong_thuc_thanh_toan"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # hocphi_entity = next(tracker.get_latest_entity_values('hocphi'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi thanh toán học phí: " + user_input)
        # logging.info("{}{}".format('Call action_hoc_phi: ', hocphi_entity))
        # if hocphi_entity:
            # hoc_phi_database = get_hoc_phi
        dispatcher.utter_message(text="Trực tiếp, Chuyển khoản: http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/11652_huong-dan-nop-hp-Online.pdf ")
        return []



class actionHoTroVayTienHoc(Action):
    def name(self):
        return "action_ho_tro_vay_tien_hoc"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # hocphi_entity = next(tracker.get_latest_entity_values('hocphi'), None)
        user_input = tracker.latest_message['text']
        print("người dùng hỏi thanh toán học phí: " + user_input)
        # logging.info("{}{}".format('Call action_hoc_phi: ', hocphi_entity))
        # if hocphi_entity:
            # hoc_phi_database = get_hoc_phi
        dispatcher.utter_message(text="Theo Điều 2 Quyết định 157/2007/QĐ-TTg và khoản 1 Điều 1 Quyết định 05/2022/QĐ-TTg</br>- Sinh viên mồ côi cả cha lẫn mẹ hoặc chỉ mồ côi cha hoặc mẹ nhưng người còn lại không có khả năng lao động.</br>- Sinh viên là thành viên của hộ gia đình thuộc một trong các đối tượng:</br>+ Hộ nghèo theo chuẩn quy định của pháp luật.</br>+ Hộ cận nghèo theo chuẩn quy định của pháp luật.</br>+ Hộ có mức sống trung bình theo chuẩn quy định của pháp luật.</br>- Sinh viên mà gia đình gặp khó khăn về tài chính do tai nạn, bệnh tật, thiên tai, hỏa hoạn, dịch bệnh trong thời gian theo học có xác nhận của Ủy ban nhân dân xã, phường, thị trấn nơi cư trú.")
        return []


    
