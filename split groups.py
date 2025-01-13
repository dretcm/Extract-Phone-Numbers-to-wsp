import pandas as pd
import csv

archivo = 'ONE_Column_Numbers.csv'

def cargar_numeros(csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return [row[0].strip() for row in reader]

df = cargar_numeros(archivo)
n = int(input("Enter amount per group: "))

# Dividir en grupos
split_groups = []
ago = 0

for i in range(n, len(df), n):
    split_groups.append(df[ago:i])
    ago = i

# Agregar los números restantes (si los hay)
if ago < len(df):
    split_groups.append(df[ago:])

# Rellenar los grupos más cortos con None para igualar la longitud
max_length = max(len(group) for group in split_groups)
for group in split_groups:
    group.extend([None] * (max_length - len(group)))

# Convertir a DataFrame
resultado_df = pd.DataFrame({f"Group {i+1}": group for i, group in enumerate(split_groups)})

# Guardar en CSV
resultado_df.to_csv('split_groups.csv', index=False)
print("Proceso completado. Archivo guardado como 'split_groups.csv'.")
