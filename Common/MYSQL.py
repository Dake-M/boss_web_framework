# -*- coding: utf-8 -*-
import pymysql
import random
import os
from Common.Conf import Config
from Common.DIR import CONFIGS_DIR


cf = Config(os.path.join(CONFIGS_DIR, "config.conf"))


class MySql:
    """
    数据库操作类
    """

    def __init__(self, user, pwd, database):
        """
        建立连接
        :param user:
        :param pwd:
        :param database:
        """
        # 建立连接
        self.conn = pymysql.connect(
            host=cf.get_value("db_msg", "host"),
            user=user,
            password=pwd,
            port=cf.get_int("db_msg", "port"),
            database=database,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        # 创建游标
        self.cursor = self.conn.cursor()

    def run_sql(self, sql, args=None, is_more=False):
        """
        sql执行
        :param sql: 需要传入的sql语句
        :param args: sql语句中需要传入的条件参数,以元组的形式传入
        :param is_more:查询到的数据是否为多条记录
        :return: 返回sql语句执行完成返回的结果（以字典的形式返回）
        """
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()  # 获取多条结果
        else:
            return self.cursor.fetchone()  # 获取一条结果

    def close(self):
        self.cursor.close()
        self.conn.close()


