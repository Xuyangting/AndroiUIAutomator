# -*- coding:utf-8 -*-
import stockCommon
import stockOptional
import stockTrade
import stockMarket
import stockMy
from Config import config


def get_element(name):
    result = ""
    all_element = dict(
        stockCommon.common.items() +
        stockOptional.optional.items() +
        stockTrade.trade.items() +
        stockMarket.market.items() +
        stockMy.my.items()
    )
    for k, v in all_element.items():
        if k == name:
            result = v
            break

    if result == "":
        return config.ERROR.get("404")
    else:
        return result


