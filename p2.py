# coding:utf-8
import time
from selenium import webdriver

print webdriver.__file__  # 打印出导入的路径

driver = webdriver.Chrome('.\chromedriver',
                          service_args=["--verbose",
                                        "--log-path=.\chromedriver.log"])

driver.get('http://xzfuli.cn/')
search_box = driver.find_element_by_id('url')
search_box.clear()
search_box.send_keys('http://t.cn/RflLBBV')
submitBtn = driver.find_element_by_id('post')
submitBtn.click()
time.sleep(5)

driver.get('http://xzfuli.cn/')
search_box = driver.find_element_by_id('url')
search_box.clear()
search_box.send_keys('http://t.cn/RfWucxF')
submitBtn = driver.find_element_by_id('post')
submitBtn.click()
time.sleep(5)

driver.get('http://xzfuli.cn/')
search_box = driver.find_element_by_id('url')
search_box.clear()
search_box.send_keys('http://t.cn/Rflhhl2')
submitBtn = driver.find_element_by_id('post')
submitBtn.click()
time.sleep(10)

driver.quit()
