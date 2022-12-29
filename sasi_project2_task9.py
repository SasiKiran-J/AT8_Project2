from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time


class Sasi_project2_task9():

    def employments(self):

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
        joined_date = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]")
        joined_date.send_keys("2023-1-03")
        time.sleep(3)
        job_title = driver.find_element(By.XPATH, "//label[text()='Job Title']/following::div[1]")
        ActionChains(driver).move_to_element(job_title).click().perform()
        select = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Chief Executive Officer']")
        ActionChains(driver).move_to_element(select).click().perform()
        time.sleep(6)
        job_category = driver.find_element(By.XPATH, "//label[text()='Job Category']/following::div[1]")
        ActionChains(driver).move_to_element(job_category).click().perform()
        select = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Officials and Managers']")
        ActionChains(driver).move_to_element(select).click().perform()
        time.sleep(6)
        sub_unit = driver.find_element(By.XPATH, "//label[text()='Sub Unit']/following::div[1]")
        ActionChains(driver).move_to_element(sub_unit).click().perform()
        select = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Development']")
        ActionChains(driver).move_to_element(select).click().perform()
        time.sleep(6)
        locations = driver.find_element(By.XPATH, "//label[text()='Location']/following::div[1]")
        ActionChains(driver).move_to_element(locations).click().perform()
        select = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Texas R&D']")
        ActionChains(driver).move_to_element(select).click().perform()
        time.sleep(6)
        employment = driver.find_element(By.XPATH, "//label[text()='Employment Status']/following::div[1]")
        ActionChains(driver).move_to_element(employment).click().perform()
        select = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Full-Time Permanent']")
        ActionChains(driver).move_to_element(select).click().perform()
        time.sleep(6)
        driver.find_element(By.XPATH,
                            "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
        time.sleep(3)
        start_date = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]")
        start_date.send_keys("2023-1-03")
        time.sleep(3)
        end_date = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[3]")
        end_date.send_keys("2027-12-30")
        time.sleep(3)


job = Sasi_project2_task9()
job.employments()