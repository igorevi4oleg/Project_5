from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/")

product_element = driver.find_element(By.XPATH, "//p[text()='Соус традиционный галактический']")

# Получаем координаты элемента до клика
before_click_position = product_element.location
print(f"Координаты до клика: {before_click_position}")

# Выполняем клик по элементу
driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'] //span[text()='Соусы']").click()

# Подождем немного, чтобы прокрутка произошла.
time.sleep(2)

# Выполняем клик по элементу
driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Начинки']").click()

# Подождем немного, чтобы прокрутка произошла
time.sleep(2)


# Получаем координаты элемента после клика

after_click_position = product_element.location
print(f"Координаты после клика: {after_click_position}")

# Проверка, что локация элемента поменялась
assert before_click_position != after_click_position


driver.quit()