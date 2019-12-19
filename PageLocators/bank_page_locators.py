# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class BankLocators:
    """
    银行管理模块元素管理页面
    """
    # ==================== 银行管理列表页面 =======================
    # 页面左上角标题
    info_title = (By.XPATH, "//div[@class='info-title']")
    # 新增银行按钮
    add_bank_btn = (By.XPATH, "//span[text()='+添加银行']")
    # 新增银行提示
    add_bank_tip = (By.XPATH, "//p[contains(@class,'el-message__content')]")
    # "//p[contains(@class,'el-message__content')]"
    # 银行列表第一行银行名称
    bank_name = (By.XPATH, "//tbody/tr[1]//td[1]//div")
    # 银行列表第一行机构代码
    organization_code_text = (By.XPATH, "//tbody/tr[1]//td[2]//div")
    # 银行列表第一行操作列删除按钮
    bank_del_btn = (By.XPATH, "//tbody/tr[1]//td[4]//span[text()='删除']")
    # 删除二次提醒确定按钮
    del_sure_btn = (By.XPATH, "//button//span[contains(.,'确定')]")
    # 删除成功提示
    del_bank_tip = (By.XPATH, "//p[contains(@class,'el-message__content')]")
    # 银行列表第一行操作列下级机构按钮
    lower_level_organization = (By.XPATH, "//tbody/tr[1]//td[4]//span[text()='下级机构']")

    # ==================== 下级机构列表页面 =======================
    # 搜索银行名称文本框
    input_bank_search = (By.XPATH, "//input[@class='el-input__inner']")
    # 搜索按钮
    search_btn = (By.XPATH, "//div[@class='fll']//button")
    # 上级机构
    up_level_organization = (By.XPATH, "//p[text()='上级机构：']/following-sibling::p")
    # 机构代码
    organization_code = (By.XPATH, "//p[text()='机构代码：']/following-sibling::p")
    # 添加银行按钮
    organization_add_bank_btn = (By.XPATH, "//div[@class='bankmanagewrap']//button[1]//span[1]")
    # 批量添加银行按钮
    add_banks_btn = (By.XPATH, "//span[text()='+批量添加']")
    # 上传入口
    upload_img = (By.XPATH, "//div[@class='el-upload-dragger']")

    # ==================== 添加银行页面 =======================
    # 银行名称文本框
    input_bank_name = (By.XPATH, "//label[@for='name']/following-sibling::div//input")
    # 机构代码文本框
    input_organization_code = (By.XPATH, "//label[@for='bankNo']/following-sibling::div//input")
    # 省市代码文本框
    input_province_code = (By.XPATH, "//label[@for='provinceCode']/following-sibling::div//input")
    # 添加银行确定按钮
    btn_add_bank = (By.XPATH, "//span[@class='dialog-footer']//span[contains(.,'确 定')]")

