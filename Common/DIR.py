# -*- coding:utf-8 -*-
import os
from datetime import datetime

# 根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件目录
CONFIGS_DIR = os.path.join(BASE_DIR, "configs")
CONFIGS_FILE_PATH = os.path.join(CONFIGS_DIR, "config.conf")


# 用例文件目录
CASE_DIR = os.path.join(BASE_DIR, "TestDatas\case_data")
CASE_FILE_PATH = os.path.join(CASE_DIR, "cases.xlsx")
PYCASE_DIR = os.path.join(BASE_DIR, "TestCases")


# 日志文件目录
LOGS_DIR = os.path.join(BASE_DIR, "Outputs\logs")
LOG_FILE_PATH = os.path.join(LOGS_DIR, "web_log.log")

# 报告文件目录
REPORTS_DIR = os.path.join(BASE_DIR, r"Outputs\reports")
str1 = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
report_name = "report_{0}.html".format(str1)
REPORTS_FILE_PATH = os.path.join(REPORTS_DIR, report_name)

# 截图存放目录
SCREEN_DIR = os.path.join(BASE_DIR, "Outputs\screenshots")


if __name__ == '__main__':
    print(BASE_DIR)
    print(PYCASE_DIR)
