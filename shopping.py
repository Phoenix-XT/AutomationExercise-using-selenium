from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

# initializing the webdriver
driver = webdriver.Chrome()

# Launch the url
driver.get("https://automationexercise.com/")
time.sleep(1)
#close_popup = driver.find_element(By.CSS_SELECTOR,"#dismiss-button > div > svg").click()
driver.set_window_size(1000, 800)

# SigningIn
click_signin = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[4]/a").click()
input_email = driver.find_element(By.NAME,"email").send_keys("charly@mailinator.com")
input_password = driver.find_element(By.NAME,"password").send_keys("1234567890")
click_login = driver.find_element(By.XPATH,"/html/body/section/div/div/div[1]/div/form/button").click()
# wait = WebDriverWait(driver, 10)
print("Welcome back! What would you like today")

# Viewing all products available in store

# Using explicit wait to ensure the product container elements are loaded
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div[1]")))

# Locating the elements containing products
product_containers = driver.find_elements(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div[1]/div")

# Loop through the product elements and print their names and prices, skipping index 0
for index, product in enumerate(product_containers, start=0):
    if index == 0:
        continue  # Skip the first product

    # Adjust the XPaths based on the structure of the web page
    name_xpath = "./div/div[1]/div[1]/p"
    price_xpath = "./div/div[1]/div[1]/h2"


    # Check if the product name and price elements exist
    product_name_elements = product.find_elements(By.XPATH, name_xpath)
    product_price_elements = product.find_elements(By.XPATH, price_xpath)

    if product_name_elements and product_price_elements:
        # Extracting product name and price
        product_name = product_name_elements[0].text
        product_price = product_price_elements[0].text

        # Printing product name and price
        print(f"Product {index}: Name: {product_name}, Price: {product_price}")
    else:
        # Printing message if elements are not found
        print(f"An error occurred while processing product {index}: {e}")

# Printing the assertive message
print("Here are our available products, please choose as many as you want")

# Adding the first product to the cart
wait = WebDriverWait(driver, 10)
add_to_cart_product1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a")))
add_to_cart_product1.click()

# Wait for the continue shopping button and click it
success_modal = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[3]/button")))
success_modal.click()

# Adding the second product to the cart
add_to_cart_button2 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div[1]/div[3]/div/div[1]/div[1]/a")))
add_to_cart_button2.click()

# Wait a few seconds for the product to be added to the cart
time.sleep(5)

print("Product has been successfully added to cart")

# Click on the view cart button
view_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[2]/p[2]/a/u")))
view_cart_button.click()

print("Now let's view what you have in your cart")
print("Now that we have seen your cart, lets check you out")

click_checkout = driver.find_element(By.XPATH,"/html/body/section/div/section/div[1]/div/div/a").click()
print("We are checking you out, please be a bit patient")

# Wait for the checkout page details page and review
checkout_page = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/section/div")))

send_message =driver.find_element(By.XPATH,"/html/body/section/div/div[6]/textarea").send_keys("Please be dilligent in your delivery")
click_placeorder = driver.find_element(By.XPATH,"/html/body/section/div/div[7]/a").click()

# Payment
print("Please provide your card details, to process your order")
wait = WebDriverWait(driver, 10)
input_bankname = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div[3]/div/div[2]/form/div[1]/div/input')))
input_bankname.send_keys("lucia Domingues")
send_cardnumber = driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[2]/div/input").send_keys("137873")
send_cvv = driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[3]/div[1]/input").send_keys("209")
send_month = driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[3]/div[2]/input").send_keys("June")
send_year = driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[3]/div[3]/input").send_keys("2009")
click_pay = driver.find_element(By.XPATH,"/html/body/section/div/div[3]/div/div[2]/form/div[5]/div/button").click()

print("Congratulations, your order has being placed")

print("Lets download your invoice")
download_receipt = driver.find_element(By.XPATH,"/html/body/section/div/div/div/a").click()
print("Here you go, kindly check your download files")

# Logout
click_logout = driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[4]/a").click()
print("You have just logged out successfully, hope to see you again soon")

# Close the driver after some time
time.sleep(5)

# Close the driver
driver.quit()
