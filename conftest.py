import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    # Инициализация WebDriver
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.maximize_window()

    # Код после yield выполнится после тестов
    yield driver

    time.sleep(5)
    # Закрытие WebDriver после выполнения теста
    driver.quit()