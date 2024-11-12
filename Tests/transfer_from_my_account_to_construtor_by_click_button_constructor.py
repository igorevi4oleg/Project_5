from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site")

driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

first_input = driver.find_element(By.XPATH, "(//input[@type='text'])")
first_input.send_keys("Oleg_TemnikovGurduz_11_123@yandex.ru")

# Находим третий инпут и передаем в него значение
second_input = driver.find_element(By.XPATH, "(//input[@type='password'])")
second_input.send_keys("22859788Asd")

driver.find_element(By.XPATH, "//button[text()='Войти']").click()

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, 'a[href="/account"]').click()

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, 'a[class="AppHeader_header__link__3D_hX"]').click()

# Проверка, что пользователь вошел в систему.
time.sleep(3)
current_url = driver.current_url
assert current_url == "https://stellarburgers.nomoreparties.site/"

driver.quit()