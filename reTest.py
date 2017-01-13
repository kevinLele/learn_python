# coding:utf-8
import sys
import re


reload(sys)
sys.setdefaultencoding("utf-8")

# 定义一个函数
def testfunction(aaa):
    print aaa

# match是必须从头匹配的，加不加^标识都一样
m = re.match(r'.*\.([^/]*)$', 'http://audio.xmcdn.com/group11/M06/50/A1/wKgDbVW0fGnSbbgJABHB5LfTflo882.mp3.apb')
expanded_name = ''


if m:
    expanded_name = m.group(1)

print 'expanded_name: ' + expanded_name
testfunction('aaa')
testfunction('bbb')



