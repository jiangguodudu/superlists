from selenium import webdriver


# test Django with selenium
driver = webdriver.Chrome()

# 这里有一个很好的在线代办事项应用
# 去看这个应用的首页
driver.get("http://localhost:8000")

# 首页的标题和头应该都包含“To-Do”
assert 'To-Do' in driver.title

# 输入一个待办事项


# 文本框输入 “Buy peacock feathers”


# 按下回车键，页面更新
# 待办事项表格中显示“1：Buy peacock feathers”


# 页面中又显示了一个文本框，可以输入其他的待办事项
# 输入“Use peacock feathers to make a fly”


# 页面再次更新，他的清单中显示了两个待办事项


# 网站是否会记住输入的清单
# 网站为我们生成了一个唯一的URL
# 而且页面中有一些文字解说这个功能


# 再次访问哪个URL，发现待办事项列表还在


# 关闭浏览器，测试结束
driver.quit()






















