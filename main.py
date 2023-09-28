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

    # Encontrar las distancias
    distance_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='listing-card-subtitle'] span span")

    # Mostrar títulos y distancias
    for title_element, distance_element in zip(title_elements, distance_elements):
        title = title_element.text
        distance = distance_element.text

        # Imprimir títulos y distancias
        print("Título:", title)
        print("Distancia:", distance)
        print("=" * 40)

except Exception as e:
    print("Error:", str(e))

finally:
    driver.quit()
