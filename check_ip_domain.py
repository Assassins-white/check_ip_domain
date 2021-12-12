# coding:utf-8
import requests
import sys
import re
from colorama import init,Fore

ua = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (XHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}

def main(website):
	init(autoreset=True)
	url = f"https://ip.bmcx.com/{website}__ip/"
	requ = requests.get(url=url,headers=ua)
	ip = re.findall(r'<td height="25" bgcolor="#FFFFFF" style="text-align: center">(.*?)</td>',requ.text)
	address = re.findall(r'<td bgcolor="#FFFFFF" style="text-align: center">(.*?)</td>',requ.text)
	print("\n    "+'IP: ' , Fore.GREEN + ip[0])
	print("    "+'物理地址: ' , Fore.RED + address[0])


def view():
    print("""
    python3 check_ip_domain.py 8.8.8.8
    python3 check_ip_domain.py google.com
""")


if __name__ == '__main__':
	if (len(sys.argv) == 2):
		main(sys.argv[1])
	else:
		view()