# -*- coding: utf-8 -*-
import time
from Common.BasePage import BasePage
from Common.LOAD_FILE import WinUpLoadFile
from PageLocators.gui_manage_locators import ShowManageLocators as sml


class ShowManagePage(BasePage):
    """
    指引管理页面逻辑处理封装
    """
    def get_info_title(self):
        """
        获取左上角title文案
        :return:
        """
        text = self.get_element_text(sml.left_up_info, "左上角标题")
        return text

    def add_gui_module(self, module_name, path):
        """
        添加指引模块
        :return:
        """
        # self.click_element(sml.show_manage_menu, "点击主菜单指引管理")
        self.click_element(sml.add_module_btn, "点击添加模块按钮")
        time.sleep(1)
        self.input_text(module_name, sml.input_name, "新增指引模块输入模块名称")
        self.input_text(1, sml.input_index, "新增指引模块输入排序")
        self.click_element(sml.load_logo_btn, "点击上传按钮")
        time.sleep(1)
        WinUpLoadFile().winUpLoadFile(path, "打开")
        time.sleep(1)
        self.click_element(sml.add_module_sure_btn, "新增指引模块点击确定按钮")

    def del_gui_module(self):
        """
        删除指引模块
        :return:
        """
        # self.enter_url("https://payexp.snsshop.net/bossmanage/guide")
        self.click_element(sml.module_del_btn, "点击删除按钮")
        self.click_element(sml.module_del_sure_btn, "点击删除指引模块确定按钮")

    def get_module_name(self):
        """
        如果存在则返回第一行模块名称
        如果不存在则返回False
        :return:
        """

        self.enter_url("https://payexp.snsshop.net/bossmanage/guide")
        if self.if_ele_is_exist(sml.module_name, "第一行模块名称"):
            return self.get_element_text(sml.module_name, "获取第一行模块名称")
        else:
            return False

    def add_show_item(self, url, gui_name, gui_text):
        """
        新增指引管理
        :return:
        """
        self.enter_url(url)
        self.click_element(sml.add_gui_btn, "点击添加指引按钮")
        self.input_text(gui_name, sml.input_gui_name, "输入指引项名称")
        self.input_text(1, sml.input_gui_index, "输入指引排序")
        self.switch_to_frame(sml.iframe_ele, "切换iframe")
        self.input_text(gui_text, sml.input_gui_text, "输入指引展示文案")
        self.switch_to_default()
        self.click_element(sml.submit_gui_btn, "点击提交按钮")
        time.sleep(2)

    def del_gui_item(self, url):
        """
        删除指引项
        :return:
        """
        self.enter_url(url)
        self.click_element(sml.gui_item_del_btn, "点击指引项第一行删除按钮")
        self.click_element(sml.del_sure_btn, "点击删除指引项确定按钮")

    def get_gui_item_name(self):
        """
        如果存在则返回指引项第一行名称
        如果不存在则返回False
        :return:
        """
        self.web_refresh()
        if self.if_ele_is_exist(sml.gui_item_name, "获取指引项名称"):
            return self.get_element_text(sml.gui_item_name, "获取指引项名称")
        else:
            return False







