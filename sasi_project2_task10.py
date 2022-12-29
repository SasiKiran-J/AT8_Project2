from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time


class Sasi_project2_task10():

    def termination(self):

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
        driver.find_element(By.XPATH, "//a[text()='Job']").click()
        time.sleep(3)
        terminate_button = driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger --termination-button']")
        terminate_button.click()
        time.sleep(3)
        termin_date = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]")
        termin_date.send_keys("2023-01-03")
        time.sleep(3)
        termin_reason = driver.find_element(By.XPATH, "//label[text()='Termination Reason']/following::div[1]")
        ActionChains(driver).move_to_element(termin_reason).click().perform()
        select = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Laid-off']")
        ActionChains(driver).move_to_element(select).click().perform()
        time.sleep(6)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)


termin = Sasi_project2_task10()
termin.termination()
