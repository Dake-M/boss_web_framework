# -*- coding: utf-8 -*-
import time
from selenium.webdriver import ActionChains
from PageLocators.login_locators import LoginLocs as ll
from Common.BasePage import BasePage


class LoginPage(BasePage):
    """
    登录
    """
    def boss_login(self, user, pwd):
        """
        登录操作
        :param user:帐号
        :param pwd: 密码
        :return:
        """
        self.web_refresh()
        self.input_text(user, ll.boss_input_user, "输入账号")
        self.input_text(pwd, ll.boss_input_password, "输入密码")
        self.click_element(ll.boss_login_btn, "点击登录按钮")
        time.sleep(0.5)

    def get_tip1(self):
        """
        错误账号或密码获取提示信息
        :return:
        """
        text = self.get_element_text(ll.boss_tip1, "获取错误提示信息")
        return text

    def get_tip2(self):
        """
        错误账号或密码获取提示信息
        :return:
        """
        text = self.get_element_text(ll.boss_tip2, "获取错误提示信息")
        return text

    def group_login(self, user, pwd):
        """
        运营商登录
        """
        self.web_refresh()
        self.input_text(user, ll.operator_input_user, "输入账号")
        self.input_text(pwd, ll.operator_input_password, "输入密码")
        self.click_move_mouse(ll.operator_img, "滑动验证")
        # time.sleep(3)
        self.click_element(ll.operator_login_btn, "点击登录按钮")
        time.sleep(0.5)




