from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os
import re

clean_number = lambda num: re.sub(r"\s+", "", num)

def cargar_numeros(csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return [row[0].strip() for row in reader]

def iniciar_whatsapp(persistencia_dir="whatsapp_session"):
    if not os.path.exists(persistencia_dir):
        os.makedirs(persistencia_dir)

    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={os.path.abspath(persistencia_dir)}")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")
    return driver

def agregar_al_grupo(driver, numeros):
    input("\nPresiona Enter para continuar...")
    i=1
    for numero in numeros:
        try:
            campo_busqueda = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[class='x1rg5ohu xh8yej3 xt7dq6l x1nn3v0j x4uap5 x1120s5i xkhd6sd xdj266r x11i5rnm xat24cr x1mh8g0r x6prxxf x19v9tvf xzsf02u x16dsc37 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1a2a7pz copyable-text selectable-text']"))
            )
            campo_busqueda.clear()
            campo_busqueda.send_keys(numero)
            time.sleep(1)
            campo_busqueda.send_keys(Keys.ENTER)
            time.sleep(1)
        
            # resultado = driver.find_element(By.CSS_SELECTOR, "div[class='_ak8l']]")
            # resultado.click()
        
            print(f"{i}.Número {numero} agregado correctamente.")
            i+=1
        except Exception as e:
            print(f"Error al agregar {numero}: {e}")

if __name__ == "__main__":
    archivo_csv = "ONE_Column_Numbers.csv"
    numeros = cargar_numeros(archivo_csv)
    driver = iniciar_whatsapp()
    try:
        agregar_al_grupo(driver, numeros)
    finally:
        input("VERIFICATE...")
        driver.quit()
