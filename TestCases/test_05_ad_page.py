# -*- coding: utf-8 -*-
import pytest
from TestDatas import ad_page_datas as ad


class TestAd:
    """
    广告管理
    """
    @pytest.mark.usefixtures("init_ad_manage")
    def test01_title_name(self, init_ad_manage):
        """
        网页标题校验
        :return:
        """
        try:
            assert init_ad_manage.get_title() == "广告管理"
            assert "广告管理" in init_ad_manage.get_info_title()
        except Exception as e:
            raise e

    @pytest.mark.usefixtures("init_search_ad")
    def test02_search_ad(self, init_search_ad):
        """
        广告名称搜索
        :return:
        """
        init_search_ad[0].search_ad(ad.api_ad_name)
        try:
            assert ad.api_ad_name in init_search_ad[0].get_ad_name()
            assert init_search_ad[0].get_status() == "el-switch"
        except Exception as e:
            raise e

    @pytest.mark.usefixtures("init_ad_manage")
    def test03_add_ad(self, init_ad_manage):
        """
        新增广告
        :return:
        """
        init_ad_manage.add_ad(ad.ad_name, ad.start_time, ad.end_time, ad.path, ad.url, ad.group_name)
        try:
            assert init_ad_manage.get_ad_name() == ad.ad_name
        except Exception as e:
            raise e

    @pytest.mark.usefixtures("init_del_ad")
    def test04_del_ad(self, init_del_ad):
        """
        删除广告
        :return:
        """
        init_del_ad.del_ad()
        try:
            assert init_del_ad.get_ad_name() != ad.api_ad_name
        except Exception as e:
            raise e


if __name__ == '__main__':
    pytest.main()


