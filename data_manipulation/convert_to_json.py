import pandas as pd
import os

os.makedirs('../data', exist_ok=True)

# Definir los componentes de la ruta
base_dir = os.path.expanduser('~')  # Ruta al home del usuario
project_folder = 'Escritorio/feminicidios_Latam/data'
file_name = 'CEPAL_statistics_feminicidios_20230627_copy.xlsx'
file_save=os.path.join(base_dir,project_folder,"data.json")

# Combinar los componentes en una sola ruta
file_path = os.path.join(base_dir, project_folder, file_name)
df=pd.read_excel(file_path)

json_data=df.to_json(orient='records',lines=True)

with open(file_save,'w',encoding='utf-8') as json_file:
    json_file.write(json_data)

print('JSON file generated successfully')