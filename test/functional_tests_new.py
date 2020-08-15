#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : functional_tests_new
# @Author: Jiang Guo
# @Date  : 2020/8/15 0015
# @Desc  :
import unittest
from selenium import webdriver


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
        self.fail("finish the test!")

        # 输入一个代办事项


if __name__ == '__main__':
    unittest.main(warnings='ignore')