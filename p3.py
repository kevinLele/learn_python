# coding:utf-8
import time
import re
import sys
import requests  ## 导入requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, "lxml")
print soup.prettify()  # 格式化输出

print '-----------------------------------'
print soup.title
print '-----------------------------------'
print soup.head
print '-----------------------------------'
print soup.a
print '-----------------------------------'
print soup.p
print '-----------------------------------'

print type(soup.title)  # 查看title的类型

print soup.p.attrs
print soup.p.string

print '************************************************************************'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url = 'http://www.ximalaya.com/29553933/album/2811947'  ##开始的URL地址
start_html = requests.get(all_url,
                          headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释

f = open('./test.txt', 'wt+')
f.write(start_html.text)
f.close()

# print(start_html.text)  ##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)
soup = BeautifulSoup(start_html.text)
soundListDiv = soup.findAll(attrs={'class': 'album_soundlist'})
soundList = soundListDiv[0].ul.findAll('li')

for soundLi in soundList:
    soundId = soundLi.attrs['sound_id']
    soundName = soundLi.find('a', {'class': 'title'}).attrs['title']
    print '%s %s' % (soundId, soundName)


# print soup.prettify()
