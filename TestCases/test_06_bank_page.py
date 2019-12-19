# -*- coding: utf-8 -*-
import pytest
from TestDatas import bank_page_datas as bpd


@pytest.mark.usefixtures("init_bank_page")
class TestBank:
    """
    银行管理页面
    """
    # @pytest.mark.usefixtures("init_bank_page")
    def test01_title_name(self, init_bank_page):
        """
        网页标题校验
        :return:
        """
        try:
            assert init_bank_page.get_title() == "银行管理"
            assert "银行管理" in init_bank_page.get_info_title()
        except Exception as e:
            raise e

    # @pytest.mark.usefixtures("init_add_bank_page")
    def test02_add_bank(self, init_bank_page):
        """
        正常添加一级银行
        :return:
        """
        init_bank_page.add_bank(bpd.bank_name, bpd.organization_code)
        try:
            assert "新增成功" in init_bank_page.get_add_tip()
            assert init_bank_page.get_bank_name() == bpd.bank_name
            assert init_bank_page.get_organization_code() == bpd.organization_code
        except Exception as e:
            raise e

    # @pytest.mark.usefixtures("init_add_bank_page")
    def test03_enter_organization(self, init_bank_page):
        """
        进入银行下级机构页面
        验证：
            机构名称
            机构代码
        :return:
        """
        a = init_bank_page.get_up_organization_code()
        try:
            assert a[0] == bpd.bank_name
            assert a[1] == bpd.organization_code
        except Exception as e:
            raise e

    # @pytest.mark.usefixtures("init_add_bank_page")
    def test04_add_organization_bank(self, init_bank_page):
        """
        正常添加下级银行
        :return:
        """
        init_bank_page.add_organization_bank(bpd.bank_name1, bpd.organization_code1, bpd.province_code)
        try:
            assert "新增成功" in init_bank_page.get_add_tip()
            assert init_bank_page.get_bank_name() == bpd.bank_name1
            assert init_bank_page.get_organization_code() == bpd.organization_code1
        except Exception as e:
            raise e

    # @pytest.mark.usefixtures("init_add_bank_page")
    def test05_del_organization_bank(self, init_bank_page):
        """
        删除下级机构银行
        :param init_bank_page:
        :return:
        """
        init_bank_page.del_organization_bank()
        try:
            assert "删除成功" in init_bank_page.get_del_tip()
            assert (init_bank_page.get_bank_name() != bpd.bank_name1) or \
                   (init_bank_page.get_bank_name() == False)
        except Exception as e:
            raise e

    # @pytest.mark.usefixtures("init_add_bank_page")
    def test06_del_bank(self, init_bank_page):
        """
        正常删除一级银行
        :return:
        """
        # 直接调用bank_page中的删除银行业务
        init_bank_page.del_bank()
        try:
            assert "删除成功" in init_bank_page.get_del_tip()
            assert (init_bank_page.get_bank_name() != bpd.bank_name) or \
                   (init_bank_page.get_bank_name() == False)
        except Exception as e:
            raise e


if __name__ == '__main__':
    pytest.main()