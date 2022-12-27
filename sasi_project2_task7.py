from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time


class Sasi_project2_task7():

    def emergency_contacts(self):

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
        driver.find_element(By.XPATH, "//div[contains(text(),'Sasi Kiran')").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[text()='Emergency Contacts']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[@class='oxd-button oxd-button--medium oxd-button--text'])[1]").click()
        time.sleep(3)
        name = driver.find_element(By.XPATH, "//label[text()='Name']/following::div[1]/input")
        time.sleep(3)
        name.send_keys("A P Jaganathan")
        time.sleep(3)
        relation = driver.find_element(By.XPATH, "//label[text()='Relationship']/following::div[1]/input")
        time.sleep(3)
        relation.send_keys("Father")
        time.sleep(3)
        mobile = driver.find_element(By.XPATH, "//label[text()='Mobile']/following::div[1]/input")
        time.sleep(3)
        mobile.send_keys("9874563210")
        time.sleep(3)
        save = driver.find_element(By.XPATH, "//button[@type='submit']")
        save.click()
        time.sleep(3)


emergency = Sasi_project2_task7()
emergency.emergency_contacts()