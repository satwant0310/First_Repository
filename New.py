from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
import time

# option = Options()

# option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
# option.add_argument("--disable-extensions")

# # Pass the argument 1 to allow and 2 to block
# option.add_experimental_option("prefs", {
#     "profile.default_content_setting_values.notifications": 1
# })

driver = webdriver.Chrome("/Users/satwantsinghhanspal/Downloads/First_Repository/chromedriver")

driver.get("https://www.facebook.com")
name = driver.find_element_by_id("email")
name.send_keys("satwant011@gmail.com")
pwrd = driver.find_element_by_id("pass")
pwrd.send_keys("Ss@130712")
driver.find_element_by_id("loginbutton").click()
time.sleep(2)
driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
link = driver.get("https://www.facebook.com/shruti.batra.96")
time.sleep(2)
driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
driver.find_element_by_id("u_0_1k").click()
time.sleep(2)
content = driver.find_elements_by_xpath("//div[@class='_1mf _1mj']")
content[1].send_keys("Hello this is an automated message")
content[1].send_keys(Keys.RETURN)
# time.sleep(2)
# driver.close()
