from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration_with_invalid_password(driver):# Переход на страницу регистрации

    # Находим первый инпут и передаем в него значение
    first_input = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
    first_input.send_keys("Oleg Igorevi4")

    # Находим второй инпут и передаем в него значение
    second_input = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
    second_input.send_keys("Oleg_TemnikovGurduz_11_123@yandex.ru")

    # Находим третий инпут и передаем в него значение некорректного пароля
    third_input = driver.find_element(By.XPATH, "(//input[@type='password'])")
    third_input.send_keys("2285")

    # Нажатие на кнопку регистрации.
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    time.sleep(3)

    div_element = driver.find_element(By.CSS_SELECTOR, ".input_status_error")

    # Проверяем, содержит ли элемент класс 'input_status_error'
    assert 'input_status_error' in div_element.get_attribute('class')



