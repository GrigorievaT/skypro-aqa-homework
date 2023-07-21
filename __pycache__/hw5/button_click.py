from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window() #сделать окно максимальным
# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(5)

# Пять раз кликните на кнопку `Add Element`
search_button = driver.find_element(By.CSS_SELECTOR, "[onclick='addElement()']")# сохраняем ссылку на элемент
for i in range(0, 5):
    search_button.send_keys(Keys.RETURN)
sleep(5)

# Соберите со страницы список кнопок `Delete`
button = driver.find_elements(By.CSS_SELECTOR, "[onclick='deleteElement()']")

# Выведите на экран размер списка.
print(len(button))

driver_fox = webdriver.Firefox(service_fox=FirefoxService(FirefoxDriverManager().install()))
driver_fox.maximize_window() #сделать окно максимальным
# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/
driver_fox.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(5)