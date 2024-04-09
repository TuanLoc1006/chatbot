
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ExtractOfficeEntity(Action):

    def name(self) -> Text:
        return "action_extract_office_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        vanPhongKhoa = next(tracker.get_latest_entity_values('văn phòng khoa'), None)
        if vanPhongKhoa:
            dispatcher.utter_message(text=f"Đây là thông tin khoa {vanPhongKhoa} bạn đã yêu cầu")
        else:
            dispatcher.utter_message(text="Xin lỗi, tôi không tìm thấy thông tin khoa bạn yêu cầu")
        return []

class OrderOfficeAction(Action):
    def name(self) -> Text:
        return "action_order_office"
     
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dhyd =  next(tracker.get_latest_entity_values('ctump'), None)
        if dhyd:
            dispatcher.utter_message(text="Đại học y dược có các Khoa\n- Y\n- Khoa Răng Hàm Mặt\n- Khoa Dược\n- Khoa Điều dưỡng\n- Kỹ thuật y học\n- Khoa Y tế công cộng\n- Khoa Khoa học cơ bản\n- Khoa Y học cổ truyền\nBạn muốn tìm kiếm thông tin của khoa nào?")
        else:
            dispatcher.utter_message(text="Xin lỗi tôi chỉ cung cấp thông tin về Đại học Y Dược Cần Thơ (ctump)")   
        return []
    
class ConfirmOrderAction(Action):
    def name(self) -> Text:
        return "action_confirm_order"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        vanPhongKhoa = next(tracker.get_latest_entity_values('văn phòng khoa'), None)
        if vanPhongKhoa:
            dispatcher.utter_message(text=f"Đây là thông tin về khoa {vanPhongKhoa} bạn cần")
        else:
            dispatcher.utter_message(text="Xin lỗi, tôi không tìm thấy thông tin khoa bạn cần")
        return []
    