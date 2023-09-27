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

try:
    # Encontrar los titulos
    title_elements = driver.find_elements(By.CSS_SELECTOR, "div[id^='title_']")

    # mostrar todos los títulos que se cargan en el sítio web
    for title_element in title_elements:
        print(title_element.text)

except Exception as e:
    print("Error:", str(e))

finally:
    driver.quit()
