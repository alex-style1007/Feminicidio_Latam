import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('../data', exist_ok=True)

def data_json():# Definir los componentes de la ruta
    base_dir = os.path.expanduser('~')  # Ruta al home del usuario
    project_folder = 'Escritorio/feminicidios_Latam/data'
    file_name = 'data.json'
    file_path = os.path.join(base_dir, project_folder, file_name)
    return file_path

def save_graphics():
    base_dir=os.path.expanduser('~')
    project_folder='Escritorio/feminicidios_Latam/graphics'
    save_dir=os.path.join(base_dir,project_folder)
    return save_dir
save_dir=save_graphics()
file_path=data_json()

data=pd.read_json(file_path,lines=True)

print("Dimensiones del dataser",data.shape)
print("\nPrimeras filas del dataset")
print(data.head())
print("\nResumen estadistico")
print(data.describe(include='all'))
print("\nInformacion del dataset")
print(data.info())
print("\nValores nulos")
print(data.isnull().sum())



def save_femicidios_distribution_plot(df, save_dir, file_name='femicidios_distribution.png'):
    # Crear la carpeta si no existe
    os.makedirs(save_dir, exist_ok=True)
    
    # Ruta completa para guardar el gráfico
    file_path = os.path.join(save_dir, file_name)
    
    # Generar el gráfico
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='País__ESTANDAR', palette='viridis')
    plt.xticks(rotation=45)
    plt.title('Número de Femicidios por País')
    plt.ylabel('Número de Femicidios')
    plt.xlabel('País')
    
    # Guardar el gráfico
    plt.savefig(file_path, bbox_inches='tight')
    plt.close()  # Cerrar el gráfico después de guardarlo
    
    print(f"Gráfico guardado en: {file_path}")
    
    return file_path


save_femicidios_distribution_plot(data,save_dir,file_name='feminicidios por pais.png')

def save_femicidios_by_year_plot(df, save_dir, file_name='femicidios_by_year.png'):
    # Crear la carpeta si no existe
    os.makedirs(save_dir, exist_ok=True)
    
    # Ruta completa para guardar el gráfico
    file_path = os.path.join(save_dir, file_name)
    
    # Generar el gráfico
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Años__ESTANDAR', palette='magma')
    plt.title('Número de Femicidios por Año')
    plt.ylabel('Número de Femicidios')
    plt.xlabel('Año')
    
    # Guardar el gráfico
    plt.savefig(file_path, bbox_inches='tight')
    plt.close()  # Cerrar el gráfico después de guardarlo
    
    print(f"Gráfico guardado en: {file_path}")
    
    return file_path

save_femicidios_by_year_plot(data, save_dir, file_name='femicidios_por_año.png')

# 5. Agrupar datos
femicidios_por_pais = data.groupby('País__ESTANDAR')['Número de femicidios o feminicidios'].sum().reset_index()
femicidios_por_pais = femicidios_por_pais.sort_values(by='Número de femicidios o feminicidios', ascending=False)
# Reemplazar valores en la columna 'País__ESTANDAR'
femicidios_por_pais['País__ESTANDAR'] = femicidios_por_pais['País__ESTANDAR'].replace({
    'Venezuela (República Bolivariana de)': 'Venezuela',
    'Bolivia (Estado Plurinacional de)': 'Bolivia',
})

def plot_top_femicidios_by_country(femicidios_por_pais, save_dir, file_name='top_femicidios_by_country.png'):
    # Crear la carpeta si no existe
    os.makedirs(save_dir, exist_ok=True)
    
    # Ruta completa para guardar el gráfico
    file_path = os.path.join(save_dir, file_name)
    
    # Generar el gráfico
    plt.figure(figsize=(12, 8))
    sns.barplot(data=femicidios_por_pais.head(10), x='Número de femicidios o feminicidios', y='País__ESTANDAR', palette='Blues_d')
    plt.title('Top 10 Países con Mayor Número de Femicidios')
    plt.xlabel('Número de Femicidios')
    plt.ylabel('País')
    
    # Guardar el gráfico
    plt.savefig(file_path, bbox_inches='tight')
    plt.close()  # Cerrar el gráfico después de guardarlo
    
    print(f"Gráfico guardado en: {file_path}")
    
    return file_path

plot_top_femicidios_by_country(femicidios_por_pais, save_dir, file_name='top_femicidios_por_pais.png')