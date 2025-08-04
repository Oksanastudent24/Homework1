from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

print("[Активация программы]")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login")
print("Открыт ресурс: https://the-internet.herokuapp.com/login")

user_name = driver.find_element(By.NAME, "username")
print("[Элемент найден]")
sleep(3)

user_name.send_keys("tomsmith")
print("[Логин введен]")
sleep(3)

password = driver.find_element(By.NAME, "password")
print("[Элемент найден]")
sleep(3)

password.send_keys("SuperSecretPassword!")
print("[Пароль введен]")
sleep(3)

button = driver.find_element(By.CSS_SELECTOR, "button.radius")
print("[Элемент найден]")
sleep(3)

button.click()
print("[Произошо нажатие на кнопку]")
sleep(3)

succes_text = driver.find_element(By.CSS_SELECTOR, "#flash")
print("[Элемент найден]")
sleep(3)

print(succes_text.text)
sleep(3)

driver.quit()
print("Конец программы")