from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window() #сделать окно максимальным
driver.get("https://ya.ru")
#driver.get("https://vk.com")
sleep(5)
driver.fullscreen_window() #перейти в полноэкранный режим
#driver.save_screenshot('./vk.png') #сохранить скриншот в текущую директорию с именем vk.png

#driver.back() #назад на страницу
#driver.forward() #вперед на страницу
#driver.refresh()  #обновить страницу

#driver.set_window_size(640, 480)  #изменить размер окна браузера


sleep(10)
