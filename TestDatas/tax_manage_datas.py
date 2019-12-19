# -*- coding: utf-8 -*-

# 新增非税局数据
bank_name = "中国农业银行"
add_data = {
    "realm_name": "tax_manage_name_test",
    "realm_code": "00001",
    "public_key": "8e30d40de736273f",
    "public_address": "http://10.100.100.78:8090/fslyxf/jkApi/api/nontaxChannelServer",
    "token1": "0c61cf65ab513cb8",
    "institution_name": "Dake非税局",
    "private_key": "11212",
    "token2": "222"
}
# 新增非税项目code
add_tax_code = {
    "item_name": "daketest01",
    "item_code": "dakecode",
    "inner_code": "dakeinnercode",
    "max_price": "99999",
    "min_price": "0",
    "count_uint": "rmb"
}

# 新增报税单位
add_unit = {
    "name": "daketest01",
    "code": "daketestcode01",
    "instanceToken": "daketesttoken01",
    "instanceQueryToken": "daketesttoken02",
    "instanceTokenApp": "daketestapp01",
    "instanceQueryApp": "daketestapp02"
}