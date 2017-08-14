# -*- coding:utf-8 -*-
import datetime
from Config import config


# 将时间显示成： 年-月-日 时：分：秒
def log_time(now):
    return now.strftime("[%Y-%m-%d %H:%M:%S]")


# 将时间显示成：年月日时分秒
def report_time(now):
    return now.strftime("%Y%m%d%H%M%S")


# 失败截图
def fail_screen_shot(my_device):
    my_device.screen_shot("%s/Pic/%s.jpg" % (config.BASE_DIR, report_time(datetime.datetime.now())))



