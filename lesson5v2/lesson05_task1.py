from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print("[Активация программы]")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")
print("[Открыт ресурс: http://uitestingplayground.com/classattr]")
sleep(5)

button_blue = driver.find_element(By.CSS_SELECTOR, "button.class2")
print("[Элемент найден]")
sleep(5)

button_blue.click()
print("[Произошло нажатие кнопки]")
sleep(5)
print("[Конец программы]")
