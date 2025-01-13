import pandas as pd
import phonenumbers
from phonenumbers import NumberParseException, is_valid_number
import random

numeros_a_eliminar = [
    "+92 319 2080765", "+92 329 3687158", "+92 328 9908249", "+92 308 7175606",
    "+92 328 3744724", "+92 309 3860573", "+92 305 8875846", "+92 301 2451927",
    "+92 318 3573459", "+92 316 2196899", "+92 326 6701638", "+92 316 2052827",
    "+92 334 8427731", "+92 308 5908182", "+92 340 7767332", "+92 320 3747102"
]

archivo = "whatsapp_groups.xlsx"
df = pd.read_excel(archivo, header=None, skiprows=1)

# Aplanar la matriz a una sola dimensión y eliminar valores NaN
numeros = df.values.flatten()
numeros = [num for num in numeros if pd.notna(num) and num not in numeros_a_eliminar and is_valid_number(phonenumbers.parse(num))]

# Eliminar duplicados
#numeros_unicos = sorted(set(numeros))  # Opcional: ordenar los números
numeros_unicos = list(set(numeros))
random.shuffle(numeros_unicos)

# Crear un DataFrame con los números únicos en una sola columna
resultado_df = pd.DataFrame(numeros_unicos)

# Guardar el resultado en un archivo CSV sin encabezado ni índices
resultado_df.to_csv('ONE_Column_Numbers.csv', index=False, header=False)

print("Proceso completado.")
