# Librerias que estamos usando

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mongo import MongoConnection


driver = webdriver.Chrome()

# URL del sitio web
url = "https://www.airbnb.com.ec/"

# Abrir la página
driver.get(url)

try:
    # Esperar a que la página se cargue, se configura 10 segundos
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='title_']"))
    )

    # Conexión a MongoDB
    db_client = MongoConnection().client
    db = db_client.get_database('airbnb')
    col = db.get_collection('sites')

    # Encontrar los títulos
    title_elements = driver.find_elements(By.CSS_SELECTOR, "div[id^='title_']")

    # Extraer las distancias
    distance_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='listing-card-subtitle'] span span")

    # Extraer las fechas
    date_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='listing-card-subtitle'] span span")

    # Extraer los valores
    price_elements = driver.find_elements(By.CSS_SELECTOR, "div.pquyp1l span._14y1gc ._tyxjp1")

    # Extraer las calificaciones del sitio
    rating_elements = driver.find_elements(By.CSS_SELECTOR, "span.t1a9j9y7.r4a59j5")

    # Almacenar títulos, distancias, fechas, valores y calificaciones en la base de datos
    for title_element, distance_element, date_element, price_element, rating_element in zip(title_elements, distance_elements, date_elements, price_elements, rating_elements):
        title = title_element.text
        distance = distance_element.text
        date = date_element.text
        price = price_element.text
        rating_text = rating_element.text

        # Crear un datos para MongoDB
        document = {
            "title": title,
            "distance": distance,
            "date": date,
            "price": price,
            "rating": rating_text
        }

        # Insertar el documento en la colección de MongoDB
        col.insert_one(document)

        # Imprimir título, distancia, fecha, valor y calificación
        print("Título:", title)
        print("Distancia:", distance)
        print("Fechas:", date)
        print("Valor:", price)
        print("Calificación promedio:", rating_text, "de 5")
        print("=" * 40)

except Exception as e:
    print("Error:", str(e))

finally:

    driver.quit()
