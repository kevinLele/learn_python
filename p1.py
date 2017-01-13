# coding:utf-8
import time
from selenium import webdriver

print webdriver.__file__  # 打印出导入的路径

# print 0
driver = webdriver.Chrome('.\chromedriver',
                          service_args=["--verbose",
                                        "--log-path=.\chromedriver.log"])
# print 1
# driver.get('http://www.google.com/xhtml')
# time.sleep(5)  # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)  # Let the user actually see something!
# driver.quit()

driver.get('https://www.baidu.com')
search_box = driver.find_element_by_id('kw')
search_box.send_keys(u'测试')
submitBtn = driver.find_element_by_id('su')
submitBtn.click()
print driver.title
time.sleep(5)
driver.quit()
