from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time


class Sasi_project2_task13():

    def tax_exemptions(self):

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
        driver.find_element(By.XPATH, "//a[text()='Tax Exemptions']").click()
        time.sleep(3)
        action = ActionChains(driver)
        status1 = driver.find_element(By.XPATH, "(//label[text()='Status'])[1]/following::div[1]")
        ActionChains(driver).move_to_element(status1).click().perform()
        count1 = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Single']")
        ActionChains(driver).move_to_element(count1).click().perform()
        time.sleep(6)
        exemptions1 = driver.find_element(By.XPATH, "(//label[text()='Exemptions'])[1]/following::div[1]/input")
        exemptions1.send_keys("Nil")
        time.sleep(3)
        state = driver.find_element(By.XPATH, "//label[text()='State']/following::div[1]")
        ActionChains(driver).move_to_element(state).click().perform()
        count2 = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Texas']")
        ActionChains(driver).move_to_element(count2).click().perform()
        time.sleep(6)
        status2 = driver.find_element(By.XPATH, "(//label[text()='Status'])[2]/following::div[1]")
        ActionChains(driver).move_to_element(status2).click().perform()
        count3 = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Single']")
        ActionChains(driver).move_to_element(count3).click().perform()
        time.sleep(6)
        exemptions2 = driver.find_element(By.XPATH, "(//label[text()='Exemptions'])[2]/following::div[1]/input")
        exemptions2.send_keys("Nil")
        time.sleep(3)
        unemployment_state = driver.find_element(By.XPATH, "//label[text()='Unemployment State']/following::div[1]")
        ActionChains(driver).move_to_element(unemployment_state).click().perform()
        count4 = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Utah']")
        ActionChains(driver).move_to_element(count4).click().perform()
        time.sleep(6)
        work_state = driver.find_element(By.XPATH, "//label[text()='Work State']/following::div[1]")
        ActionChains(driver).move_to_element(work_state).click().perform()
        count5 = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Texas']")
        ActionChains(driver).move_to_element(count5).click().perform()
        time.sleep(6)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)


tax = Sasi_project2_task13()
tax.tax_exemptions()