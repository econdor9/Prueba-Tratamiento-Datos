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
    # Encontrar  los títulos
    title_elements = driver.find_elements(By.CSS_SELECTOR, "div[id^='title_']")

    # Encontrar  las distancias
    distance_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='listing-card-subtitle'] span span")

    # Encontrar  las fechas
    date_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='listing-card-subtitle'] span span")

    # Encontrar los precios
    price_elements = driver.find_elements(By.CSS_SELECTOR, "div.pquyp1l span._14y1gc ._tyxjp1")

    # Mostrar títulos, distancias, fechas y precios
    for title_element, distance_element, date_element, price_element in zip(title_elements, distance_elements, date_elements, price_elements):
        title = title_element.text
        distance = distance_element.text
        date = date_element.text
        price = price_element.text

        # Imprimir título, distancia, fecha y precio
        print("Título:", title)
        print("Distancia:", distance)
        print("Fechas:", date)
        print("Precio:", price)
        print("=" * 40)

except Exception as e:
    print("Error:", str(e))

finally:
    # Cerrar el navegador
    driver.quit()
