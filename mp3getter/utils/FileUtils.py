# coding:utf-8

import os
import re


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

