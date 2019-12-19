# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class AdLocators:
    """
    广告管理页面网页元素信息
    """
    # ========================  广告管理页面  ======================
    # 页面左上角标题
    info_title = (By.XPATH, "//div[@class='info-title']")
    # 广告名称搜索文本框
    search_ad_name = (By.XPATH, "//label//span[text()='广告名称：']/following-sibling::div//input")
    # 搜索按钮
    search_btn = (By.XPATH, "//button/span[text()='搜索']")
    # 新增广告按钮
    add_ad_btn = (By.XPATH, "//a/span[text()='+创建广告']")
    # 广告列表第一行广告名称
    ad_name = (By.XPATH, "//tr[1]//td[1]//div[1]")
    # 广告列表第一行删除
    del_ad_btn = (By.XPATH, "//tr[1]//td[8]//button//span[text()='删除']")
    # 删除确定按钮
    del_sure_btn = (By.XPATH, "//span[contains(.,'确定')]")
    # 删除提示
    del_tip = (By.XPATH, "//p[@class='el-message__content']")
    # 广告列表第一行状态按钮
    status_btn = (By.XPATH, "//tr[1]//td[7]//div[1]//div[1]")

    # =========================  新增广告页面  ====================
    # 广告名称输入文本框
    input_ad_name = (By.XPATH, "//label[@for='title']/following-sibling::div//input")
    # 展示时间
    js_start_time = '''
    var start_time = document.getElementsByClassName('el-range-input')[0];
    start_time.value = arguments[0];
    '''
    js_end_time = '''     
    var end_time = document.getElementsByClassName('el-range-input')[1];
    end_time.value = arguments[0];
    '''
    js_button = '''
    var button = document.getElementsByTagName('button')[11];
    button.disabled = false;
    '''

    # 广告图片上传按钮
    ad_img_upload_btn = (By.XPATH, "//div[@class='el-upload el-upload--text']")
    # 条件链接文本框
    input_url = (By.XPATH, "//label[@for='adUrl']/following-sibling::div//input")
    # 投放客户选择按钮
    throw_user_choose_btn = (By.XPATH, "//span[@class='iscustomer']")
    # 确认按钮
    sure_btn = (By.XPATH, "//button[@class='el-button el-button--primary el-button--small']")

    # ============================= 投放客户选择页面 ===============================
    # 教育局/集团文本框
    input_education_name = (By.XPATH, "//label[text()='教育局/集团:']/following-sibling::div//input")
    # 搜索按钮
    serch_btn = (By.XPATH, "//button[@type='button'][contains(.,'搜 索')]")
    # 勾选框
    choose_item = (By.XPATH, "//tbody//tr[1]//span[@class='el-checkbox__inner']")
    # 确定按钮
    submit_btn = (By.XPATH, "//button[@type='button'][contains(.,'确 定')]")


