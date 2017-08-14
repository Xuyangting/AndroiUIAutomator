# -*- coding:utf-8 -*-
import os
import urllib
import datetime
from Util import util
from Config import config


# 查看包名，如果存在就删除，进行重新安装APP
def reinstall_app(env, app_path):
    print u"============================= 初始化测试环境 ============================="
    # 查看手机中安装所有应用的包名
    find_data = os.popen("adb shell pm list packages").readlines()
    for data in find_data:
        if config.PACKAGE.get(env) in data.strip():
            print u"%s 删除已安装APP, Package=%s" % (util.log_time(datetime.datetime.now()), config.PACKAGE.get(env))
            return_data = os.popen("adb uninstall %s" % config.PACKAGE.get(env)).readlines()
            for item in return_data:
                print u"%s %s" % (util.log_time(datetime.datetime.now()), item.strip())
    local = "APP.apk"
    urllib.urlretrieve(app_path, local)
    print u"%s 安装APP, Package=%s" % (util.log_time(datetime.datetime.now()), config.PACKAGE.get(env))
    return_data = os.popen("adb install %s" % local).readlines()
    print u"%s %s" % (util.log_time(datetime.datetime.now()), return_data[-2].strip())
    print u"%s %s" % (util.log_time(datetime.datetime.now()), return_data[-1].strip())


# 主函数 - 测试入口 run tests
def main():
    os.system("py.test %s/TestCase/ --html=%s/Report/%s.html" % (
        config.BASE_DIR,
        config.BASE_DIR,
        util.report_time(datetime.datetime.now())
    ))

if __name__ == '__main__':
    apk_path = "http://apk.mhs.local/apks/majikwealth/android/app/debug/majikWealth_v2.2.0(Build_952)_official_20170809_0908.apk"
    reinstall_app(config.ENV, apk_path)
    main()




