# -*- coding: utf-8 -*-
import requests
import warnings


class ApiFunction:
    """
    web自动化前置条件直接调用接口实现的封装
    """
    def __init__(self):
        warnings.filterwarnings("ignore")
        url = "https://payexp.snsshop.net/boss/login/do"
        data = {"username": "13266816551", "password": "123456"}
        self.s = requests.Session()  # 创建session会话
        res = self.s.post(url, data, verify=False)
        # res_json = res.json()
        self.login_key = res.json()["data"]["loginKey"]
        # self.headers = {"login-key": self.login_key}

    def add_bank(self):
        """
        新增银行
        :return:
        """
        url = "https://payexp.snsshop.net/boss/bank-info/create"
        data = {
            "name": "dake_test",
            "bankNo": "dake001",
            "pid": 0
        }
        headers = {"login-key": self.login_key}
        res = self.s.post(url, json=data, headers=headers, verify=False)
        res_json = res.json()
        bank_name = res_json["data"]["name"]
        bank_id = res_json["data"]["id"]
        return bank_name, bank_id

    def del_bank(self, bank_id):
        """
        删除银行
        :return:
        """
        url = "https://payexp.snsshop.net/boss/bank-info/del"
        data = {"id": bank_id}
        headers = {"login-key": self.login_key}
        self.s.post(url, json=data, headers=headers, verify=False)

    def api_add_tax_manage(self):
        """
        添加非税局
        :return:
        """
        url = "https://payexp.snsshop.net/boss/tax_platform/create"
        data = {
            "type": "hunan",
            "platformName": "rongchang",
            "apartmentName": "dake11",
            "areaNo": "0011",
            "platformToken": "dake0011",
            "platformPrefix": "dake0011",
            "platformQueryToken": "dake0011",
            "agentName": "dakenametest",
            "invoiceToken": "1",
            "invoiceTokenApp": "1",
            "bankInfoId": 1
        }
        headers = {"login-key": self.login_key}
        res = self.s.post(url, json=data, headers=headers, verify=False)
        return res.json()["data"]["agentName"], res.json()["data"]["id"]

    def api_del_tax_manage(self, agent_id):
        """
        删除非税局
        :param agent_id:
        :return:
        """
        url = "https://payexp.snsshop.net/boss/tax_platform/delete"
        data = {"id": agent_id}
        headers = {"login-key": self.login_key}
        self.s.post(url, json=data, headers=headers, verify=False)

    def api_add_tax_code(self, agent_id):
        """
        添加非税局项目code
        :return:
        """
        url = "https://payexp.snsshop.net/boss/tax_platform_project_code/create"
        data = {
            "name": "2",
            "code": "2",
            "innerCode": "2",
            "maxLimitPrice": 200,
            "minLimitPrice": 0,
            "countUint": "2",
            "taxPlatformId": agent_id
        }
        headers = {"login-key": self.login_key}
        self.s.post(url, json=data, headers=headers, verify=False)

    def api_add_tax_unit(self, agent_id):
        """
        添加报税单位
        :return:
        """
        url = "https://payexp.snsshop.net/boss/tax_instance/create"
        data = {
            "name": "333",
            "code": "333",
            "instanceToken": "33",
            "instanceQueryToken": "33",
            "instanceTokenApp": "333",
            "instanceQueryApp": "333",
            "taxPlatformId": agent_id
        }
        headers = {"login-key": self.login_key}
        self.s.post(url, json=data, headers=headers, verify=False)

    def api_add_gui_module(self):
        """
        添加指引模块
        :return:
        """
        url = "https://payexp.snsshop.net/boss/guide_module/create"
        data = {
            "name": "dakename",
            "sort": 1
        }
        headers = {"login-key": self.login_key}
        res = self.s.post(url, json=data, headers=headers, verify=False)
        return res.json()["data"]["id"], res.json()["data"]["name"], res.json()["data"]["sort"]

    def api_del_gui_module(self, gui_module_id, gui_module_sort):
        """
        删除指引模块
        :return:
        """
        url = "https://payexp.snsshop.net/boss/guide_module/update"
        data = {"id": gui_module_id, "deleted": 1, "sort": gui_module_sort}
        headers = {"login-key": self.login_key}
        res = self.s.post(url, json=data, headers=headers, verify=False)
        print(res)

    def api_add_gui_item(self, gui_module_id):
        """
        新增指引项
        :return:
        """
        url = "https://payexp.snsshop.net/boss/guide_module_item/create"
        data = {
            "guideModuleId": gui_module_id,
            "guideName": "1",
            "article": "1",
            "sort": 1
        }
        headers = {"login-key": self.login_key}
        self.s.post(url, json=data, headers=headers, verify=False)

    def api_add_ad(self, name):
        """
        新增广告
        :return:
        """
        url = "https://payexp.snsshop.net/boss/ad/create"
        data = {
            "title":  name,
            "imgUrl": "https://imgcache.vikduo.com/oss/bc5d55a67a251d6c4e4155d6ad33f142.jpg",
            "adUrl": "https://www.hao123.com/",
            "merchantIds": [14],
            "startTime": 1573660800,
            "endTime": 1574438400,
            "status": 2
        }
        headers = {"login-key": self.login_key}
        res = self.s.post(url, json=data, headers=headers, verify=False)
        print(res.json())

    def api_del_ad(self, ad_id):
        """
        删除广告
        :param ad_id:
        :return:
        """
        url = "https://payexp.snsshop.net/boss/ad/delete"
        data = {"id": ad_id}
        headers = {"login-key": self.login_key}
        res = self.s.post(url, json=data, headers=headers, verify=False)
        print(res.json())

    def api_add_bank(self, bank_name, bank_code, pid):
        """
        添加一级银行
        :return:
        """
        url = "https://payexp.snsshop.net/boss/bank-info/create"
        data = {"name": bank_name, "bankNo": bank_code, "pid": pid}
        headers = {"login-key": self.login_key}
        res = self.s.post(url, json=data, headers=headers, verify=False)
        return res.json()["data"]["id"], res.json()["data"]["name"]


if __name__ == '__main__':
    a = ApiFunction()
    aa = a.add_bank()
    print(aa)

