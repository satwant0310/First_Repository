from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
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
name.send_keys("Enter email")
pwrd = driver.find_element_by_id("pass")
pwrd.send_keys("Enter password")
driver.find_element_by_id("loginbutton").click()
time.sleep(2)
driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
############################## CODE TO ENTER IN SEARCH BAR ##########################
#search_bar = driver.find_element_by_name("q")
#search_bar.send_keys("Search")
#search_bar.send_keys(Keys.ENTER)
#####################################################################################
lst =[list of people]
for i in lst:
    # driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
    link = driver.get(i)
    time.sleep(2)
    driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
    time.sleep(2)
    driver.find_element_by_xpath("//*[@class='_42ft _4jy0 _4jy4 _517h _51sy']").click()
    time.sleep(8)
    content = driver.find_elements_by_xpath("//div[@class='_1mf _1mj']")
    content[1].send_keys('Hello this is an automated message please ignore')
    content[1].send_keys(Keys.ENTER)
    time.sleep(2)
driver.close()
