# -*- coding:utf-8 -*-
import os
import datetime
from Pages import element
from Service import service
from uiautomator import device
from Config import config
from Util import util


# 检测列表数据显示
def check_list_data(my_device, index, el_name, text, current):
    stock_name = my_device.get_text_by_index(element.get_element(el_name), index)
    print u"%s %s -> %s" % (
        util.log_time(current),
        text,
        stock_name
    )
    assert stock_name != "None"


# --------------------------------------------
# 基础类
# --------------------------------------------
class BaseTest:
    my_service = service.Service(device)

    # 在每个测试方法开始执行
    def setup_method(self):
        self.my_service.screen_on()
        self.my_service.click(element.get_element("common_app_name"))
        self.my_service.sleep_screen(5)
        if self.my_service.exists(element.get_element("common_welcome_indicator")):
            self.my_service.swipe("left", 0.7, 0.2, 10)
            self.my_service.swipe("left", 0.7, 0.2, 10)
            self.my_service.click(element.get_element("common_welcome_experience"))
        else:
            print u"%s 跳过欢迎页" % util.log_time(datetime.datetime.now())

    # 在每个测试方法结束执行
    def teardown_method(self):
        self.my_service.press_home()
        os.system("adb shell pm clear %s" % config.PACKAGE.get(config.ENV))




