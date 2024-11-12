from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/register")  # Переход на страницу регистрации

# Находим первый инпут и передаем в него значение
first_input = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
first_input.send_keys("Oleg Igorevi4")

# Находим второй инпут и передаем в него значение
second_input = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
second_input.send_keys("Oleg_TemnikovGurduz_11_123@yandex.ru")

# Находим третий инпут и передаем в него значение
third_input = driver.find_element(By.XPATH, "(//input[@type='password'])")
third_input.send_keys("22859788Asd")

# Нажатие на кнопку регистрации.
driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

time.sleep(5)

assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

driver.quit()  # Закрываем браузер