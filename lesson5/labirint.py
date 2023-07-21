
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window() #сделать окно максимальным
# зайти на лабиринт
driver.get("https://www.labirint.ru")
sleep(5)

# найти книги по слову Python
search_input = driver.find_element(By.CSS_SELECTOR, "#search-field")# сохраняем ссылку на элемент
#search_input.send_keys("Python") #передать значение
#search_input.send_keys(Keys.RETURN) #нажать на клавишу Enter
#можно объединить
search_input.send_keys("Python", Keys.RETURN)

# собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product")
print(len(books))

# вывести в консоль информацию: название + автор + цена
for book in books:
    author = ''
    title = book.find_element(By.CSS_SELECTOR, "span.product-title").text
    price = book.find_element(By.CSS_SELECTOR, "span.price-val").text
    try: #попробуй выполнить
        author = book.find_element(By.CSS_SELECTOR, "div.product-author").text
    except: #если не получится, то 
        author = "Автор не указан"
    print(author + "\t" + title + "\t" + price)

