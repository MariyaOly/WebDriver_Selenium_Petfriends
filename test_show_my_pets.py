from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialise the web driver and set an implicit expectation
driver = webdriver.Chrome()
driver.implicitly_wait(10)


def test_show_my_pets():
    # Open the PetFriends login page
    driver.get("http://petfriends.skillfactory.ru/login")

    # In email
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys('momaroly@gmail.com')

    # In password
    password_input = driver.find_element(By.ID, 'pass')
    password_input.send_keys('1234567890')

    # Click on the account login button
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    # Check that we are on the user's home page
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


def test_show_pets_table():
    # Open the page with all the pets
    driver.get("http://petfriends.skillfactory.ru/all_pets")

    # Explicit waiting
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck')))


images = driver.find_elements(By.CSS_SELECTOR, 'div:nth-of-type(2) > div > div > img')
names = driver.find_elements(By.CSS_SELECTOR, 'div:nth-of-type(2) > h5')
descriptions = driver.find_elements(By.CSS_SELECTOR, 'div:nth-of-type(2) > p')

for i in range(len(names)):
    assert images[i].get_attribute('src') != ''
    assert names[i].text != ''
    assert descriptions[i].text != ''
    assert ', ' in descriptions[i].text
    parts = descriptions[i].text.split(", ")
    assert len(parts[0]) > 0
    assert len(parts[1]) > 0

#python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_show_my_pets.py


