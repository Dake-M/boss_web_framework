# -*- coding: utf-8 -*-

# BOSS登录非正常登录数据
boss_unnomal_data1 = [
    {"user": "13266816552", "pwd": "123456", "check": "账号或密码错误"},
    {"user": "13266816551", "pwd": "147258", "check": "账号或密码错误"},
    {"user": "13266816551", "pwd": "123456 ", "check": "账号或密码错误"},
    {"user": "13266816551", "pwd": "123 456", "check": "账号或密码错误"},
    {"user": "13266816551", "pwd": " 123456", "check": "账号或密码错误"}
]
boss_unnomal_data2 = [
    {"user": "", "pwd": "123456", "check": "请输入用户名"},
    {"user": "13266816552", "pwd": "", "check": "请输入密码"},
    {"user": "13266816551 ", "pwd": "123456", "check": "请输入正确的账号"},
    {"user": "1326681 6551", "pwd": "123456", "check": "请输入正确的账号"},
    {"user": " 13266816551", "pwd": "123456", "check": "请输入正确的账号"}
]

# boss_unnomal_data3 = [
#     {"user": "13266816551 ", "pwd": "123456", "check": "请输入正确的账号"},
#     {"user": "1326681 6551", "pwd": "123456", "check": "请输入正确的账号"},
#     {"user": " 13266816551", "pwd": "123456", "check": "请输入正确的账号"}
#
# ]