from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time


class Sasi_project2_task6():

    def contact_details(self):

        driver = webdriver.Firefox()
        url1 = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url1)
        driver.maximize_window()
        time.sleep(3)
        username = driver.find_element(By.XPATH, "//input[@name='username']")
        username.send_keys("Admin")
        time.sleep(3)
        password = driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys("admin123")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[contains(text(),'Sasi Kiran')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[text()='Contact Details']").click()
        time.sleep(3)
        street1 = driver.find_element(By.XPATH, "//label[text()='Street 1']/following::div[1]/input")
        time.sleep(3)
        street1.send_keys("Address 1")
        time.sleep(3)
        street2 = driver.find_element(By.XPATH, "//label[text()='Street 2']/following::div[1]/input")
        time.sleep(3)
        street2.send_keys("Address 2")
        time.sleep(3)
        city = driver.find_element(By.XPATH, "//label[text()='City']/following::div[1]/input")
        time.sleep(3)
        city.send_keys("Atlantis")
        time.sleep(3)
        state = driver.find_element(By.XPATH, "//label[text()='State/Province']/following::div[1]/input")
        time.sleep(3)
        state.send_keys("Tamil Nadu")
        time.sleep(3)
        zip_code = driver.find_element(By.XPATH, "//label[text()='Zip/Postal Code']/following::div[1]/input")
        time.sleep(3)
        zip_code.send_keys("654987")
        time.sleep(3)
        country = driver.find_element(By.XPATH, "//label[text()='Country']/following::div[1]")
        ActionChains(driver).move_to_element(country).click().perform()
        count = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='India']")
        ActionChains(driver).move_to_element(count).click().perform()
        time.sleep(6)
        mobile = driver.find_element(By.XPATH, "//label[text()='Mobile']/following::div[1]/input")
        time.sleep(3)
        mobile.send_keys("9876543210")
        time.sleep(3)
        email = driver.find_element(By.XPATH, "//label[text()='Word Email']/following::div[1]/input")
        time.sleep(3)
        email.send_keys("sasi12@example.com")
        time.sleep(3)
        save = driver.find_element(By.XPATH, "//button[@type='submit']")
        save.click()
        time.sleep(3)


contact = Sasi_project2_task6()
contact.contact_details()