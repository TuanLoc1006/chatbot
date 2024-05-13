


import requests
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = None

    def crawl(self, off_number=None):
        url = "https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_tr%C6%B0%E1%BB%9Dng_%C4%91%E1%BA%A1i_h%E1%BB%8Dc,_h%E1%BB%8Dc_vi%E1%BB%87n_v%C3%A0_cao_%C4%91%E1%BA%B3ng_t%E1%BA%A1i_Vi%E1%BB%87t_Nam"
        payload = ""

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        # response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        response = etree.HTML(self.resp)
        name = response.xpath('//*[@id="mw-content-text"]//ol/li/a/text()')
        self.result = list(set(name))
        print(self.result)
        print(len(self.result))

    def save(self):
        with open(r'C:\xampp\htdocs\rasa_chatbot\rasa_php\customs\university_vietnam\university_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(self.result))
            pass
    def run(self):
        self.crawl()
        self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()