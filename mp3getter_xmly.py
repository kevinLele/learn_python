# coding:utf-8

import time
import re
import sys
import os
import requests
from bs4 import BeautifulSoup
import json
import sqlite3

'''
用于从喜马拉雅抓取儿童成语故事m4a文件
'''

reload(sys)
sys.setdefaultencoding("utf-8")
time.sleep(1)

main_url = 'http://www.ximalaya.com/29553933/album/2811947'  # 喜马拉雅内容地址
#main_url = 'http://www.ximalaya.com/3999963/album/235740'


# <-------------------- Configs ---------------------
downloadPath = "./download/"
PrintLog = False
index = 1
TIMEOUT = 30  # requests 超时时间，单位：秒

# #浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
headers = {
    'User-Agent':
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

# --------------------- Configs -------------------->


# <-------------------- Functions ---------------------

# 创建目录，如果目录已存在则不做任何事情
def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


# 根据文件名称获取文件的扩展名，如果文件没有扩展名则返回空字符串
def get_expanded_name(file_name):
    m = re.match(r'.*\.([^/]*)$', file_name)
    expanded_name = ''

    if m:
        expanded_name = '.' + m.group(1)

    return expanded_name


# 根据全局配置来打印信息
def log(log_info, log_flag=False):
    if PrintLog or log_flag:
        print log_info


# 从指定的url下载文件并保存到本地
def download_file_form_url(sound_id, url, file_path):

    try:
        sound_html = requests.get(url, headers=headers, timeout=TIMEOUT)

        # 已存在的文件不再进行下载
        if os.path.exists(file_path):
            return

        # 下载到本地
        with open(file_path, "wb") as downloadFile:
            downloadFile.write(sound_html.content)
            downloadFile.close()

        # 在数据库中将已下载的文件标识为已下载
        update_db(sound_id)

    except requests.exceptions.ReadTimeout, msg:
        print msg
    except requests.exceptions.ConnectionError, msg:
        print msg


def save_db(sn, sound_id, sound_name, sound_path):
    con = sqlite3.connect("./test.db")
    cu = con.cursor()

    try:
        cu.execute("insert into story (sn,id,name,path) values (?,?,?,?)", (sn, sound_id, sound_name, sound_path))
        con.commit()
    finally:
        cu.close()
        con.close()


def update_db(sound_id):
    con = sqlite3.connect("./test.db")
    cu = con.cursor()

    try:
        cu.execute("update story set is_download=1 where id=?", (sound_id,))
        con.commit()
    finally:
        cu.close()
        con.close()


# 解析一个页面的信息
def process_one_page(page_url):
    global index
    log('pagingUrl: ' + page_url)

    page_html = requests.get(page_url, headers=headers, timeout=TIMEOUT)
    sound_list_div = BeautifulSoup(page_html.text).findAll(attrs={'class': 'album_soundlist'})
    sound_list = sound_list_div[0].ul.findAll('li')

    for soundLi in sound_list:
        sound_id = soundLi.attrs['sound_id']
        sound_name = soundLi.find('a', {'class': 'title'}).attrs['title']

        json_url = 'http://www.ximalaya.com/tracks/' + sound_id + '.json'
        log('json_url: ' + json_url)
        json_html = requests.get(json_url, headers=headers, timeout=TIMEOUT)
        log(json_html.text)
        json_result = json.loads(json_html.text)
        sound_path = json_result['play_path']
        expanded_name = get_expanded_name(sound_path)

        log('%d %s %s %s' % (index, sound_id, sound_name, sound_path), True)
        save_db(index, sound_id, sound_name, sound_path)
        index += 1

        download_file_form_url(sound_id, sound_path, downloadPath + sound_name + expanded_name)
# ----------------------Functions -------------------->


start_html = requests.get(main_url, headers=headers, timeout=TIMEOUT)
soup = BeautifulSoup(start_html.text)

create_dir(downloadPath)
pagingBar_wrapper = soup.find('div', {'class': 'pagingBar_wrapper'})

# 检查是否有分页标签栏
if pagingBar_wrapper is not None:
    paging_btns = pagingBar_wrapper.findAll('a')

    for btn in paging_btns:
        if btn.text.encode("utf-8").isdigit():
            pagingUrl = main_url + "?page=" + btn.text
            process_one_page(pagingUrl)
else:
    process_one_page(main_url)
