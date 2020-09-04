from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.headless = True

driver = webdriver.Chrome(options=chrome_options)
start_url = "https://www.rightmove.co.uk/"
driver.get(start_url)
search_box = driver.find_element_by_xpath("//input[@id='searchLocation']")
search_box.send_keys("SE21 8BD")
driver.find_element_by_xpath("//button[@id='buy']").click()
time.sleep(5)
driver.find_element_by_xpath("//button[@id='submit']").click()
time.sleep(5)
expected_url = driver.current_url
print(expected_url)
pattern = "POSTCODE%(.+?)&"
post_code = re.search(pattern, expected_url)
print(post_code)

post_code = re.findall(r"POSTCODE%(.+?)&", expected_url)
print(post_code)
# print(driver.page_source.encode("utf-8"))
driver.quit()
