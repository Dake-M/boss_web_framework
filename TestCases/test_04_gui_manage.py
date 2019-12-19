# -*- coding: utf-8 -*-
import pytest
from TestDatas import gui_manage_datas as smd


@pytest.mark.usefixtures("init_gui_manage")
class TestShow:
    """
    指引管理
    """

    # @pytest.mark.usefixtures("init_gui_manage")
    def test01_title_name(self, init_gui_manage):
        """
        网页标题校验
        :return:
        """
        try:
            assert init_gui_manage[0].get_title() == "指引管理"
            assert "指引模块列表" in init_gui_manage[0].get_info_title()
        except Exception as e:
            raise e

    # @pytest.mark.usefixtures("init_gui_manage")
    def test02_add_show_module(self, init_gui_manage):
        """
        新增指引模块
        :return:
        """
        init_gui_manage[0].add_gui_module(smd.module_name, smd.path)
        try:
            assert init_gui_manage[0].get_module_name() == smd.module_name
        except Exception as e:
            raise e

    # @pytest.mark.usefixtures("init_gui_manage")
    def test03_del_gui_module(self, init_gui_manage):
        """
        删除指引模块
        :return:
        """
        init_gui_manage[0].del_gui_module()
        try:
            assert (init_gui_manage[0].get_module_name() != init_gui_manage[2]) or\
                   (init_gui_manage[0].get_module_name() == False)
        except Exception as e:
            raise e

    # @pytest.mark.usefixtures("init_gui_manage")
    def test04_add_gui_item(self, init_gui_manage):
        """
        新增指引项
        :return:
        """
        new_url = smd.url.format(init_gui_manage[1])
        init_gui_manage[0].add_show_item(new_url, smd.gui_data["gui_name"], smd.gui_data["gui_text"])
        try:
            assert init_gui_manage[0].get_gui_item_name() == smd.gui_data["gui_name"]
        except Exception as e:
            raise e

    # @pytest.mark.usefixtures("init_gui_manage")
    def test05_del_gui_item(self, init_gui_manage):
        """
        删除指引项
        :return:
        """
        new_url = smd.url.format(init_gui_manage[1])
        init_gui_manage[0].del_gui_item(new_url)
        try:
            assert (init_gui_manage[0].get_gui_item_name() != init_gui_manage[2]) or\
                   (init_gui_manage[0].get_gui_item_name() == False)
        except Exception as e:
            raise e


if __name__ == '__main__':
    pytest.main()




