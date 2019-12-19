# -*- coding: utf-8 -*-
import os
import pytest
from selenium import webdriver
from Common.Conf import Config
from Common.DIR import CONFIGS_DIR
from Common.MYSQL import MySql
from TestDatas import Common_Data as cd
from TestDatas import ad_page_datas as apd
from TestDatas import bank_page_datas as bpd
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from PageObjects.non_tax_manage_page import NonTaxManagePage
from PageObjects.gui_manage_page import ShowManagePage
from PageObjects.ad_page import AdPage
from PageObjects.bank_page import BankPage
from PageLocators.home_page_locators import HomeLocs as hl

from Api.api_objects import ApiFunction

cf = Config(os.path.join(CONFIGS_DIR, "config.conf"))

# ========================================= BOSS =========================================


@pytest.fixture(scope="function")
def init_driver():
    driver = webdriver.Chrome()
    driver.get(cd.login_boss_url)
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.boss_login(cd.boss_user["user"], cd.boss_user["pwd"])
    hp = HomePage(driver)
    np = NonTaxManagePage(driver)

    yield driver, hp, lp, np

    driver.quit()


@pytest.fixture(scope="function")
def boss_login_driver():
    """
    登录BOSS的前置条件
    :return:
    """
    # 前置
    driver = webdriver.Chrome()
    driver.get(cd.login_boss_url)
    driver.maximize_window()
    lp = LoginPage(driver)

    # 分隔线 yield以上的为前置，yield以下的为后置
    yield driver, lp
    #
    # # 后置
    driver.quit()


@pytest.fixture(scope="function")
def non_tax_page1(init_driver):
    """
    非税局管理页面前置条件
    :return:
    """
    init_driver[1].click_element(hl.non_tax_menu, "点击非税局管理菜单")

    yield init_driver[3]


@pytest.fixture(scope="function")
def non_tax_page2(non_tax_page1):
    """
    添加非税局前置条件
    :return:
    """
    # af = ApiFunction()
    # bank_name, bank_id = af.add_bank()
    # driver = webdriver.Chrome()
    # driver.get(cd.login_boss_url)
    # driver.maximize_window()
    # lp = LoginPage(driver)
    # lp.boss_login(cd.boss_user["user"], cd.boss_user["pwd"])
    # hp = HomePage(driver)
    # hp.click_element(hl.non_tax_menu, "点击非税局管理菜单")
    # np = NonTaxManagePage(driver)

    yield non_tax_page1

    non_tax_page1.dele_tax_manage()
    # af = ApiFunction()
    # af.del_bank(bank_id)


@pytest.fixture(scope="function")
def non_tax_page3():
    """
    删除非税局前置条件
    :return:
    """
    af = ApiFunction()
    agent_name, agent_id = af.api_add_tax_manage()

    driver = webdriver.Chrome()
    driver.get(cd.login_boss_url)
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.boss_login(cd.boss_user["user"], cd.boss_user["pwd"])
    hp = HomePage(driver)
    hp.click_element(hl.non_tax_menu, "点击非税局管理菜单")
    np = NonTaxManagePage(driver)

    yield np, agent_name

    driver.quit()


@pytest.fixture(scope="function")
def add_tax_manage_code():
    """
    添加非税局项目code、新增报税单位前置条件
    :return:
    """
    af = ApiFunction()
    agent_name, agent_id = af.api_add_tax_manage()

    driver = webdriver.Chrome()
    driver.get(cd.login_boss_url)
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.boss_login(cd.boss_user["user"], cd.boss_user["pwd"])
    hp = HomePage(driver)
    hp.click_element(hl.non_tax_menu, "点击非税局管理菜单")
    np = NonTaxManagePage(driver)

    yield np, agent_name, agent_id

    af = ApiFunction()
    af.api_del_tax_manage(agent_id)
    driver.quit()


@pytest.fixture(scope="function")
def del_notax_magage_code():
    """
    删除非税局项目code前置条件
    :return: 
    """
    af = ApiFunction()
    agent_name, agent_id = af.api_add_tax_manage()
    af.api_add_tax_code(agent_id)
    driver = webdriver.Chrome()
    driver.get(cd.login_boss_url)
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.boss_login(cd.boss_user["user"], cd.boss_user["pwd"])
    hp = HomePage(driver)
    hp.click_element(hl.non_tax_menu, "点击非税局管理菜单")
    np = NonTaxManagePage(driver)

    yield np

    af = ApiFunction()
    af.api_del_tax_manage(agent_id)
    driver.quit()


