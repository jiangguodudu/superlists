#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : functional_tests_new
# @Author: Jiang Guo
# @Date  : 2020/8/15 0015
# @Desc  :
import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_can_start_a_list_and_retieve_it_later(self):
        # 打开应用首页
        self.driver.get("http://localhost:8000")

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

        table = self.driver.find_element_by_id("id_list_table")
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy a peacock feathers' for row in rows)
        )

        self.fail("finish the test!")


if __name__ == '__main__':
    unittest.main(warnings='ignore')