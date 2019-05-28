# coding=utf-8
import requests
from lxml import etree
import json


class Chapter_spider():
    def __init__(self):
        self.start_url = "https://h5.17k.com/chapter/2849619/35312236.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36",
            "Host": "h5.17k.com",
            "Cookie": "BAIDU_SSP_lcr=https://www.baidu.com/link?url=M6ENl3PnnqO66L8PRqJAiJlhsqIqzkSGrv__dYqEd-y&wd=&eqid=99d9e3e600057f2e000000065cec8e5e; Hm_lvt_9793f42b498361373512340937deb2a0=1559006816; sajssdk_2015_cross_new_user=1; UM_distinctid=16afc0c29756bf-09fcd7753b2e2a-3e7e045d-1fa400-16afc0c2976521; acw_tc=b65cfd2215590068498865234e79a4ac9f9b0d777448c3548bf58365dca62c; GUID=4291a5b6-5d9a-5c4c-2966-bf7ed0fe2323; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%224291a5b6-5d9a-5c4c-2966-bf7ed0fe2323%22%2C%22%24device_id%22%3A%2216afc0c288f4a-0d4e6d66c97773-3e7e045d-2073600-16afc0c28907ed%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1559017565; Hm_lvt_b33ccadfca0f88b71e592ec2bf9d3497=1559017851; Hm_lpvt_b33ccadfca0f88b71e592ec2bf9d3497=1559017851; CNZZDATA1257018823=705428450-1559012875-https%253A%252F%252Fwww.17k.com%252F%7C1559012875",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
        }

    def parse_url(self,url):
        # 获取请求
        response = requests.get(url,headers=self.headers)
        return response.content.decode('utf-8')

    def get_content_list(self,html_str):
        # 提取数据
        html = etree.HTML(html_str)
        div_list = html.xpath('//*[@id="Context"]')
        content_list = []
        # print(div_list)
        for div in div_list:
            item = {}
            item['title'] = div.xpath("./h1/text()")[0]
            item['text'] = div.xpath("./article/p/text()")[0] if len(div.xpath("./article/p/text()"))>0 else None
            content_list.append(item)
        next_url = html.xpath("//*[@id='BottomTask']/div[2]/a[text()='下一章']/@href")[0] if len(html.xpath("//*[@id='BottomTask']/div[2]/a[text()='下一章']/@href"))>0 else ""
        next_urls = "https://www.h5.17k.com"+next_url
        return content_list,next_urls

    def save_content_list(self,content_list,html_str):
        file_name = "归一.text"
        with open(file_name,'a') as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent=2))
                f.write("\n")



    def run(self):
    # 实现主要逻辑
        next_urls = self.start_url
        while next_urls != "https://www.h5.17k.com":
            # 1. start_url
            # 2. 发送请求，获取响应
            html_str = self.parse_url(next_urls)
            # 3. 提取数据
                # 3.2 请求下一章的url地址
                # 3.3 提取下一张数据
                # 3.4 请求下一章的地址，提取数据进入循环
            content_list,next_urls = self.get_content_list(html_str)

            # 4. 保存
            self.get_content_list(content_list)
            # 5. 进入循环


if __name__ == "__main__":
    text_file = Chapter_spider()
    text_file.run()
# text = Chapter_spider()
# text.get_content_list()
