from selenium import webdriver
import time

name = "Arjun Vaghela"
email = "avaghela@uw.edu"
tel = "123456789"
address = "124 anytown"
zip = "98044"
city = "Seattle"
state = "WA"
country = "USA"

number = "1111 1111 1111 1111"
expiration_month = "09"
expiration_year = "2023"
ccv = "123"

chromedriver_location = "chromedriver.exe"

driver = webdriver.Chrome(chromedriver_location)
driver.get("https://www.supremenewyork.com/shop/accessories/nq5hkuef2/mt26hz7la")

add_to_cart_button = '//*[@id="add-remove-buttons"]/input'
driver.find_element_by_xpath(add_to_cart_button).click()


time.sleep(2)

checkout_button = '//*@id="cart"]/a[2]'
driver.find_element_by_xpath(checkout_button).click()

print("Web Driver Run")