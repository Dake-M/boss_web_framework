# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class LoginLocs:
    """
    登录页面元素定位
    """
#  ==================BOSS系统==========================
    # 登录账号文本框
    boss_input_user = (By.XPATH, "//input[@placeholder='请输入登录手机号']")
    # 登录密码文本框
    boss_input_password = (By.XPATH, "//input[@placeholder='请输入密码']")
    # 登录按钮
    boss_login_btn = (By.XPATH, "//button[@class = 'el-button el-button--primary']")

    # 错误提示
    boss_tip1 = (By.XPATH, "//p[@class = 'el-message__content']")
    boss_tip2 = (By.XPATH, "//div[@class = 'el-form-item__error']")

#  ==================运营商系统==========================
    # 登录账号文本框
    operator_input_user = (By.XPATH, "//input[@placeholder='账号']")
    # 登录密码文本框
    operator_input_password = (By.XPATH, "//input[@placeholder='密码']")
    # 滑动图标
    operator_img = (By.XPATH, "//div[@class='slider-btn']//img")
    # 登录按钮
    operator_login_btn = (By.XPATH, "//button[@class='el-button userbtn el-button--primary el-button--medium']")
