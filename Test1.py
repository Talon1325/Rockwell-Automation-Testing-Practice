from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://practicetestautomation.com/"
LOGIN_URL = BASE_URL + "practice-test-login/"

def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        print("Navigating")
        driver.get(LOGIN_URL)
        print(driver.current_url)

        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "submit")

        print(username, password)

        username.send_keys("student")
        password.send_keys("Password123")
        submit_button.click()

        driver.save_screenshot("Success.png")

        expected_url = "https://practicetestautomation.com/logged-in-successfully/"
        if expected_url == driver.current_url:
            print("Success")

        expected_text = "Logged In Successfully"
        if expected_text == driver.find_element(By.TAG_NAME, "h1").text:
            print("Success")


    except Exception as e:
        print(f"Test Failed! Error: {e}")

    # Always make sure to close session
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()