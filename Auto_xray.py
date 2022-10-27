# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     xray
   Author :       chenci
   date：          2022/10/24
-------------------------------------------------
"""
import os
import re
import sys
import threading
import argparse
import queue
import time
from my_email import send_mail
from time import strftime
from time import gmtime
import fofa


def cmd(target_url):
    save_name = target_url.replace('/', '').replace(':', '')  # 去掉特殊字符,windows的文件名问题
    shell = f'{args.xray} webscan --basic-crawler {target_url} --html-output {args.outpath}/{save_name}.html'
    os.system(shell)
    # print(shell)
    return


# 调用xray扫描
def xray_scan(url_queue):
    # 判断队列是否为空,空结束,不为空继续
    while not url_queue.empty():
        url_line = url_queue.get()  # 获取队列
        # 正则匹配是否为http:// or https://开头
        pattern = re.compile(r'[a-zA-z]+://')
        try:
            if not pattern.match(url_line.strip()):
                target_url = 'http://' + url_line.strip()
            else:
                target_url = url_line.strip()
            print('正在扫描:', target_url)
            # 将url带入扫描
            cmd(target_url)
        except Exception as e:
            print(e)
    else:
        print(f'扫描结束!')
        sys.exit()


# 构造线程池
def thread_pool(url_queue):
    threads_list = []
    # 5.将扫描队列加入线程池, 调用xray_scan函数开始扫描
    for i in range(int(args.threads)):
        t = threading.Thread(target=xray_scan, args=(url_queue,))
        threads_list.append(t)
        t.start()
    for t in threads_list:
        t.join()


# 逐行读取urls.txt,并写队列
def read_url(filename):
    url_queue = queue.Queue()
    with open(filename, 'r') as f:
        urls = f.readlines()
        for i in urls:
            url = i.strip()  # 去空格
            url_queue.put(url)
        return url_queue  # 返回队列


# 入口函数
def main():
    # 创建输出目录
    create_dir_not_exist(args.outpath)
    # 3.调用read_url函数返回扫描url队列
    url_queue = read_url(args.filename)

    # 4.调用进程池,给入url队列
    thread_pool(url_queue)


# 判断输出文件夹是否存在
def create_dir_not_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)


if __name__ == "__main__":
    # 启动时间
    start_time = time.time()
    # 1.自定义参数
    parser = argparse.ArgumentParser(description='多线程批量xray扫描小脚本 by chenci')
    parser.add_argument('--xray', '-x', help='指定xray路径;非必选,默认为./xray_darwin_amd64', default='./xray_darwin_amd64')
    parser.add_argument('--threads', '-t', help='指定线程数;非必选,默认值为10线程', default=10)
    parser.add_argument('--filename', '-f', help='指定扫描url列表文件路径;非必选,默认为./urls.txt', default='./urls.txt')
    parser.add_argument('--outpath', '-o', help='指定输出路径;非必选,默认为./out', default='./out')
    parser.add_argument('--email', '-e', help='开启邮件推送 -e True;非必选,默认关闭,需填写my_email.py中的配置参数', default=False)
    parser.add_argument('--fofa', '-ff', help='启用fofa批量收集域名 -ff True;非必选,默认关闭,需填写fofa.py中的配置参数', default=False)
    args = parser.parse_args()

    # 2.判断启动功能
    try:
        # 判断是否调用fofa域名收集
        if args.fofa:
            fofa.do_fofa(args.filename)
            main()
        else:
            main()
        # 判断是否调用邮件提醒
        if args.email:
            end_time = time.time() - start_time
            run_time = strftime("%H:%M:%S", gmtime(end_time))
            send_mail(run_time)
    except Exception as e:
        print(e)
