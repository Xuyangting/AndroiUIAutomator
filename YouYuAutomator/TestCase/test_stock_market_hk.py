# -*- coding:utf-8 -*-
import datetime
import baseTest
from Pages import element
from Util import util


class TestMarketHK(baseTest.BaseTest):
    # 新股日历
    def test_new_stock(self):
        try:
            # 进入新股日历
            self.my_service.click(element.get_element("stock_market_marketButton"))
            self.my_service.click(element.get_element("stock_market_newStock"))
            self.my_service.sleep_screen(5)
            # 通过上市时间和IPO以来表现的差异进行划分待上市数据和已上市数据
            data_three_length = self.my_service.get_length(
                element.get_element("stock_market_hk_new_stock_num_three")
            )
            wait_public_num = 0
            for i in range(data_three_length):
                three_text = self.my_service.get_text_by_index(
                    element.get_element("stock_market_hk_new_stock_num_three"),
                    i
                )
                if "%" not in three_text:
                    wait_public_num += 1
            already_public_num = data_three_length - wait_public_num
            print "%s 待上市 -> %s  已上市 -> %s" % (
                util.log_time(datetime.datetime.now()),
                str(wait_public_num),
                str(already_public_num)
            )
            # 检测待上市 -> 1级数据
            print u"%s 检测待上市 -> 1级数据" % util.log_time(datetime.datetime.now())
            if wait_public_num == 0:
                print u"%s -- Check Point -- 待上市列表中没有数据，请手动进行检测" %\
                      util.log_time(datetime.datetime.now())
            else:
                for i in range(wait_public_num):
                    baseTest.check_list_data(self.my_service, i, "stock_market_hk_new_stock_name", u"股票名称",
                                             datetime.datetime.now())
                    baseTest.check_list_data(self.my_service, i, "stock_market_hk_new_stock_code", u"股票代码",
                                             datetime.datetime.now())
                    baseTest.check_list_data(self.my_service, i, "stock_market_hk_new_stock_num_one", u"申购价",
                                             datetime.datetime.now())
                    baseTest.check_list_data(self.my_service, i, "stock_market_hk_new_stock_num_two", u"入场费",
                                             datetime.datetime.now())
                    baseTest.check_list_data(self.my_service, i, "stock_market_hk_new_stock_num_three", u"上市时间",
                                             datetime.datetime.now())
            # 检测待上市 -> 2级数据

            # 检测已上市 -> 1级数据
            print u"%s 检测已上市 -> 1级数据" % util.log_time(datetime.datetime.now())
            if already_public_num == 0:
                print u"%s -- Check Point -- 已上市列表中没有数据，请手动进行检测" % \
                      util.log_time(datetime.datetime.now())
            else:
                for i in range(already_public_num):
                    baseTest.check_list_data(self.my_service, i, "stock_market_hk_new_stock_name", u"股票名称",
                                             datetime.datetime.now())
                    baseTest.check_list_data(self.my_service, i, "stock_market_hk_new_stock_code", u"股票代码",
                                             datetime.datetime.now())
                    baseTest.check_list_data(self.my_service, i, "stock_market_hk_new_stock_num_one", u"发行价",
                                             datetime.datetime.now())
                    baseTest.check_list_data(self.my_service, i, "stock_market_hk_new_stock_num_two", u"现价",
                                             datetime.datetime.now())
                    baseTest.check_list_data(self.my_service, i, "stock_market_hk_new_stock_num_three", u"IPO以来表现",
                                             datetime.datetime.now())
            # 检测已上市 -> 2级数据

        except:
            util.fail_screen_shot(self.my_service)
            assert False

    # 分红派息
    # def test_dividend(self):
    #     try:
    #         # 进入分红派息
    #         self.my_service.click(element.get_element("stock_market_marketButton"))
    #         self.my_service.click(element.get_element("stock_market_dividend"))
    #         self.my_service.sleep_screen(2)
    #     except:
    #         util.fail_screen_shot(self.my_service)
    #         assert False



