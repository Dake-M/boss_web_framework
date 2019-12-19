# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class ShowManageLocators:
    """
    指引管理页面元素信息
    """
    # 主菜单指引管理
    show_manage_menu = (By.XPATH, "//span[text()='指引管理']")

    # ===========================指引管理页面===========================
    # 添加模块按钮
    add_module_btn = (By.XPATH, "//span[text()='添加模块']")
    # 列表第一行模块名称
    module_name = (By.XPATH, "//tbody//tr[1]//div")
    # 列表第一行操作列删除按钮
    module_del_btn = (By.XPATH, "//tbody//tr[1]//span[text()='删除']")
    # 列表第一行删除确定按钮
    module_del_sure_btn = (By.XPATH, "//span[contains(.,'确定')]")
    # 列表第一行操作列详情按钮
    information_btn = (By.XPATH, "//tbody//tr[1]//span[text()='详情']")
    # 左上角title名称
    left_up_info = (By.XPATH, "//div[@class='info-title']")

    # ===========================新增指引模块页面==============================
    # 名称文本框
    input_name = (By.XPATH, "//label[@for='name']/following-sibling::div//input")
    # 排序文本框
    input_index = (By.XPATH, "//label[@for='index']/following-sibling::div//input")
    # logo 上传按钮
    load_logo_btn = (By.XPATH, "//i[@class='el-icon-plus upload-demo-icon over']")
    # 添加指引模块确定按钮
    add_module_sure_btn = (By.XPATH, "//button[@class='el-button el-button--primary']")

    # ===========================详情页面====================================
    # 添加指引按钮
    add_gui_btn = (By.XPATH, "//span[text()='添加指引']")
    # 列表第一行指引项名称//tbody//tr[1]//td[4]//span[text()='删除']
    gui_item_name =(By.XPATH, "//tbody//tr[1]//td[2]//div")
    # 列表操作列删除按钮
    gui_item_del_btn = (By.XPATH, "//tbody//tr[1]//td[4]//span[text()='删除']")
    # 删除确定按钮
    del_sure_btn = (By.XPATH, "//button//span[contains(text(),'确定')]")

    # ============================添加指引页面================================
    # 名称文本框
    input_gui_name = (By.XPATH, "//input[@type='text' and @class = 'el-input__inner']")
    # 排序文本框
    input_gui_index = (By.XPATH, "//input[@type='number']")
    # 展示
    iframe_ele = (By.XPATH, "//iframe[@class= 'ke-edit-iframe']")
    input_gui_text = (By.XPATH, "//body[contains(@class,'ke-content')]")
    # 提交按钮
    submit_gui_btn = (By.XPATH, "//span[text()='提交']")