from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initializing the webdriver
driver = webdriver.Chrome()

# Launch the url
driver.get("https://automationexercise.com/")
time.sleep(1)
#close_popup = driver.find_element(By.CSS_SELECTOR,"#dismiss-button > div > svg").click()
driver.set_window_size(1000, 800)

# SigningUp
click_signup = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[4]/a").click()
input_name = driver.find_element(By.NAME,"name").send_keys("Charlie")
input_email = driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[3]").send_keys("charlip@mailinator.com")
click_signup = driver.find_element(By.CSS_SELECTOR,"#form > div > div > div:nth-child(3) > div > form > button").click()
# wait = WebDriverWait(driver, 10)
print("Enter your account information")

# Providing account information
select_title = driver.find_element(By.ID,"id_gender2").click()
input_password =driver.find_element(By.ID,"password").send_keys("1234567890")
select_day = driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/div[5]/div/div[1]/div/select/option[4]").click()
select_month = driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/div[5]/div/div[2]/div/select/option[4]").click()
select_year = driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/div[5]/div/div[3]/div/select/option[23]").click()
click_newsletter = driver.find_element(By.ID,"newsletter").click()
click_special = driver.find_element(By.ID, "optin").click()
print("Proceed to provide your address information")
input_Fname = driver.find_element(By.ID,"first_name").send_keys("Charlie")
input_Lname = driver.find_element(By.ID,"last_name").send_keys("Mendoza")
input_Company = driver.find_element(By.ID,"company").send_keys("Charlize Enterprise")
input_address = driver.find_element(By.ID,"address1").send_keys("Area D")
select_country = driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[6]/select/option[3]").click()
input_state = driver.find_element(By.ID,"state").send_keys("Indianapolis")
input_city = driver.find_element(By.ID,"city").send_keys("Memphis")
input_zipcode = driver.find_element(By.ID,"zipcode").send_keys("107642")
input_Mobile = driver.find_element(By.ID,"mobile_number").send_keys("+9767182741")
click_submit = driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/button").click()
print("Congratulations! Your new account has been successfully created!")
click_continue =driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/a").click


# Logout
click_logout = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[4]/a").click()
print("You have just logged out successfully, hope to see you again soon")

time.sleep(3)

# Close the driver
driver.quit()