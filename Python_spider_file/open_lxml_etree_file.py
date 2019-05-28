# coding=utf-8
from lxml import etree

# parser = etree.HTMLParser(encoding='utf-8')
# html = etree

def html_Text():
    parser = etree.HTMLParser(encoding='utf-8')
    html_file_text = etree.HTML('../Html_File/17K_network.html',parser=parser)
    print(etree.tostring(html_file_text,encoding='utf-8').decode('utf-8'))

def parse_file():
    parser = etree.HTMLParser(encoding='utf-8')
    html_file_parse = etree.parse('../Html_File/17K_network.html',parser=parser)
    print(etree.tostring(html_file_parse,encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    html_Text()
    # parse_file()