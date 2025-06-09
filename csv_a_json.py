import pandas as pd
import json
import os

# Ruta del archivo CSV
archivo_csv = 'datos.secc25.csv'

# Comprobamos si existe el archivo
if not os.path.exists(archivo_csv):
    print(f"❌ Error: El archivo {archivo_csv} no fue encontrado.")
else:
    try:
        # Definir columnas manualmente si no hay encabezado
        columnas = ['ntcse', 'uunn', 'amt', 'direccion', 'wgsy', 'wgsx']
        
        # Leer CSV con tolerancia a errores
        df = pd.read_csv(archivo_csv, names=columnas, header=None, on_bad_lines='skip')

        # Eliminar filas vacías
        df.dropna(how='all', inplace=True)

        # Guardar como JSON
        df.to_json('secc_datos.json', orient='records', force_ascii=False, indent=2)

        print("✅ Archivo 'secc_datos.json' creado correctamente.")

    except Exception as e:
        print(f"❌ Error al procesar el archivo: {e}")
