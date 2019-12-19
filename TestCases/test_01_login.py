# -*- coding: utf-8 -*-
import pytest
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDatas import Common_Data as cd
from TestDatas import login_datas as ld


@pytest.mark.demo
@pytest.mark.usefixtures("boss_login_driver")
class TestLogin:
    """
    登录
    """
    def test01_boss_login_success(self, boss_login_driver):

        boss_login_driver[1].boss_login(cd.boss_user["user"], cd.boss_user["pwd"])

        try:
            assert HomePage(boss_login_driver[0]).get_title() == "首页"
        except Exception as e:
            raise e

    @pytest.mark.parametrize("data", ld.boss_unnomal_data1)
    def test02_boss_login_unnomal(self, data, boss_login_driver):
        """
        错误帐号或错误密码登录
        :return:
        """
        boss_login_driver[1].boss_login(data["user"], data["pwd"])

        try:
            assert data["check"] in boss_login_driver[1].get_tip1()
        except Exception as e:
            raise e

    @pytest.mark.parametrize("data", ld.boss_unnomal_data2)
    def test03_boss_login_unnomal(self, data, boss_login_driver):
        """
        帐号或密码为空异常登录
        :return:
        """
        boss_login_driver[1].boss_login(data["user"], data["pwd"])

        try:
            assert boss_login_driver[1].get_tip2() == data["check"]
        except Exception as e:
            raise e


if __name__ == '__main__':
    pytest.main()

