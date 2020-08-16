#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : functional_tests_new
# @Author: Jiang Guo
# @Date  : 2020/8/15 0015
# @Desc  :
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from django.test import LiveServerTestCase


class NewVistorTest(LiveServerTestCase):

    MAX_WAIT = 10

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def wait_for_row_in_list_table(self, row_text):
        """显式等待并校验"""
        start_time = time.time()
        while True:
            try:
                table = self.driver.find_element_by_id("id_list_table")
                rows = table.find_elements_by_tag_name("tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > NewVistorTest.MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retieve_it_later(self):
        # 打开应用首页
        self.driver.get(self.live_server_url)

        # 网页标题和头部都应包含"To-Do"
        self.assertIn("To-Do", self.driver.title)

        header_text = self.driver.find_element_by_tag_name("h1").text
        self.assertIn('To-Do', header_text)

        # 输入一个代办事项
        input_box = self.driver.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 输入"Buy a peacock feathers"
        input_box.send_keys("Buy a peacock feathers")

        # 按下回车键，页面更新
        # 待办事项列表显示“1: Buy a peacock feathers”
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)

        self.wait_for_row_in_list_table('1: Buy a peacock feathers')

        # 文本框再次输入其他待办事项
        # 输入"Use peacock feathers to make a fly"
        input_box = self.driver.find_element_by_id('id_new_item')
        input_box.send_keys("Use peacock feathers to make a fly")
        input_box.send_keys(Keys.ENTER)

        # 页面再次更新，清单中显示两个待办事项
        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")

        # self.fail("finish the test!")
