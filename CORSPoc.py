#-*- coding:utf-8 -*-

"""CORS跨域漏洞检测.
Usage:
  CORSPoc.py [-u <url> | -l <file>] [--cookies=<cookies>] [--date=<date>]
  CORSPoc.py (-h | --help)

Options:
  -h --help              显示帮助
  -u <url>               添加url 
  -l <file>              添加file
  --cookies=<cookies>    添加cookies
  --date=<date>          post数据包

Example:
  CORSPoc.py -u "https://www.baidu.com"
  CORSPoc.py -l domain.txt
"""

import requests
from prettytable import PrettyTable
from docopt import docopt

print('''
 ----
    __________  ____  _____ ____            
  / ____/ __ \/ __ \/ ___// __ \____  _____
 / /   / / / / /_/ /\__ \/ /_/ / __ \/ ___/
/ /___/ /_/ / _, _/___/ / ____/ /_/ / /__  
\____/\____/_/ |_|/____/_/    \____/\___/  
                                           
 ----
\                             .       .
 \                           / `.   .' " 
  \                  .---.  <    > <    >  .---.
   \                 |    \  \ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \~~~\.'                    `./~~~/
       ---------   \__/                        \__/
      .'  O    \     /               /       \  " 
     (_____,    `._.'               |         }  \/~~~/
      `----.          /       }     |        /    \__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'   
                     |     /        |     /     ~-.     `-. _  _  _
                     |_____|        |_____|         ~ - . _ _ _ _ _>
 
''')

def file_filter(url,file,cookies,date):
    url = url
    file = file 
    cookies = cookies
    date = date
    x = PrettyTable(["测试url", "测试结果"])
    x.align["测试url"] = "l"
    x.padding_width = 10
    if file == None:
        try:
            print("开始请求"+url)
            result = cors_check(url,cookies,date)
            x.add_row([url,result])
            print(x)
        except:
            print("url请求错误，请手动测试")
    else:
        f = open(file,'r')
        line = f.readline()
        while line:
            print("开始请求："+line)
            if line:
                try:
                    result = cors_check(line.strip(),cookies,date)
                    x.add_row([line,result])
                except:
                    print("url请求错误，请手动测试") 
            line = f.readline()
        f.close()
        print(x)


def cors_check(url,cookies,date):
    cookies = cookies
    date = date
    headers={
	      'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2767.400',
        'Origin':'www.corspoc.com',
        'Cookie':cookies
    }
    url = url
    if 'http' in url:
        url = url
    else:
        url = 'https://'+url

    if date == None:
        rep = requests.get(url=url,headers=headers)
    else:
        rep = requests.post(url=url,headers=headers,date=date)
    rep_headers = rep.headers

    if rep_headers.get("access-control-allow-origin") == "www.corspoc.com":
        if resp_headers.get("access-control-allow-credentials") == "true":
            return '存在CORS跨域漏洞'
        return '不存在CORS跨域漏洞'
    return '不存在CORS跨域漏洞'
    


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    url = arguments['-u']
    file = arguments['-l']
    cookies = arguments['--cookies']
    date = arguments['--date']
    file_filter(url,file,cookies,date)