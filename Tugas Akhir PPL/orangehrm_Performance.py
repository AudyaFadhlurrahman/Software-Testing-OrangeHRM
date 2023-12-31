import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture()

def driver():
    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.maximize_window()
    yield driver
    driver.quit()

def test(driver):
    time.sleep(3)
    driver.find_element(By.NAME, 'username').send_keys('Admin')
    driver.find_element(By.NAME, 'password').send_keys('admin123' + Keys.ENTER)
    time.sleep(3)

    # Masuk_Menu_Performance 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]').click()
    time.sleep(3)

    # Masuk_Sub_Menu_Manage_Reviews    
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]').click()
    time.sleep(3)

    # Manage_Performance_Reviews_berdasarkan_rentang_waktu_yang_sesuai 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys('2022-01-01')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys('2023-12-31')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Manage_Performance_Reviews_berdasarkan_waktu_yang_salah 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys('2026-01-01')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys('2023-12-31')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Manage_Performance_Reviews_berdasarkan_waktu_yang_tidak_sesuai_format 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys('Test')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys('31-12-2023')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Menambah_Performance_Review_tanpa_input_apapun 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/button[3]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/button[1]').click()
    time.sleep(3)

    # Melihat_detail_Performance_Reviews 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[8]/div/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]').click()
    time.sleep(3)

    # Menghapus_Performance_Reviews 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[8]/div/button[1]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
    time.sleep(3)

    # Melihat_My_Performance_Trackers 
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]').click()
    time.sleep(3)