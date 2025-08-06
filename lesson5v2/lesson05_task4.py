from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("[Активация программы]")
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login")
print("Открыт ресурс: https://the-internet.herokuapp.com/login")

user_name = driver.find_element(By.NAME, "username")
print("[Элемент найден]")

user_name.send_keys("tomsmith")
print("[Логин введен]")

password = driver.find_element(By.NAME, "password")
print("[Элемент найден]")

password.send_keys("SuperSecretPassword!")
print("[Пароль введен]")

button = driver.find_element(By.CSS_SELECTOR, "button.radius")
print("[Элемент найден]")

button.click()
print("[Произошло нажатие на кнопку]")
sleep(3)

succes_text = driver.find_element(By.CSS_SELECTOR, "#flash")
print("[Элемент найден]")

print(succes_text.text)
sleep(3)

driver.quit()
print("Конец программы")
