# coding:utf-8

import requests
import os


# #浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
HEADERS = {
    'User-Agent':
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

# requests 超时时间，单位：秒
TIMEOUT = 10


def get_page_html(page_url):
    page_html = requests.get(page_url, headers=HEADERS, timeout=TIMEOUT)
    return page_html


def download_file_form_url(url, file_path):

    # 已存在的文件不再进行下载
    if os.path.exists(file_path):
        print u"该文件已存在，file_path: " + file_path
        return

    download_html = get_page_html(url)

    # 下载到本地
    with open(file_path, "wb") as downloadFile:
        downloadFile.write(download_html.content)
        downloadFile.close()

