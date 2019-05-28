# coding=utf-8
import requests
import threading
from queue import Queue
from lxml import etree

# url = 'https://www.17k.com/list/2849619.html'
# url_file = 'https://www.17k.com'
#
# headers = {
#     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
#     "cookie": "sajssdk_2015_cross_new_user=1; UM_distinctid=16af9b93b1c5b1-074f87c4354d95-3e7e045d-1fa400-16af9b93b1d84e; CNZZDATA5647345=cnzz_eid%3D249746133-1558964850-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1558964850; Hm_lvt_9793f42b498361373512340937deb2a0=1558967827; GUID=34126f39-a4e2-b9f3-0cc0-ec80a52ffc88; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2234126f39-a4e2-b9f3-0cc0-ec80a52ffc88%22%2C%22%24device_id%22%3A%2216af9b93a45789-0bcab30d9ce8b5-3e7e045d-2073600-16af9b93a46d2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1558969370"
# }
#
# # response = requests.get(url,headers=headers)
# # response_file = response.content.decode('utf-8')
# #
# # parser = etree.HTMLParser(encoding='utf-8')
# # chapter_file = etree.HTML(response_file,parser=parser)
# # chapter_file_text = etree.tostring(chapter_file,encoding='utf-8').decode('utf-8')
# # # print(chapter_file_text)
# # href_list = chapter_file_text.xpath("//html/body/div[6]/dl[2]/dd/a")
# # print(href_list)

url = ""

