# -*- coding: utf-8 -*-
import time
from PageLocators.home_page_locators import HomeLocs as hl
from Common.BasePage import BasePage


class HomePage(BasePage):
    """
    首页
    """

    def get_img_names1(self):
        """
        获取收费数据content_top的名称
        :return: 名称列表
        """
        self.web_refresh()
        return self.find_display_elements(hl.content_top, 2)

    def get_img_names2(self):
        """
        获取商户数据content_top的名称
        :return: 名称列表
        """
        self.web_refresh()
        self.click_element(hl.tab_btn, "点击商户数据")
        return self.find_display_elements(hl.content_top, 2)

    def quit_login(self):
        """
        退出登录
        :return:
        """
        time.sleep(2)
        self.move_mouse(hl.user, "移动鼠标到右上角帐号处")
        time.sleep(2)
        self.click_element(hl.quit_btn, "点击退出登录按钮")



