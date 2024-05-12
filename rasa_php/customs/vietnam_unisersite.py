


# import requests
# import json
# from lxml import etree


# class DemoSpider(object):
#     def __init__(self):
#         self.resp = None
#         self.result = None

#     def crawl(self, off_number=None):
#         url = "https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_tr%C6%B0%E1%BB%9Dng_%C4%91%E1%BA%A1i_h%E1%BB%8Dc,_h%E1%BB%8Dc_vi%E1%BB%87n_v%C3%A0_cao_%C4%91%E1%BA%B3ng_t%E1%BA%A1i_Vi%E1%BB%87t_Nam#"
#         # url = "https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_tr%C6%B0%E1%BB%9Dng_%C4%91%E1%BA%A1i_h%Epy 1%BB%8Dc,_h%E1%BB%8Dc_vi%E1%BB%87n_v%C3%A0_cao_%C4%91%E1%BA%B3ng_t%E1%BA%A1i_Vi%E1%BB%87t_Nam"
#         payload = ""

#         headers = {
#             'cache-control': "no-cache",
#             'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#         }
#         response = requests.request("GET", url, data=payload, headers=headers)
#         # response = requests.request("POST", url, data=payload, headers=headers)
#         self.resp = response.text

#     def parser(self):
#         response = etree.HTML(self.resp)
#         name = response.xpath('//*[@id="mw-content-text"]//ol/li/a/text()')
#         self.result = list(set(name))
#         print(self.result)
#         print(len(self.result))

#     def save(self):
#         with open(r'C:\xampp\htdocs\rasa_chatbot\rasa_php\customs\university_name.txt', 'a', encoding='utf-8')as f:
#             f.write('\n'.join(self.result))
#             pass
#     def run(self):
#         self.crawl()
#         self.parser()
#         self.save()


# if __name__ == '__main__':
#     demo = DemoSpider()
#     demo.run()

import requests
from bs4 import BeautifulSoup

def get_wiki_data(url):
    # Gửi yêu cầu GET đến URL của trang wiki
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không (status code 200 là thành công)
    if response.status_code == 200:
        # Sử dụng BeautifulSoup để phân tích HTML từ phản hồi
        soup = BeautifulSoup(response.content, 'html.parser')

        # Tìm và lấy phần dữ liệu bạn quan tâm từ trang wiki
        # Ví dụ: lấy tiêu đề của trang
        title = soup.find('h1', id='firstHeading').text

        # Ví dụ khác: lấy nội dung của một phần tử có class cụ thể
        content = soup.find('div', class_='mw-parser-output').text

        # Trả về dữ liệu bạn đã lấy được
        return title, content
    else:
        # Trả về None nếu yêu cầu không thành công
        return None, None

def write_to_txt(title, content):
    # Mở hoặc tạo một file .txt để ghi dữ liệu
    with open('C:\xampp\htdocs\rasa_chatbot\rasa_php\customs\wiki_data.txt', 'w', encoding='utf-8') as file:
        # Ghi tiêu đề vào file
        file.write("Tiêu đề: {}\n\n".format(title))
        # Ghi nội dung vào file
        file.write(content)

# URL của trang wiki bạn muốn lấy dữ liệu
wiki_url = 'https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_tr%C6%B0%E1%BB%9Dng_%C4%91%E1%BA%A1i_h%E1%BB%8Dc,_h%E1%BB%8Dc_vi%E1%BB%87n_v%C3%A0_cao_%C4%91%E1%BA%B3ng_t%E1%BA%A1i_Vi%E1%BB%87t_Nam'

# Gọi hàm để lấy dữ liệu từ trang wiki
title, content = get_wiki_data(wiki_url)

# Nếu lấy được dữ liệu, ghi vào file .txt
if title and content:
    write_to_txt(title, content)
    print("Dữ liệu đã được ghi vào file wiki_data.txt.")
else:
    print("Không thể lấy dữ liệu từ trang wiki.")
