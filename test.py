# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDatas import Common_Data as cd
from Common.BasePage import BasePage
import time
import pytest


# driver = webdriver.Chrome()
# driver.get("https://payexp.snsshop.net/merchant/login")
# driver.maximize_window()
# aa = driver.find_element(By.XPATH, "//img")
# print(aa.get_attribute("src"))
# aa.__setattr__("src", a)
# driver.find_element(By.XPATH, "//input[@placeholder='账号']").send_keys("16000000000")
# time.sleep(1)
# driver.find_element(By.XPATH, "//input[@placeholder='密码']").send_keys("16000000000")
# time.sleep(1)
# driver.find_element(By.XPATH, "//button[@type= 'button']").click()
#
#
# time.sleep(5)
# driver.quit()
@pytest.mark.usefixtures("init_driver1")
class TestLogin1:
    """
    登录
    """

    def test01_group_login_success(self, init_driver1):

        lp = LoginPage(init_driver1)
        lp.group_login(cd.operator_user["user"], cd.operator_user["pwd"])

        try:
            assert HomePage(init_driver1).get_title() == "首页"
        except Exception as e:
            raise e


if __name__ == '__main__':
    pytest.main()
