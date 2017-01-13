# coding:utf-8

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

PrintLog = False


# 根据全局配置来打印信息
def log(log_info, log_flag=False):
    if PrintLog or log_flag:
        print log_info

