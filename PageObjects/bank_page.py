# -*- coding: utf-8 -*-
import time
from Common.BasePage import BasePage
from Common.LOAD_FILE import WinUpLoadFile
from PageLocators.bank_page_locators import BankLocators as bl


class BankPage(BasePage):
    """
    银行管理页面逻辑封装
    """
    def get_info_title(self):
        """
        获取左上角title文案
        :return:
        """
        text = self.get_element_text(bl.info_title, "左上角标题")
        return text

    def add_bank(self, bank_name, organization_code):
        """
        添加一级银行
        :return:
        """
        self.click_element(bl.add_bank_btn, "添加添加银行按钮")
        self.input_text(bank_name, bl.input_bank_name, "输入银行名称")
        self.input_text(organization_code, bl.input_organization_code, "输入机构代码")
        self.click_element(bl.btn_add_bank, "点击添加银行确定按钮")
        time.sleep(1)

    def get_add_tip(self):
        """
        获取添加银行成功提示信息
        :return:
        """
        text = self.get_element_text(bl.add_bank_tip, "获取添加提示")
        return text

    def get_bank_name(self):
        """
        获取列表第一行银行名称
        如果存在则返回指引项第一行名称
        如果不存在则返回False
        :return:
        """
        self.web_refresh()
        if self.if_ele_is_exist(bl.bank_name, "获取列表第一行银行名称"):
            return self.get_element_text(bl.bank_name, "获取列表第一行银行名称")
        else:
            return False

    def get_organization_code(self):
        """
        获取列表第一行机构代码
        如果存在则返回指引项第一行名称
        如果不存在则返回False
        :return:
        """
        self.web_refresh()
        if self.if_ele_is_exist(bl.organization_code_text, "获取列表第一行机构代码"):
            return self.get_element_text(bl.organization_code_text, "获取列表第一行机构代码")
        else:
            return False

    def del_bank(self):
        """
        删除银行
        :return:
        """
        self.click_element(bl.bank_del_btn, "点击列表第一行操作列删除按钮")
        self.click_element(bl.del_sure_btn, "点击删除确定按钮")
        time.sleep(1)

    def get_del_tip(self):
        """
        获取删除提示
        :return:
        """
        text = self.get_element_text(bl.del_bank_tip, "获取删除提示信息")
        return text

    def get_up_organization_code(self):
        """
        获取上级机构和机构代码
        :return:
        """
        self.click_element(bl.lower_level_organization, "点击进入下级机构页面")
        self.web_refresh()
        text1 = self.get_element_text(bl.up_level_organization, "获取上级机构名称")
        text2 = self.get_element_text(bl.organization_code, "获取机构代码")
        return text1, text2

    def add_organization_bank(self, bank_name, organization_code, province_code):
        """
        添加下级机构银行
        :return:
        """
        self.click_element(bl.lower_level_organization, "点击进入下级机构页面")
        self.click_element(bl.organization_add_bank_btn, "点击新增银行按钮")
        self.input_text(bank_name, bl.input_bank_name, "在文本框中输入银行名称")
        self.input_text(organization_code, bl.input_organization_code, "在文本框中输入机构代码")
        self.input_text(province_code, bl.input_province_code, "在文本框中输入省市代码")
        self.click_element(bl.btn_add_bank, "点击确定按钮")
        time.sleep(1)

    def add_organization_banks(self, path):
        """
        批量导入添加
        :return:
        """
        self.click_element(bl.lower_level_organization, "点击进入下级机构页面")
        self.click_element(bl.add_banks_btn, "点击批量添加按钮")
        self.click_element(bl.upload_img, "点击上传按钮")
        up_load = WinUpLoadFile()
        up_load.winUpLoadFile(path, "打开")
        time.sleep(2)

    def del_organization_bank(self):
        """
        删除下级机构银行
        :return:
        """
        self.click_element(bl.lower_level_organization, "点击进入下级机构页面")
        self.click_element(bl.bank_del_btn, "点击列表第一行操作列的删除按钮")
        self.click_element(bl.del_sure_btn, "点击删除确定按钮")
        time.sleep(1)