@pytest.fixture(scope="function")
def del_tax_unit():
    """
    删除报税单位前置条件
    :return:
    """
    af = ApiFunction()
    agent_name, agent_id = af.api_add_tax_manage()
    af.api_add_tax_unit(agent_id)
    driver = webdriver.Chrome()
    driver.get(cd.login_boss_url)
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.boss_login(cd.boss_user["user"], cd.boss_user["pwd"])
    hp = HomePage(driver)
    hp.click_element(hl.non_tax_menu, "点击非税局管理菜单")
    np = NonTaxManagePage(driver)

    yield np

    af = ApiFunction()
    af.api_del_tax_manage(agent_id)
    driver.quit()


@pytest.fixture(scope="function")
def init_gui_manage():
    """
    指引模块前置后置
    :return:
    """
    af = ApiFunction()
    gui_module_id, gui_module_name, gui_module_sort = af.api_add_gui_module()
    af.api_add_gui_item(gui_module_id)

    driver = webdriver.Chrome()
    driver.get(cd.login_boss_url)
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.boss_login(cd.boss_user["user"], cd.boss_user["pwd"])
    hp = HomePage(driver)
    hp.click_element(hl.gui_menu, "点击指引管理菜单")
    sm = ShowManagePage(driver)

    yield sm, gui_module_id, gui_module_name, gui_module_sort

    af = ApiFunction()
    af.api_del_gui_module(gui_module_id, gui_module_sort)
    driver.quit()


@pytest.fixture(scope="function")
def init_ad_manage():
    driver = webdriver.Chrome()
    driver.get(cd.login_boss_url)
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.boss_login(cd.boss_user["user"], cd.boss_user["pwd"])
    hp = HomePage(driver)
    hp.click_element(hl.ad_menu, "点击广告管理菜单")
    ad = AdPage(driver)

    yield ad

    driver.quit()


@pytest.fixture(scope="class")
def init_add_ad_manage():
    """
    广告管理
    前置：新增广告
    后置：删除广告
    :return:
    """
    af = ApiFunction()
    af.api_add_ad(apd.api_ad_name)
    mysql = MySql(cf.get_value("db_msg", "user1"), cf.get_value("db_msg", "pwd1"), cf.get_value("db_msg", "database1"))
    result = mysql.run_sql(apd.sql1)
    ad_id = result["id"]

    yield ad_id,

    af = ApiFunction()
    af.api_del_ad(ad_id)


@pytest.fixture(scope="class")
def init_add_ad():
    """
    新增广告
    :return:
    """
    af = ApiFunction()
    af.api_add_ad(apd.api_ad_del_name)
    yield


@pytest.fixture(scope="function")
def init_search_ad(init_add_ad_manage, init_ad_manage):
    """
    搜索前置
    :return:
    """
    yield init_ad_manage, init_add_ad_manage


@pytest.fixture(scope="function")
def init_del_ad(init_add_ad, init_ad_manage):
    """
    删除广告前置后置
    前置：新增广告
    后置：退出浏览器
    :param init_add_ad:
    :param init_ad_manage:
    :return:
    """
    yield init_ad_manage


@pytest.fixture(scope="function")
def init_bank_page(init_driver):
    """
    银行
    :return:
    """
    init_driver[1].click_element(hl.bank_menu, "点击银行管理菜单")
    bp = BankPage(init_driver[0])

    yield bp


@pytest.fixture(scope="function")
def init_add_bank_page(init_bank_page):

    yield init_bank_page


# @pytest.fixture(scope="function")
# def init_organization():
#     af = ApiFunction()
#     af.api_add_bank(bpd.bank_name, bpd.organization_code)
#
#     driver = webdriver.Chrome()
#     driver.get(cd.login_boss_url)
#     driver.maximize_window()
#     lp = LoginPage(driver)
#     lp.boss_login(cd.boss_user["user"], cd.boss_user["pwd"])
#     hp = HomePage(driver)
#
#     yield driver, hp
#
#     driver.quit()

# ========================================= 运营商 =========================================
@pytest.fixture(scope="function")
def init_driver1():
    """
    登录运营商的前置条件
    :return:
    """
    # 前置
    driver = webdriver.Chrome()
    driver.get(cd.login_operator_url)
    driver.maximize_window()

    # 分隔线 yield以上的为前置，yield以下的为后置
    yield driver
    #
    # # 后置
    driver.quit()
