from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import Keys
import time


class Sasi_project2_task2():

    def page_headers(self):

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
        driver.find_element(By.XPATH, "//span[text()='Admin']").click()
        time.sleep(3)
        user_role = driver.find_element(By.XPATH, "//label[text()='User Role']/following::div[1]")
        action = ActionChains(driver)
        ActionChains(driver).move_to_element(user_role).click().perform()
        time.sleep(5)
        status = driver.find_element(By.XPATH, "//label[text()='Status']/following::div[1]")
        action = ActionChains(driver)
        ActionChains(driver).move_to_element(status).click().perform()
        time.sleep(5)

        driver.close()


pghd = Sasi_project2_task2()
pghd.page_headers()