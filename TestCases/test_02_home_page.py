# -*- coding: utf-8 -*-
import pytest
from TestDatas import home_page_datas as hpd


@pytest.mark.demo
@pytest.mark.usefixtures("init_driver")
class TestHome:
    """
    首页
    """
    def test01_pay_data(self, init_driver):
        """
        收费数据
        :return:
        """
        try:
            assert init_driver[1].get_img_names1() == hpd.content_top1
        except Exception as e:
            raise e

    def test02_merchant_data(self, init_driver):
        """
        商户数据
        :param init_driver:
        :return:
        """

        try:
            assert init_driver[1].get_img_names2() == hpd.content_top2
        except Exception as e:
            raise e

    def test03_quit_login(self, init_driver):
        """
        退出登录
        :return:
        """
        init_driver[1].quit_login()

        try:
            assert init_driver[2].get_title() == "登录"
        except Exception as e:
            raise e


if __name__ == '__main__':
    pytest.main()






