from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()

EM_wait = WebDriverWait(driver, 10)

search_box = EM_wait.until(EC.visibility_of_element_located(("name", "q")))
search_box.send_keys("iphones")


search_button = EM_wait.until(EC.element_to_be_clickable(("xpath", "//button[@type='submit']")))
search_button.click()

mobile = EM_wait.until(EC.visibility_of_all_elements_located(("xpath", "//div[@class='KzDlHZ']")))
price = EM_wait.until(EC.visibility_of_all_elements_located(("xpath", "//div[@class='Nx9bqj _4b5DiR']")))
# print(moblie)
# print(price)

for mob, pri in zip(mobile, price):
    print(f"{mob.text} -- {pri.text}")

page_title=driver.title
print(page_title)
user_title="Iphones- Buy Products Online at Best Price in India - All Categories | Flipkart.com"
if page_title==user_title:
    print("welcome to FilpKart")
else:
    print("Please check the Url once")
driver.quit()
