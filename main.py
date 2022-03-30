from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#launching Chrome
P = Service("C:/BrowserDrivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=P)
driver.get("https://www.saucedemo.com/")

#maximize browser
driver.maximize_window()

#click and Type email
email=driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")

#click and type Password button
password=driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
time.sleep(3)

#click Log In button
login_button=driver.find_element(By.XPATH, "//input[@id='login-button']").click()
time.sleep(3)

#item name
item_name=driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")

for name in item_name:
    print(name.text)


#scroll down
scroll_down=driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
scroll_down.location_once_scrolled_into_view

#add to cart button
add_cart=driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
time.sleep(3)

#click cart icon
cart_icon=driver.find_element(By.XPATH, "//body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='header_container']/div[1]/div[3]/a[1]").click()
time.sleep(3)

#click continue shopping button
cont_shop=driver.find_element(By.XPATH, "//button[@id='continue-shopping']").click()
time.sleep(3)

#filter dropdown
filter=driver.find_element(By.XPATH, "//body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='header_container']/div[2]/div[2]/span[1]/select[1]").click()

#click low to high dropdown
low_high=driver.find_element(By.XPATH, "//option[contains(text(),'Price (low to high)')]").click()
time.sleep(3)

#click 2nd add to cart
add_cart2=driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
cart_icon=driver.find_element(By.XPATH, "//body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='header_container']/div[1]/div[3]/a[1]").click()
time.sleep(3)

#click checkout button
checkout=driver.find_element(By.XPATH, "//button[@id='checkout']").click()
time.sleep(3)

#input first name
first_name=driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Test first name")
time.sleep(3)

#input last name
last_name=driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Test last name")
time.sleep(3)

#input zip code
zip_code=driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("5690")
time.sleep(3)

#click continue button
cont_button=driver.find_element(By.XPATH, "//input[@id='continue']").click()
time.sleep(3)

#click finish button
finish_button=driver.find_element(By.XPATH, "//button[@id='finish']").click()
time.sleep(3)

#back to home button
back_home_button=driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
time.sleep(3)

#click side menu
side_menu=driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
#Click About menu
all_items=driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")

time.sleep(3)

driver.quit()



