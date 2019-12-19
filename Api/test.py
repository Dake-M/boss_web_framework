# -*- coding: utf-8 -*-
import os
import random
import requests
import warnings


# path = r"G:"
# file = []
# for i in os.listdir(path):
#     aa = os.path.join(path, i)
#     if os.path.isfile(aa):
#         file.append(i)
#
# print(file)
# randnm = random.randint(0, file.__len__()-1)
# new_file = file[randnm]
# print(new_file)
#
# data = new_file
# url = "url"
# s = requests.Session()
# res = s.post(url, data, verify=False)

warnings.filterwarnings("ignore")
url = "https://payexp.snsshop.net/boss/login/do"
data = {"username": "13266816551", "password": "123456"}
s = requests.Session()  # 创建session会话
res = s.post(url, data, verify=False)
print(res)

url = "https://payexp.snsshop.net/boss/bank-info/create"
data = {"name": "dake_test", "bankNo": "dake001", "pid": 0}
res1 = requests.Session().post(url, data, verify=False)
res_json = res1.json()
print(res_json)
# bank_name = res_json["data"]["name"]
# bank_id = res_json["data"]["id"]
# return bank_name, bank_id


