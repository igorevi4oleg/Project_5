from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_from_main_page(driver):

    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

    first_input = driver.find_element(By.XPATH, "(//input[@type='text'])")
    first_input.send_keys("Oleg_TemnikovGurduz_11_123@yandex.ru")

    # Находим третий инпут и передаем в него значение
    second_input = driver.find_element(By.XPATH, "(//input[@type='password'])")
    second_input.send_keys("22859788Asd")

    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    # Проверка, что пользователь вошел в систему.
    time.sleep(3)
    profile_button = driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")
    assert profile_button.is_displayed()
