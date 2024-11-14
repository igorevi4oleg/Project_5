from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_exit_from_account(driver):

    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

    first_input = driver.find_element(By.XPATH, "(//input[@type='text'])")
    first_input.send_keys("Oleg_TemnikovGurduz_11_123@yandex.ru")

    # Находим третий инпут и передаем в него значение.
    second_input = driver.find_element(By.XPATH, "(//input[@type='password'])")
    second_input.send_keys("22859788Asd")

    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, 'a[href="/account"]').click()

    time.sleep(2)

    driver.find_element(By.XPATH, '//button[text()="Выход"]').click()

    time.sleep(2)

    current_url = driver.current_url
    assert current_url == "https://stellarburgers.nomoreparties.site/login"