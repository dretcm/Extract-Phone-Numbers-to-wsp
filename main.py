import time
import re
import pandas as pd
import os
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


chromedriver_path = 'chromedriver.exe'
url = "https://web.whatsapp.com/"
file_name = "whatsapp_groups.xlsx"
group_name = ""


# verbosidad de TensorFlow:
# '0': Mostrar todos los logs (por defecto).
# '1': Mostrar solo advertencias y errores.
# '2': Mostrar solo errores.
# '3': Mostrar solo errores críticos.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# Configuración del driver de Selenium
service = Service(chromedriver_path)
service.log_path = 'NUL'  # En Windows, esto redirige los logs a "ningún archivo"
service.suppress_output = True  # Suprime todos los mensajes de salida

options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")  # Opcional
options.add_argument("--disable-dev-shm-usage")  # Opcional
options.add_argument("--no-sandbox")  # Opcional
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-features=OutOfBlinkCors")
options.add_argument("--force-device-scale-factor=1")

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

print("Escanea el código QR para iniciar sesión en WhatsApp Web...")
input("\nUNA VEZ INICIO SESIÓN EN WSP WEB PRESIONE ENTER PARA CONTINUAR ...")
#time.sleep(25)

try:
    while 1:
        input("\nSELECIONE EL GRUPO EN WSP WEB Y LUEGO PRESIONE ENTER EN LA CONSOLA PARA CONTINUAR ...")

        group_name = driver.find_element(By.CSS_SELECTOR, "div._amig > span").text
        print(group_name)

        # # open the info group
        # group_info_button = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "div._amig"))
        # ).click()

        # select the members list
        # menbers_group = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[3]/div/div[5]/span/div/span/div/div/div/section/div[6]/div[1]/div/div[1]/span"))
        # )
        # menbers_group.click()

        # time.sleep(3)
        input("\nSELECIONE LOS MIEMBROS Y LUEGO PRESIONE ENTER EN LA CONSOLA PARA CONTINUAR ...")

        # get text with the tag
        A_nums, B_nums = [], []

        # while True:
        #     if keyboard.is_pressed("q"):  # Cambia 'q' por otra tecla si lo deseas
        #         print("END NUMBERS")
        #         break
        #A_elementos = driver.find_elements(By.CSS_SELECTOR, "span._ao3e")

        band = ''
        while not len(band):
            A_elementos = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span._ao3e"))
                )
            A_nums += [elemento.text for elemento in A_elementos]

            B_elementos = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[@class='x9f619 x78zum5 xdt5ytf x1v8jjaa xkwfhqy x17e6fzg x15dh256 x1t7u3xy x1shw4ur x6ikm8r x10wlt62 x1n2onr6 x1iyjqo2 xs83m0k x1l7klhg xs8rnei xexx8yu x4uap5 x18d9i69 xkhd6sd x1coevs8 x11i5rnm xui9b5u x1mh8g0r xg3pqpk x5frtva x1a6k631 x9b845u x1n7bigs x180mg20 x12v3509 x14m7gzy']//span[@class='x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1rg5ohu _ao3e']"))
                )
            B_nums += [elemento.text for elemento in B_elementos]

            band = input(f"\n ====>>> ({len(A_nums)})-({len(B_nums)})SEGUIR? (Y:ENTER, N: 0):")
            
        print(B_nums)
        print("\n..........................................\n\n")

        phone_pattern = re.compile(r'^\+(\d{1,3})\s')
        unique_phone_numbers = set()

        for phone in A_nums:
            text_p = phone.split(', ')
            for text in text_p:
                if phone_pattern.match(text):
                    unique_phone_numbers.add(text)

        for text in B_nums:
            if phone_pattern.match(text):
                unique_phone_numbers.add(text)

        unique_phone_list = list(unique_phone_numbers)
        print(unique_phone_list)
        print("\n",len(A_nums), len(B_nums), len(unique_phone_list),"\n")

        # Save numbers
        if pd.io.common.file_exists(file_name):
            df = pd.read_excel(file_name)
            df[group_name] = pd.Series(unique_phone_list)
        else:
            df = pd.DataFrame({group_name: unique_phone_list})

        df.to_excel(file_name, index=False)
        print(f"\nDatos guardados en {file_name}.\n")

        go = input("\nCONTINUAR (ENTER) - SALIR ('N', 'n'): ")
        if go == 'N' or go == 'n':
            break

except Exception as e:
    print(f"Error: {e}")

finally:
    print("\nGood Bye.")
    #time.sleep(5)
    driver.quit()
