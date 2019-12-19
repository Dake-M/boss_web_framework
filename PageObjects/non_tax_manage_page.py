# -*- coding: utf-8 -*-
import time
from Common.BasePage import BasePage
from PageLocators.non_tax_locators import NonTaxLocs as ntl


class NonTaxManagePage(BasePage):
    """
    非税局管理页面
    """
    def get_info_title(self):
        """
        获取info标题
        :return:
        """
        text = self.get_element_text(ntl.info_title, "获取左上角信息标题")
        return text

    def add_tax_manage(self, bank_name, realm_name, realm_code, public_key, public_address, token1, institution_name, private_key, token2):
        """
        新增非税局
        :return:
        """
        self.click_element(ntl.add_btn, "点击新增非税局按钮")
        self.click_element(ntl.type_name, "点击平台类型下拉框")
        time.sleep(1)
        self.click_element(ntl.select_value, "点击选择湖南非税局")
        self.click_element(ntl.terrace_name, "点击平台名下拉框")
        time.sleep(1)
        self.click_element(ntl.select_value2, "点击选择农行重庆分行")
        self.input_text(realm_name, ntl.realm_name, "输入区域名")
        self.input_text(realm_code, ntl.realm_code, "输入区域编号")
        self.input_text(public_key, ntl.public_key, "输入平台公钥")
        self.input_text(public_address, ntl.public_address, "输入接口地址")
        self.input_text(token1, ntl.token1, "输入平台查询token")
        self.input_text(institution_name, ntl.institution_name, "输入机构名称")
        self.click_element(ntl.bank, "点击所属银行下拉框")
        time.sleep(1)
        new_bank_name = (ntl.bank_name[0], ntl.bank_name[1].format(bank_name))
        time.sleep(1)
        self.click_element(new_bank_name, "点击选择{}".format(bank_name))
        self.input_text(private_key, ntl.private_key, "输入平台私钥")
        self.input_text(token2, ntl.token2, "输入平台token")
        self.click_element(ntl.submit_btn, "点击提交按钮")
        time.sleep(1)

    def get_realm_name(self):
        """
        获取列表机构名
        :return:
        """
        self.web_refresh()
        text = self.get_element_text(ntl.realm_name_text, "获取列表第一个非税局名称")
        return text

    def dele_tax_manage(self):
        """
        删除非税局
        :return:
        """
        self.web_refresh()
        self.click_element(ntl.dele_btn, "点击删除按钮")
        self.click_element(ntl.sure_btn, "点击确定删除按钮")

    def enter_tax_manage_code(self):
        self.web_refresh()
        self.click_element(ntl.more_btn, "点击操作列更多按钮")
        self.click_element(ntl.item_btn, "点击缴费项目管理按钮")

    def add_tax_manage_code(self, item_name, item_code, inner_code, max_price, min_price, count_uint):
        """
        新增非税局项目code
        :return:
        """
        self.enter_tax_manage_code()
        self.click_element(ntl.add_code_btn, "点击新增非税局项目code按钮")
        self.input_text(item_name, ntl.input_item, "输入项目名称")
        self.input_text(item_code, ntl.input_item_code, "输入项目编码")
        self.input_text(inner_code, ntl.input_inner_code, "输入项目内部编码")
        self.input_text(max_price, ntl.input_max_price, "输入缴费上限金额")
        self.input_text(min_price, ntl.input_min_price, "输入缴费最低金额")
        self.input_text(count_uint, ntl.input_count_uint, "输入计量单位")
        self.click_element(ntl.inner_submit_btn, "点击提交按钮")
        time.sleep(1)

    def get_code_name_text(self):
        """
        获取code的项目名称
        :return:
        """
        self.web_refresh()
        text = self.get_element_text(ntl.item_name, "获取列表第一行项目名称")
        return text

    def del_tax_manage_code(self):
        """
        删除非税局项目code
        :return:
        """
        self.enter_tax_manage_code()
        self.web_refresh()
        self.click_element(ntl.del_btn, "code点击删除按钮")
        self.click_element(ntl.del_sure_btn, "点击删除确定按钮")

    def get_del_notax_code_tip_text(self):
        """
        获取删除成功提示
        :return:
        """
        text = self.get_element_text(ntl.del_tip, "获取删除成提示")
        return text

    def enter_tax_unit(self):
        """
        进入报税单位
        :return:
        """
        self.web_refresh()
        self.click_element(ntl.more_btn, "点击操作列更多按钮")
        self.click_element(ntl.tax_unit_btn, "点击报税单位管理按钮")

    def add_tax_unit(self, name, code, instanceToken, instanceQueryToken, instanceTokenApp, instanceQueryApp):
        """
        新增报税单位
        :return:
        """
        self.enter_tax_unit()
        self.web_refresh()
        self.click_element(ntl.add_tax_unit_btn, "点击新增报税单位按钮")
        self.input_text(name, ntl.input_unit_name, "输入缴费单位名称")
        self.input_text(code, ntl.input_unit_code, "输入缴费单位code")
        self.input_text(instanceToken, ntl.input_unit_instanceToken, "输入token")
        self.input_text(instanceQueryToken, ntl.input_unit_instanceQueryToken, "输入查询token")
        self.input_text(instanceTokenApp, ntl.input_unit_instanceTokenApp, "输入token配套app")
        self.input_text(instanceQueryApp, ntl.input_unit_instanceQueryApp, "输入查询token配套app")
        self.click_element(ntl.add_unit_submit_btn, "点击提交按钮")
        time.sleep(1)

    def get_tax_unit_name_tex(self):
        """
        获取列表第一列的缴费单位名称
        :return:
        """
        self.web_refresh()
        text = self.get_element_text(ntl.tax_unit_name, "获取缴费名单名称")
        return text

    def del_tax_unit(self):
        """
        删除列表第一列的报税单位
        :return:
        """
        self.enter_tax_unit()
        self.web_refresh()
        self.click_element(ntl.tax_unit_del_btn, "非税局报税单位点击删除按钮")
        self.click_element(ntl.tax_unit_del_sure_btn, "点击删除确定按钮")

    def get_del_unit_tip(self):
        """
        非税局报税单位获取删除提示信息
        :return:
        """
        text = self.get_element_text(ntl.tax_unit_del_tip, "获取非税局报税单位删除成提示")
        return text














