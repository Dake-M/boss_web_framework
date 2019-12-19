# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class NonTaxLocs:
    """
    非税局管理页面元素信息
    """
# ===================非税局管理页面===================
    # 左上角标题
    info_title = (By.XPATH, "//div[@class='info-title']")
    # 新增非税局按钮
    add_btn = (By.XPATH, "//span[text()='新增非税局']")
    # 非税局列表机构名字
    realm_name_text = (By.XPATH, "(//div[@class='cell'])[10]")
    # 列表删除按钮
    dele_btn = (By.XPATH, "(//span[text()='删除'])[1]")
    # 删除确定按钮
    sure_btn = (By.XPATH, "//span[contains(.,'确定')]")
    # 列表操作列更多操作按钮
    more_btn = (By.XPATH, "(//i[@class='el-icon-s-operation'])[1]")
    # 操作列更多下的缴费项目管理按钮
    item_btn = (By.XPATH, "/html[1]/body[1]/div[2]//div[1]/button[1]")
    # 操作列更多下的报税单位管理按钮
    tax_unit_btn = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/button[2]/span[1]")

# =====================新增非税局页面=======================
    # 新增非税局页面的平台类型
    type_name = (By.XPATH, "//input[@placeholder='请选择平台类型']")
    # 下拉框选择“湖南非税局”
    select_value = (By.XPATH, "//span[text()='湖南非税']")
    # 新增非税局页面平台名称
    terrace_name = (By.XPATH, "//input[@placeholder='请选择平台名']")
    # 下拉框选择“农行重庆分行”
    select_value2 = (By.XPATH, "//span[text()='农行重庆分行']")
    # 区域名文本框
    realm_name = (By.XPATH, "(//input[@type='text'])[3]")
    # 区域编号
    realm_code = (By.XPATH, "(//input[@type='text'])[4]")
    # 平台公钥
    public_key = (By.XPATH, "(//input[@type='text'])[5]")
    # 接口地址
    public_address = (By.XPATH, "(//input[@type='text'])[6]")
    # 平台查询token
    token1 = (By.XPATH, "(//input[@type='text'])[7]")
    # 机构名称
    institution_name = (By.XPATH, "(//input[@type='text'])[8]")
    # 所属银行
    bank = (By.XPATH, "//div[@class='el-input el-input--suffix']//input[@placeholder='全部']")
    # 下拉框选择银行
    bank_name = (By.XPATH, "//ul//li//span[text()='{}']")
    # 平台私钥
    private_key = (By.XPATH, "(//input[@type='text'])[14]")
    # 平台token
    token2 = (By.XPATH, "(//input[@type='text'])[15]")
    # 提交按钮
    submit_btn = (By.XPATH, "//span[text()='提交']")

# =========================非税局项目code管理页面======================
    # 新增项目code按钮
    add_code_btn = (By.XPATH, "//span[contains(text(),'code')]")
    # 列表第一行项目名称
    item_name = (By.XPATH, "(//div[@class='cell'])[8]")
    # 列表第一行操作列删除按钮
    del_btn = (By.XPATH, "//tbody//tr[1]//button//span[text()='删除']")
    # 删除确定按钮
    del_sure_btn = (By.XPATH, "//span[contains(text(),'确定')]")
    # 删除成功提示
    del_tip = (By.XPATH, "//p[@class='el-message__content']")

# ========================新增非税局项目code页面=======================
    # 项目名称文本框
    input_item = (By.XPATH, "//label[@for='name']/following-sibling::div//input")
    # 项目编码文本框
    input_item_code = (By.XPATH, "//label[@for='code']/following-sibling::div//input")
    # 内部编码文本框
    input_inner_code = (By.XPATH, "//label[@for='innerCode']/following-sibling::div//input")
    # 缴费上限金额文本框
    input_max_price = (By.XPATH, "//label[@for='maxLimitPrice']/following-sibling::div//input")
    # 缴费最低金额文本框
    input_min_price = (By.XPATH, "//label[@for='minLimitPrice']/following-sibling::div//input")
    # 计量单位文本框
    input_count_uint = (By.XPATH, "//label[@for='countUint']/following-sibling::div//input")
    # 提交按钮
    inner_submit_btn = (By.XPATH, "//button[@class='el-button el-button--primary el-button--small']")

# ==========================报税单位管理页面===========================
    # 新增报税单位按钮
    add_tax_unit_btn = (By.XPATH, "//span[text()='新增报税单位']")
    # 列表第一行项目名称
    tax_unit_name = (By.XPATH, "(//div[contains(@class,'cell')])[8]")
    # 列表第一行操作列删除按钮
    tax_unit_del_btn = (By.XPATH, "(//span[contains(.,'删除')])[1]")
    # 删除确定按钮
    tax_unit_del_sure_btn = (By.XPATH, "//span[contains(text(),'确定')]")
    # 删除成功提示
    tax_unit_del_tip = (By.XPATH, "//p[@class='el-message__content']")

# =========================新增报税单位页面==============================
    # 缴费单位名文本框
    input_unit_name = (By.XPATH, "//label[@for='name']/following-sibling::div//input")
    # 缴费单位code文本框
    input_unit_code = (By.XPATH, "//label[@for='code']/following-sibling::div//input")
    # token文本框
    input_unit_instanceToken = (By.XPATH, "//label[@for='instanceToken']/following-sibling::div//input")
    # 查询token文本框
    input_unit_instanceQueryToken = (By.XPATH, "//label[@for='instanceQueryToken']/following-sibling::div//input")
    # token配套app文本框
    input_unit_instanceTokenApp = (By.XPATH, "//label[@for='instanceTokenApp']/following-sibling::div//input")
    # 查询token配套app文本框
    input_unit_instanceQueryApp = (By.XPATH, "//label[@for='instanceQueryApp']/following-sibling::div//input")
    # 提交按钮
    add_unit_submit_btn = (By.XPATH, "//span[text()='提交']")

