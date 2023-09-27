# Librerias que estamos usando
from selenium import webdriver
from selenium.webdriver.common.by import By

# URL del sitio web
url = "https://www.airbnb.com.ec/"

driver = webdriver.Chrome()

# Abrir la página
driver.get(url)

# Esperar a que la página se cargue, se configura 10 segundos
driver.implicitly_wait(10)


title = driver.find_element(By.CSS_SELECTOR, "div[id^='title_']")

# Mostrar el texto del elemento encontrado
print(title.text)

driver.quit()