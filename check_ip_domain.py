# coding:utf-8

import requests
import sys
from lxml import etree
import re


def view():
    print("""
python3 check_ip_domain.py 8.8.8.8
python3 check_ip_domain.py google.com

========================================================================
""")


def ip():
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (XHTML, like Gecko) '
                      'Chrome/84.0.4147.135 Safari/537.36 '
    }
    try:
        requ = requests.get(url='https://m.ip138.com/iplookup.asp?ip=' + sys.argv[1], headers=ua)
        requ = requ.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(requ.text)[0])
        content1 = re.findall(r'<caption><h1>(.*?)</h1></caption>',requ)
        content2 = re.findall(r'</td><td>(.*?)</td></tr></tbody>',requ)
        print(content1[0])
        print("ASN归属地 :",content2[0])
    except:
        print('特殊IP!')


def domain():
    test = requests.post(url='https://ip.chinaz.com/' + sys.argv[1], data={'ip': sys.argv[1]})
    cookie1 = re.findall(r'cookie="(.*?);', test.text)
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (XHTML, like Gecko) '
                      'Chrome/84.0.4147.135 Safari/537.36',
        'Cookie': cookie1[0]
    }
    requ = requests.post(url='https://ip.chinaz.com/' + sys.argv[1], data={'ip': sys.argv[1]}, headers=ua)
    xpath = etree.HTML(requ.text)
    ip = xpath.xpath('//*[@id="leftinfo"]/div[3]/div[2]/div[2]/span[2]/text()')
    address = xpath.xpath('//*[@id="leftinfo"]/div[3]/div[2]/div[2]/span[4]/p/text()')
    domain = xpath.xpath('//*[@id="leftinfo"]/div[3]/div[2]/div[2]/span[1]/text()')

    shield = xpath.xpath('//*[@id="leftinfo"]/div[2]/form/div[2]/text()')
    if len(shield) == 1:
        print(shield[0])
    else:
        print('域名: ' + domain[0])
        print('IP: ' + ip[0])
        print('物理地址: ' + address[0])


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        view()
    else:
        view()
        input1 = re.findall(
            r'^(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|['
            r'1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2['
            r'0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])$',
            sys.argv[1])
        if len(input1) > 0:
            ip()
        else:
            domain()
