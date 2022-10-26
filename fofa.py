# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fofa
   Author :       chenci
   date：          2022/10/26
-------------------------------------------------
"""

import requests
import base64
import os


# 判断写入文件是否为空,不为空清空
def get_sizes(filename_path):
    if os.path.getsize(filename_path):
        with open(filename_path, 'a+') as f:
            f.truncate(0)


# 调用fofa api抓取数据
def do_fofa(filename_path):
    resp = requests.get(get_url)
    results = resp.json()['results']
    get_sizes(filename_path)
    for url in results:
        url = url
        with open(f'{filename_path}', 'a+') as f:
            f.write(url)
            f.write('\n')
    print('fofa:数据已抓取完成~开始扫描!')


# 配置参数
fofa_email = ''  # fofa email
fofa_key = ''  # fofa key
fields = 'host'  # 可选字段，默认host,ip,port，详见附录1
query = '''region="TW" && host=".edu.tw" && status_code="200"'''  # 输入的查询语法
size = 100  # 每页查询数量，默认为100条，最大支持10,000条/页
page = 1  # 是否翻页，默认为第一页，按照更新时间排序

qbase64 = str(base64.b64encode(query.encode('utf-8')), 'utf-8')  # base64编码搜索语法
get_url = f"https://fofa.info/api/v1/search/all?email={fofa_email}&key={fofa_key}&fields={fields}&size={size}&page={page}&qbase64={qbase64}"

if __name__ == '__main__':
    do_fofa()
