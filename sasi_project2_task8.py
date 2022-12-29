from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time


class Sasi_project2_task8():

    def dependents(self):

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
        name.send_keys("Adhithya")
        time.sleep(3)
        relation = driver.find_element(By.XPATH, "//label[text()='Relationship']/following::div[1]")
        ActionChains(driver).move_to_element(relation).click().perform()
        select = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Child']")
        ActionChains(driver).move_to_element(select).click().perform()
        time.sleep(6)
        dob = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]")
        dob.send_keys("2019-12-03")
        time.sleep(3)
        save = driver.find_element(By.XPATH, "//button[@type='submit']")
        save.click()
        time.sleep(3)


depends = Sasi_project2_task8()
depends.dependents()
