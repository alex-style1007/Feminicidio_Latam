import geopandas as gpd
import os
import matplotlib.pyplot as plt
import pandas as pd

# Definir la ruta al archivo GeoJSON
base_dir = os.path.expanduser('~')  # Ruta al home del usuario
project_folder = 'Escritorio/feminicidios_Latam/data'
geojson_file = 'custom.geo.json'
file_path = os.path.join(base_dir, project_folder, geojson_file)
file_data=os.path.join(base_dir,project_folder,"femicidios_por_pais.json")

output_file=os.path.join(base_dir,'Escritorio/feminicidios_Latam/graphics',"feminicidios_map.png")
femicidios_por_pais = pd.read_json(file_data, lines=True)

# Cargar la capa temática
map_data = gpd.read_file(file_path)
map_data['pais']=map_data['sovereignt']
unico2=map_data['pais'].unique()
#print(unico2)
# Diccionario de reemplazo
reemplazos = {
    'Brazil': 'Brasil',
    'Mexico': 'México',
    'Honduras': 'Honduras',  # No se cambia
    'Dominican Republic': 'República Dominicana',
    'Colombia': 'Colombia',  # No se cambia
    'Argentina': 'Argentina',  # No se cambia
    'Peru': 'Perú',
    'Guatemala': 'Guatemala',  # No se cambia
    'El Salvador': 'El Salvador',  # No se cambia
    'Bolivia': 'Bolivia',  # No se cambia
    'Paraguay': 'Paraguay',  # No se cambia
    'Ecuador': 'Ecuador',  # No se cambia
    'Costa Rica': 'Costa Rica',  # No se cambia
    'Uruguay': 'Uruguay',  # No se cambia
    'Venezuela': 'Venezuela',  # No se cambia
    'Trinidad and Tobago': 'Trinidad y Tabago',
    'Panama': 'Panamá',
    'Chile': 'Chile',  # No se cambia
    'Saint Lucia': 'Santa Lucía',
    'Dominica': 'Dominica',  # No se cambia
    'United Kingdom': 'Islas Vírgenes Británicas',
    'Guyana': 'Guyana',  # No se cambia
    'Suriname': 'Suriname',  # No se cambia
    'France': 'France',  # No se cambia
    'Nicaragua': 'Nicaragua',  # No se cambia
    'Netherlands': 'Netherlands',  # No se cambia
    'Haiti': 'Haiti',  # No se cambia
    'Cuba': 'Cuba',  # No se cambia
    'United States of America': 'United States of America',  # No se cambia
    'Canada': 'Canada',  # No se cambia
    'Belize': 'Belice',
    'Panama': 'Panamá',  # Repetido, ya está en el diccionario
    'Denmark': 'Denmark',  # No se cambia
    'The Bahamas': 'The Bahamas',  # No se cambia
    'Grenada': 'Grenada',  # No se cambia
    'Saint Vincent and the Grenadines': 'Saint Vincent and the Grenadines',  # No se cambia
    'Barbados': 'Barbados',  # No se cambia
    'Saint Kitts and Nevis': 'Saint Kitts and Nevis',  # No se cambia
    'Jamaica': 'Jamaica'  # No se cambia
}

map_data['pais'] = map_data['pais'].replace(reemplazos)
merged=femicidios_por_pais.merge(map_data,left_on='País__ESTANDAR', 
                                   right_on='pais', 
                                   how='left')

feminicidios_gdf=gpd.GeoDataFrame(merged, geometry='geometry')

## Crear el gráfico
fig, ax = plt.subplots(1, 1, figsize=(10, 6))

# Configurar el mapa y plotear la cantidad de feminicidios o femicidios por país
feminicidios_gdf.plot(column='Número de femicidios o feminicidios', 
                      cmap='Reds', 
                      linewidth=1.5,      # Grosor del borde
                      ax=ax, 
                      edgecolor='black',   # Color del borde para resaltar las divisiones
                      legend=True)

# Títulos y etiquetas
ax.set_title('Número de Femicidios o Feminicidios por País', fontdict={'fontsize': 15}, pad=12)
ax.set_axis_off()  # Para ocultar los ejes

# Añadir etiquetas de valores en los países
for x, y, label in zip(feminicidios_gdf.geometry.centroid.x, 
                       feminicidios_gdf.geometry.centroid.y, 
                       feminicidios_gdf['Número de femicidios o feminicidios']):
    ax.text(x, y, str(label), fontsize=8, ha='center', va='center')

# Guardar el gráfico
plt.savefig(output_file, bbox_inches='tight')  # Guarda el gráfico



output_file1=os.path.join(base_dir,'Escritorio/feminicidios_Latam/graphics',"feminicidios_map.svg")

# Crear el gráfico
fig, ax = plt.subplots(1, 1, figsize=(10, 6))

# Configurar el mapa y plotear la cantidad de feminicidios o femicidios por país
feminicidios_gdf.plot(column='Número de femicidios o feminicidios', 
                      cmap='Reds', 
                      linewidth=1.5,      # Grosor del borde
                      ax=ax, 
                      edgecolor='black',   # Color del borde para resaltar las divisiones
                      legend=True)

# Títulos y etiquetas
ax.set_title('Número de Femicidios o Feminicidios por País', fontdict={'fontsize': 15}, pad=12)
ax.set_axis_off()  # Para ocultar los ejes

# Añadir etiquetas de valores en los países
for x, y, label in zip(feminicidios_gdf.geometry.centroid.x, 
                       feminicidios_gdf.geometry.centroid.y, 
                       feminicidios_gdf['Número de femicidios o feminicidios']):
    ax.text(x, y, str(label), fontsize=8, ha='center', va='center')

# Guardar el gráfico en formato SVG
plt.savefig(output_file1, bbox_inches='tight')  # Guarda el gráfico en SVG