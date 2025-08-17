from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    # Добавление товаров в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))

    # Нажимаем Checkout
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    # Заполнение формы вашими данными
    driver.find_element(By.ID, "first-name").send_keys("Оксана")
    driver.find_element(By.ID, "last-name").send_keys("Маричева")
    driver.find_element(By.ID, "postal-code").send_keys("142620")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    # Чтение итоговой стоимости
    total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    total_cost_value = float(total_cost.split("$")[1])

    # Проверка итоговой суммы
    assert total_cost_value == 58.29, f"Итоговая сумма должна быть 58.29, но получена {total_cost_value}"

    driver.quit()
