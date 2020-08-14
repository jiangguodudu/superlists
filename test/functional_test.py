from selenium import webdriver


# test Django with selenium
driver = webdriver.Chrome()
driver.get("http://localhost:8000")

assert "Django" in driver.title
