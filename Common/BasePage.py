# -*- coding: utf-8 -*-
import os
import time
import random
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.DIR import SCREEN_DIR
from Common.LOG import Log

log = Log().get_logger()  # 日志实例化


class BasePage:
    """
    selenium常用关键字的二次封装
    在任何一个页面操作都可以事实捕获异常/输出操作日志/失败截图
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def web_refresh(self):
        """
        刷新页面
        :return:
        """
        self.driver.refresh()

    def enter_url(self, url):
        """
        进入指定url地址
        :return:
        """
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def switch_to_frame(self, loc, img_doc):
        """
        切换iframe
        :param loc:
        :param img_doc:
        :return:
        """
        ele = self.get_element(loc, img_doc)
        self.driver.switch_to.frame(ele)

    def switch_to_default(self):
        """
        切换iframe后返回主页面
        :return:
        """
        self.driver.switch_to.default_content()

    def click_move_mouse(self, loc1, img_doc1):
        """
        点击移动鼠标
        :return:
        """
        tab = ActionChains(self.driver)
        hua1 = self.get_element(loc1, img_doc1)  # 获取滑动按钮
        tab.click_and_hold(hua1).perform()
        tab.reset_actions()
        tab.move_by_offset(338, 0).perform()  # 使用随机数确定滑动位置后滑动
        # tab.move_to_element(hua1).release()  # 释放鼠标

    def move_mouse(self, loc, img_doc):
        """
        移动鼠标
        :param loc:
        :param img_doc:
        :return:
        """
        ele = self.get_element(loc, img_doc)
        ActionChains(self.driver).move_to_element(ele).perform()

    def wait_ele_visible(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        等待元素可见
        :param loc: 元素表达式（元组形式传入）
        :param img_doc: 截图说明
        :param timeout: 超时时间
        :param frequency: 每0.5s一次
        :return:
        """
        log.info("在{0}等待元素{1}可见。".format(img_doc, loc))
        start_time = time.time()
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            # 异常截图 -- 通过截图名称知道哪个页面哪个模块出错了
            self.save_screenshot(img_doc)
            # 异常日志捕获
            log.exception("等待元素可见失败！")
            # 抛出异常
            raise e
        else:
            end_time = time.time()
            log.info("等待时长为：{}".format(end_time - start_time))

    def if_text_in_element(self, loc, img_doc, text, timeout=20, frequency=0.5):
        """
        文本text是否在元素中存在
        :param loc:
        :param img_doc:
        :param timeout:
        :param frequency:
        :return: True or F
        """
        log.info("在{0}等待元素{1}可见。".format(img_doc, loc))
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.text_to_be_present_in_element(loc, text))
            return True
        except Exception:
            # 异常截图 -- 通过截图名称知道哪个页面哪个模块出错了
            self.save_screenshot(img_doc)
            # 异常日志捕获
            log.exception("元素不存在！")
            return False

    def if_ele_is_exist(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        元素是否存在
        :param loc:
        :param img_doc:
        :param timeout:
        :param frequency:
        :return:
        """
        log.info("在{0}等待元素{1}可见。".format(img_doc, loc))
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(loc))
            return True
        except Exception:
            # 异常截图 -- 通过截图名称知道哪个页面哪个模块出错了
            self.save_screenshot(img_doc)
            # 异常日志捕获
            log.exception("元素不存在！")
            return False

    def wait_page_contains_element(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        等待页面包含元素（元素存在）
        判断元素是否存在
        :return:
        """
        log.info("在{0}页面等待元素{1}存在。".format(img_doc, loc))
        start_time = time.time()
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(loc))
        except Exception as e:
            # 异常截图 -- 通过截图名称知道哪个页面哪个模块出错了
            self.save_screenshot(img_doc)
            # 异常日志捕获
            log.exception("元素不存在！")
            # 抛出异常
            raise e
        else:
            end_time = time.time()
            log.info("等待时长为：{}".format(end_time - start_time))

    def get_element(self, loc, img_doc):
        """
        查找元素
        :param loc: 元素表达式（元组形式传入）
        :param img_doc: 截图说明
        :return: 单个元素
        """
        log.info("在{0}查找元素{1}可见。".format(img_doc, loc))
        try:
            ele = WebDriverWait(self.driver, 15, 1).until(EC.presence_of_element_located(loc))
        except Exception as e:
            # 异常截图 -- 通过截图名称知道哪个页面哪个模块出错了
            self.save_screenshot(img_doc)
            # 异常日志捕获
            log.exception("查找失败！")
            # 抛出异常
            raise e
        else:
            return ele

    def get_elements(self, loc, img_doc):
        """
        与get_element一致
        :param loc: 元素表达式（元组形式传入）
        :param img_doc: 截图说明
        :return: 元素列表
        """
        log.info("在{0}查找元素s{1}可见。".format(img_doc, loc))
        try:
            eles = WebDriverWait(self.driver, 15, 1).until(EC.presence_of_all_elements_located(loc))
        except Exception as e:
            # 异常截图 -- 通过截图名称知道哪个页面哪个模块出错了
            self.save_screenshot(img_doc)
            # 异常日志捕获
            log.exception("查找失败！")
            # 抛出异常
            raise e
        else:
            return eles

    def click_element(self, loc, img_doc):
        """
        点击元素
        :param loc: 元素表达式（元组形式传入）
        :param img_doc: 截图说明
        :return:
        """
        # 要找到元素，元素可见
        ele = self.get_element(loc, img_doc)
        log.info("在{0}点击元素{1}。".format(img_doc, loc))
        try:
            ele.click()
        except Exception as e:
            # 异常日志捕获
            log.exception("元素点击失败")
            # 抛出异常
            raise e

    def input_text(self, text, loc, img_doc):
        """
        输入文本
        :return:
        """
        # 要找到元素，元素可见
        ele = self.get_element(loc, img_doc)
        log.info("在{0}对元素{1}输入信息{2}。".format(img_doc, loc, text))
        try:
            ele.send_keys(text)
        except Exception as e:
            # 异常日志捕获
            log.exception("输入击失败")
            # 抛出异常
            raise e

    def get_element_text(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        获取元素的文本值
        :param loc: 元素表达式（元组形式传入）
        :param img_doc: 截图说明
        :param timeout: 超时时间
        :param frequency: 没0.5s一次
        :return:
        """
        # 要找到元素
        self.wait_page_contains_element(loc, img_doc, timeout, frequency)
        ele = self.get_element(loc, img_doc)
        log.info("在{0}页面获取元素{1}的文本值。".format(img_doc, loc))
        try:
            text = ele.text
        except Exception as e:
            # 异常截图 -- 通过截图名称知道哪个页面哪个模块出错了
            self.save_screenshot(img_doc)
            # 异常日志捕获
            log.exception("获取元素文本值失败")
            # 抛出异常
            raise e
        else:
            log.info("获取到的元素文本内容为:{}".format(text))
            return text

    def get_element_attr(self, loc, sttr_name, img_doc, timeout=20, frequency=0.5):
        """
        获取元素的属性
        :param loc: 元素表达式（元组形式传入）
        :param img_doc: 截图说明
        :param timeout: 超时时间
        :param frequency: 没0.5s一次
        :return:
        """
        self.wait_page_contains_element(loc, img_doc, timeout, frequency)
        ele = self.get_element(loc, img_doc)
        log.info("在{0}页面获取元素{1}的属性{2}。".format(img_doc, loc, sttr_name))
        try:
            value = ele.get_attribute(sttr_name)
        except Exception as e:
            # 异常截图 -- 通过截图名称知道哪个页面哪个模块出错了
            self.save_screenshot(img_doc)
            # 异常日志捕获
            log.exception("获取元素属性值失败")
            # 抛出异常
            raise e
        else:
            log.info("获取到的元素属性值为:{}".format(value))
            return value

    def save_screenshot(self, img_doc):
        """
        保存截图
        :param img_doc: 截图说明
        :return:
        """
        t = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        filename = "{}_{}.png".format(t, img_doc)
        file = os.path.join(SCREEN_DIR, filename)
        self.driver.save_screenshot(file)
        log.info("截图文件保存在：{0}，文件名为{1}".format(SCREEN_DIR, filename))

    # def find_element(self, loc, img_doc, OVER_TIME=1):
    #     """
    #     这里添加了一个OVER_TIME作为查找元素的超时次数，根据系统的实际情况设置OVER_TIME的大小
    #     """
    #     for i in range(OVER_TIME):
    #         try:
    #             ele = self.driver.find_element(*loc)
    #         except Exception as e:
    #             # 异常截图 -- 通过截图名称知道哪个页面哪个模块出错了
    #             self.save_screenshot(img_doc)
    #             # 异常日志捕获
    #             logging.exception("查找失败！")
    #             # 抛出异常
    #             raise
    #         else:
    #             return ele

    def find_display_elements(self, loc, OVER_TIME):
        """
        查找状态为displayed的元素集合，当查找一类元素时，
        经常出现有些元素是不可见的情况，此函数屏蔽那些不可见的元素
         """
        for i in range(OVER_TIME):
            try:
                elements = self.driver.find_elements(*loc)
                num = elements.__len__()
            except Exception as e:
                print(e)
                time.sleep(1)
            if num >= 1:
                break

        display_element = []
        # 将可见的元素放到列表中， 并返回
        for j in range(num):
            element = elements.__getitem__(j)
            if element.is_displayed():
                display_element.append(element.text)
        return display_element

    # =============================== JS 操作封装==================================
    def js_execute(self, js, img_doc, *args):
        """执行js"""
        try:
            self.driver.execute_script(js, args)
        except Exception as e:
            # 异常截图 -- 通过截图名称知道哪个页面哪个模块出错了
            self.save_screenshot(img_doc)
            # 异常日志捕获
            log.exception("js执行失败")
            # 抛出异常
            raise e

    def js_execute1(self, js, img_doc):
        """执行js"""
        try:
            self.driver.execute_script(js)
        except Exception as e:
            # 异常截图 -- 通过截图名称知道哪个页面哪个模块出错了
            self.save_screenshot(img_doc)
            # 异常日志捕获
            log.exception("js执行失败")
            # 抛出异常
            raise e

    def js_fours_element(self, loc, img_doc):
        """聚焦元素"""
        element = self.get_element(loc, img_doc)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def js_scroll_top(self):
        """滑动到页面顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        """滑动到页面底部"""
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)

# if __name__ == '__main__':
#     from PageLocators.ad_locators import AdLocators as al
#     a = BasePage()
#     a.get_element_attr(al.status_btn, "class", "获取状态信息")
