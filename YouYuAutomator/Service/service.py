# -*- coding:utf-8 -*-
import sys
import datetime
from Util import util
from time import sleep
from Config import config
# 重置python默认编码格式为utf-8
reload(sys)
sys.setdefaultencoding("utf-8")


# 返回查找元素方法
def find_element(device, find_type, find_text):
    if find_type == "text":
        return device(text=find_text)
    if find_type == "resource":
        return device(resourceId= config.PACKAGE.get(config.ENV) + find_text)


class Service:
    def __init__(self, device):
        self.device = device

    # 点亮屏幕
    def screen_on(self):
        print u"%s 点亮屏幕" % util.log_time(datetime.datetime.now())
        self.device.screen.on()

    # 熄灭屏幕
    def screen_off(self):
        print u"%s 熄灭屏幕" % util.log_time(datetime.datetime.now())
        self.device.screen.off()

    # 点击手机HOME键
    def press_home(self):
        print u"%s 点击手机HOME键" % util.log_time(datetime.datetime.now())
        self.device.press.home()

    # 点击手机回退键
    def press_back(self):
        print u"%s 点击手机回退键" % util.log_time(datetime.datetime.now())
        self.device.press.back()

    # 截图
    def screen_shot(self, pic):
        print u"%s 失败截图 -> %s" % (util.log_time(datetime.datetime.now()), pic)
        self.device.screenshot(pic)

    # 输入文本
    def set_text(self, element, text):
        print u"%s 输入 -> %s" % (util.log_time(datetime.datetime.now()), text)
        device = find_element(self.device, element[0], element[1])
        device.set_text(text)

    # 清空文本
    def clear_text(self, element):
        print u"%s 清空 -> %s" % (util.log_time(datetime.datetime.now()), element[2])
        device = find_element(self.device, element[0], element[1])
        device.clear_text()

    # 获取文本
    def get_text(self, element):
        device = find_element(self.device, element[0], element[1])
        data = device.info
        return str(data.get("text"))

    # 获取文本
    def get_text_by_index(self, element, index):
        device = find_element(self.device, element[0], element[1])
        data = device[index].info
        result = str(data.get("text"))
        return result

    # 获取同一个页面resource id相同的元素的个数
    def get_length(self, element):
        device = find_element(self.device, element[0], element[1])
        element_length = len(device)
        print u"%s 长度 -> %s" % (util.log_time(datetime.datetime.now()), str(element_length))
        return element_length

    # 点击事件
    def click(self, element):
        print u"%s 点击 -> %s" % (util.log_time(datetime.datetime.now()), element[2])
        device = find_element(self.device, element[0], element[1])
        device.click()

    # 时间暂停，休眠
    def sleep_screen(self, second):
        print u"%s 等待%s秒" % (util.log_time(datetime.datetime.now()), str(second))
        sleep(second)

    # 判断元素是否存在
    def exists(self, element):
        print u"%s 判断元素是否存在 -> %s" % (util.log_time(datetime.datetime.now()), element[2])
        device = find_element(self.device, element[0], element[1])
        if device.exists:
            print u"%s 元素存在" % util.log_time(datetime.datetime.now())
            return True
        else:
            print u"%s 元素不存在" % util.log_time(datetime.datetime.now())
            return False

    # 屏幕滑动
    def swipe(self, direction, start, end, step):
        data = self.device.info
        mobile_width = data.get("displayWidth")
        mobile_height = data.get("displayHeight")
        if direction == "up":
            print u"%s 向上滑" % util.log_time(datetime.datetime.now())
            self.device.swipe(mobile_width * 0.5, mobile_height * start, mobile_width * 0.5, mobile_height * end, step)
        if direction == "down":
            print u"%s 向下滑" % util.log_time(datetime.datetime.now())
            self.device.swipe(mobile_width * 0.5, mobile_height * start, mobile_width * 0.5, mobile_height * end, step)
        if direction == "left":
            print u"%s 向左滑" % util.log_time(datetime.datetime.now())
            self.device.swipe(mobile_width * start, mobile_height * 0.5, mobile_width * end, mobile_height * 0.5, step)
        if direction == "right":
            print u"%s 向右滑" % util.log_time(datetime.datetime.now())
            self.device.swipe(mobile_width * start, mobile_height * 0.5, mobile_width * end, mobile_height * 0.5, step)






