# -*- coding: utf-8 -*-
import pytest
from TestDatas import tax_manage_datas as tmd


@pytest.mark.demo
class TestNonTax:
    """
    非税局管理
    """

    @pytest.mark.usefixtures("non_tax_page1")
    def test01_title_name(self, non_tax_page1):
        """
        网页标题校验
        :return:
        """
        try:
            assert non_tax_page1.get_title() == "非税局管理"
            assert non_tax_page1.get_info_title() == "非税局管理"
        except Exception as e:
            raise e

    @pytest.mark.usefixtures("non_tax_page2")
    def test02_add_tax_manage(self, non_tax_page2):
        """
        添加非税局
        :param non_tax_page2:
        :return:
        """
        non_tax_page2.add_tax_manage(
            tmd.bank_name,
            tmd.add_data["realm_name"],
            tmd.add_data["realm_code"],
            tmd.add_data["public_key"],
            tmd.add_data["public_address"],
            tmd.add_data["token1"],
            tmd.add_data["institution_name"],
            tmd.add_data["private_key"],
            tmd.add_data["token2"]
        )
        try:
            assert non_tax_page2.get_realm_name() == tmd.add_data["institution_name"]
        except Exception as e:
            raise e

    @pytest.mark.usefixtures("non_tax_page3")
    def test03_del_tax_manage(self, non_tax_page3):
        """
        删除非税局
        :return:
        """
        non_tax_page3[0].dele_tax_manage()
        try:
            assert non_tax_page3[0].get_realm_name() != non_tax_page3[1]
        except Exception as e:
            raise e

    @pytest.mark.usefixtures("add_tax_manage_code")
    def test04_course_management_add_code(self, add_tax_manage_code):
        """
        添加非税局项目code
        :return:
        """
        add_tax_manage_code[0].add_tax_manage_code(
            tmd.add_tax_code["item_name"],
            tmd.add_tax_code["item_code"],
            tmd.add_tax_code["inner_code"],
            tmd.add_tax_code["max_price"],
            tmd.add_tax_code["min_price"],
            tmd.add_tax_code["count_uint"]
        )
        try:
            assert add_tax_manage_code[0].get_code_name_text() == tmd.add_tax_code["item_name"]
        except Exception as e:
            raise e

    @pytest.mark.usefixtures("del_notax_magage_code")
    def test05_course_management_del_code(self, del_notax_magage_code):
        """
        删除非税局项目code
        :return:
        """
        del_notax_magage_code.del_tax_manage_code()
        try:
            assert "删除成功!" in del_notax_magage_code.get_del_notax_code_tip_text()
        except Exception as e:
            raise e

    @pytest.mark.usefixtures("add_tax_manage_code")
    def test06_add_tax_unit(self, add_tax_manage_code):
        """
        非税局新增缴费单位
        :param add_tax_manage_code:
        :return:
        """
        add_tax_manage_code[0].add_tax_unit(
            tmd.add_unit["name"],
            tmd.add_unit["code"],
            tmd.add_unit["instanceToken"],
            tmd.add_unit["instanceQueryToken"],
            tmd.add_unit["instanceTokenApp"],
            tmd.add_unit["instanceQueryApp"]
        )
        try:
            assert add_tax_manage_code[0].get_tax_unit_name_tex() == tmd.add_unit["name"]
        except Exception as e:
            raise e

    @pytest.mark.usefixtures("del_tax_unit")
    def test07_del_tax_unit(self, del_tax_unit):
        """
        删除报税单位
        :return:
        """
        del_tax_unit.del_tax_unit()
        try:
            assert "删除成功!" in del_tax_unit.get_del_unit_tip()
        except Exception as e:
            raise e


if __name__ == '__main__':
    pytest.main()