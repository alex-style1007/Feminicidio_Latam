from ydata_profiling import ProfileReport
from EDA_basic import data_json
import os
import pandas as pd

file_path=data_json()

# Cargar los datos desde la función data_json()
data=pd.read_json(file_path,lines=True)
# Definir los componentes de la ruta
base_dir = os.path.expanduser('~')  # Ruta al home del usuario
project_folder = 'Escritorio/feminicidios_Latam/data_profiling'
file_name = 'data_profile_report.html'

# Combinar los componentes en una sola ruta para guardar el archivo HTML
file_save = os.path.join(base_dir, project_folder, file_name)

# Asegurarse de que el directorio de destino existe, crearlo si no
os.makedirs(os.path.join(base_dir, project_folder), exist_ok=True)

# Generar el perfil de datos
profile = ProfileReport(data, title='Data Profile Report', explorative=True)

# Guardar el informe en un archivo HTML
profile.to_file(file_save)

print(f"El perfil de datos ha sido creado y guardado como '{file_save}'.")
