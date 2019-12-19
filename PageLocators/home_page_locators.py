# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class HomeLocs:
    """
    boss首页元素
    """
# ===================boss首页==================
    # '今日收费', '昨日收费', '近一月收费'/
    content_top = (By.XPATH, "//div[@class = 'flex content-top']//span")
    # 商户数据
    tab_btn = (By.XPATH, "//div[@id = 'tab-merchant']")
    # 非税局管理按钮
    non_tax_menu = (By.XPATH, "//span[text() = '非税局管理']")
    # 指引管理菜单按钮
    gui_menu = (By.XPATH, "//span[text() = '指引管理']")
    # 广告管理菜单按钮
    ad_menu = (By.XPATH, "//span[text() = '广告管理']")
    # 银行管理菜单按钮
    bank_menu = (By.XPATH, "//span[text() = '银行管理']")
    # 应用管理菜单按钮
    open_app_menu = (By.XPATH, "//span[text() = '应用管理']")
    # 小程序管理菜单按钮
    applet_menu = (By.XPATH, "//span[text() = '小程序管理']")
    # 设置菜单按钮
    setting_menu = (By.XPATH, "//span[text() = '设置']")
    # 右上角帐号
    user = (By.XPATH, "//span[contains(@class,'user-name')]")
    # 右上角退出按钮
    quit_btn = (By.XPATH, "//li[@tabindex='-1'][contains(.,'退出')]")


