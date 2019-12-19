# -*- coding: utf-8 -*-
import time
from Common.BasePage import BasePage
from PageLocators.ad_locators import AdLocators as al
from Common.LOAD_FILE import WinUpLoadFile


class AdPage(BasePage):
    """
    广告管理页面逻辑处理封装
    """

    def get_info_title(self):
        """
        获取左上角title文案
        :return:
        """
        text = self.get_element_text(al.info_title, "左上角标题")
        return text

    def search_ad(self, ad_name):
        """
        搜索广告
        :return:
        """
        self.web_refresh()
        self.input_text(ad_name, al.search_ad_name, "在广告名称文本框输入广告名称")
        self.click_element(al.search_btn, "点击搜索按钮")
        time.sleep(1)

    def get_ad_name(self):
        """
        获取列表第一行广告名称
        :return:
        """
        self.web_refresh()  # 刷新页面
        text = self.get_element_text(al.ad_name, "获取广告列表第一行广告名称")
        return text

    def get_status(self):
        """
        获取列表第一行广告名称状态
        :return:
        """
        status = self.get_element_attr(al.status_btn, "class", "获取状态信息")
        return status

    def add_ad(self, ad_name, start_time, end_time, path, url, group_name):
        """
        新增广告
        :return:
        """
        self.click_element(al.add_ad_btn, "点击创建广告按钮")
        self.input_text(ad_name, al.input_ad_name, "输入广告名称")
        self.js_execute(al.js_start_time, "展示开始时间设置", start_time)
        time.sleep(1)
        self.js_execute(al.js_end_time, "展示结束时间设置", end_time)
        time.sleep(1)
        self.click_element(al.ad_img_upload_btn, "点击上传按钮")
        time.sleep(1)
        WinUpLoadFile().winUpLoadFile(path, "打开")
        time.sleep(2)
        self.input_text(url, al.input_url, "输入跳转链接url")
        self.click_element(al.throw_user_choose_btn, "点击选择投放客户按钮")
        time.sleep(1)
        self.input_text(group_name, al.input_education_name, "在教育局/集团文本框输入教育局名称")
        self.click_element(al.serch_btn, "客户列表点击搜索按钮")
        time.sleep(1)
        self.click_element(al.choose_item, "点击勾选框选择客户")
        self.click_element(al.submit_btn, "选择客户点击确定按钮")
        time.sleep(3)
        self.click_element(al.sure_btn, "添加广告点击确定按钮")
        time.sleep(3)

    def del_ad(self):
        """
        删除广告
        :return:
        """
        self.click_element(al.del_ad_btn, "点击删除按钮")
        self.click_element(al.del_sure_btn, "点击删除确定按钮")
        time.sleep(1)

    def get_del_tip_text(self):
        """
        获取删除提示
        :return:
        """
        text = self.get_element_text(al.del_tip, "获取删除提示信息")
        return text















