# coding:utf-8
import sys
import os
import requests

reload(sys)
sys.setdefaultencoding("utf-8")

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url = 'https://pypi.python.org/packages/c2/41/d41fe95e916b797d3bb697ca74877f6b852d68d481635d890fadec1af553/cdrouter-0.0.7.tar.gz#md5=141652e754b1a59a501116cd506448c9'  ##开始的URL地址

try:
    start_html = requests.get(all_url,
                          headers=headers,
                          timeout=1)  ##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释

    path = './aaa/bbb/ccc/'
    name = u'测试.tar.gz'
    if not os.path.exists(path):
        os.makedirs(path)

    with open(path + name, "wb") as code:
        code.write(start_html.content)
        code.close()

except requests.exceptions.ReadTimeout, msg:
    print msg
except requests.exceptions.ConnectionError, msg:
    print msg


print 'finished....'

