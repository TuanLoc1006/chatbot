NGANH = [
    'y khoa',
    'răng hàm mặt',
    'dược học',
    'y học cổ truyền',
    'y học dự phòng',
    'điều dưỡng',
    'kỹ thuật xét nghiệm y học',
    'hộ sinh',
    'kỹ thuật hình ảnh y học',
    'y tế công cộng'
]

CTDT = {
    'y khoa': 'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/9079_Nganh-Y-khoa.pdf',
    'răng hàm mặt': 'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/9220_2019.-BAN-MO-TA-CTDT-RHM.pdf',
    'dược học':'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/5478_3625_CTDT-tin-chi-Duoc-24-11-17.pdf',
    'y học cổ truyển':'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/8831_Ban-mo-ta-CTDT-YHCT2019.pdf',
    'y học dự phòng':'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/8819_CTDT-tin-chi-YHDP-2013.pdf',
    'điều dưỡng':'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/3618_1.-DDDK-VLVH-24-11-17.pdf',
    'kỹ thuật xét nghiệm y học':'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/9218_Mota_CTDT_XN-2019.pdf',
    'hộ sinh':'Chưa cập nhật',
    'kỹ thuật hình ảnh y học':'Chưa cập nhật',
    'y tế công cộng':'http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/8801_CTDT-tin-chi-YTCC-2013.pdf'
}

hocphi1nam = {
    'Y khoa': '44.100.000',
    'Răng hàm mặt': '44.100.000',
    'Dược học':'44.100.000',
    'Y học cổ truyền': '39.200.000',
    'Y học dự phòng': '39.200.000',    
    'Điều dưỡng': '39.200.000',    
    'Kỹ thuật xét nghiệm y học': '39.200.000',    
    'Hộ sinh': '20.400.000',
    'Kỹ thuật hình ảnh y học': '20.400.000',
    'Y tế công cộng': '20.400.000'
}



class Constant:
    def __init__(self):
        pass
    def get_nganh_hoc(self):
        return NGANH
    def get_hoc_phi(self):
        return hocphi1nam
    def getCTDT(self):
        return CTDT