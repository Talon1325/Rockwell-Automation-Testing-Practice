# Webdriver module provides all the Webdriver implementations (Firefox, Chrome, Remote)
from selenium import webdriver
# By module provides ability to locate elements in web browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://practicetestautomation.com/"
LOGIN_URL = BASE_URL + "practice-test-login/"

def test_login():
    # the instance of Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        print("Navigating")
        driver.get(LOGIN_URL) # navigate to login page
        print(driver.current_url)
        wait = WebDriverWait(driver, 10)

        # the find_element function locate by element attributes (By.ID locates element with 2nd parameter)
        username = wait.until(EC.presence_of_element_located((By.ID, "username")))      
        password = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "submit")

        # send_keys function send keys similar to using keyboard
        username.send_keys("student")
        password.send_keys("Password123")
        submit_button.click()

        # Saves a screenshot of web browser instance in a file
        driver.save_screenshot("Success.png")

        # Manual test of location of driver
        expected_url = wait.until(EC.url_to_be("https://practicetestautomation.com/logged-in-successfully/"))
        assert expected_url

        # Manual test of information on driver
        assert "Logged In Successfully" in driver.find_element(By.TAG_NAME, "h1").text

        old_url = driver.current_url
        logout_button = driver.find_element(By.LINK_TEXT, "Log out")
        logout_button.click()
        assert  old_url not in driver.current_url

    # If assert fails 
    except Exception as e:
        print(f"Test Failed! Error: {e}")

    # Always make sure to close session
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()