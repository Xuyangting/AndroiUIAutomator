# -*- coding:utf-8 -*-
import os
# ------------- 基础路径 -------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ------------- 测试环境 -------------
ENV = "qa"

# ------------- 错误码 -------------
ERROR = {
    "404": ["404", u"元素文档中未找到该元素，请检测搜索元素名称"]
}

# ------------ 有鱼股票 -------------
PACKAGE = {
    "qa": "com.ruifusoft.finance.app.debug",
    "live": "com.ruifusoft.finance.app"
}



