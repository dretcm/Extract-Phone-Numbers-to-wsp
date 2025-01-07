import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")  # Opcional
options.add_argument("--disable-dev-shm-usage")  # Opcional
options.add_argument("--no-sandbox")  # Opcional

chromedriver_path = 'chromedriver.exe'
url = "https://web.whatsapp.com/"
file_name = "whatsapp_groups.xlsx"
group_name = "LA JARRITA🍟🍗 #1"

# Configuración del driver de Selenium
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(url)

print("Escanea el código QR para iniciar sesión en WhatsApp Web...")
time.sleep(25)

try:
    # print(f"Buscando el grupo: {group_name}")

    # # search box
    # search_box = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "p.selectable-text.copyable-text.x15bjb6t.x1n2onr6"))
    # )
    # search_box.click()
    # search_box.send_keys(group_name)

    # time.sleep(2)

    # # select group by name
    # group = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.XPATH, f"//span[@title='{group_name}']"))
    # )
    # group.click()

    # print(f"Entraste al grupo: {group_name}")

    print("go")
    time.sleep(10)

    # open the info group
    group_info_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div._amig"))
    ).click()

    time.sleep(2)

    # select the members list
    menbers_group = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[3]/div/div[5]/span/div/span/div/div/div/section/div[6]/div[1]/div/div[1]/span"))
    )
    menbers_group.click()

    time.sleep(5)
    print("members contact:")

    # get text with the tag
    phone_numbers = driver.find_elements(By.CSS_SELECTOR, "span._ao3e")

    phone_pattern = re.compile(r'^\+(\d{1,3})\s')
    unique_phone_numbers = set()

    for phone in phone_numbers:
        text_p = phone.text.split(', ')
        for text in text_p:
            if phone_pattern.match(text):
                unique_phone_numbers.add(text)

    unique_phone_list = list(unique_phone_numbers)
    print(unique_phone_list)

    # Save numbers
    if pd.io.common.file_exists(file_name):
        df = pd.read_excel(file_name)
        df[group_name] = pd.Series(unique_phone_list)
    else:
        df = pd.DataFrame({group_name: unique_phone_list})

    df.to_excel(file_name, index=False)
    print(f"Datos guardados en {file_name}")

except Exception as e:
    print(f"Error: {e}")

finally:
    time.sleep(5)
    driver.quit()
