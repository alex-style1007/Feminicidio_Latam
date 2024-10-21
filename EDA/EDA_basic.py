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


# save_femicidios_distribution_plot(data,save_dir,file_name='feminicidios por pais_.png')

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

# save_femicidios_by_year_plot(data, save_dir, file_name='femicidios_por_año.png')



def save_data_as_json(data):
    #Agrupar datos
    femicidios_por_pais = data.groupby('País__ESTANDAR')['Número de femicidios o feminicidios'].sum().reset_index()
    femicidios_por_pais = femicidios_por_pais.sort_values(by='Número de femicidios o feminicidios', ascending=False)

    # Reemplazar valores en la columna 'País__ESTANDAR'
    femicidios_por_pais['País__ESTANDAR'] = femicidios_por_pais['País__ESTANDAR'].replace({
        'Venezuela (República Bolivariana de)': 'Venezuela',
        'Bolivia (Estado Plurinacional de)': 'Bolivia',
    })

    # Definir la ruta de guardado
    base_dir = os.path.expanduser('~')  # Ruta al home del usuario
    project_folder = 'Escritorio/feminicidios_Latam/data'
    save_dir = os.path.join(base_dir, project_folder)
    json_file_path = os.path.join(save_dir, 'femicidios_por_pais.json')

    # Guardar en formato JSON
    femicidios_por_pais.to_json(json_file_path, orient='records', lines=True)

    print(f"Datos guardados en: {json_file_path}")
    return femicidios_por_pais

# femicidios_por_pais=save_data_as_json(data)


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

# plot_top_femicidios_by_country(femicidios_por_pais, save_dir, file_name='top_femicidios_por_pais.png')

def analyze_femicidios_by_year(data):
    # Agrupar por año y sumar los feminicidios
    femicidios_por_año = data.groupby('Años__ESTANDAR')['Número de femicidios o feminicidios'].sum().reset_index()

    # Mostrar el DataFrame resultante
    print(femicidios_por_año)

    # Crear un gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(femicidios_por_año['Años__ESTANDAR'], femicidios_por_año['Número de femicidios o feminicidios'], color='blue')
    plt.title('Número de Feminicidios por Año')
    plt.xlabel('Año')
    plt.ylabel('Número de Feminicidios')
    plt.grid()
    plt.xticks(rotation=45)

    # Definir rutas para guardar los resultados
    graphics_dir = '/home/alex/Escritorio/feminicidios_Latam/graphics'
    data_dir = '/home/alex/Escritorio/feminicidios_Latam/data'

    # Crear carpetas si no existen
    os.makedirs(graphics_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)

    # Guardar el gráfico
    graph_file_path = os.path.join(graphics_dir, 'femicidios_por_año.png')
    plt.savefig(graph_file_path, bbox_inches='tight')
    plt.close()  # Cerrar el gráfico después de guardarlo
    print(f"Gráfico guardado en: {graph_file_path}")

    # Guardar los datos en formato JSON
    json_file_path = os.path.join(data_dir, 'femicidios_por_año.json')
    femicidios_por_año.to_json(json_file_path, index=False)
    print(f"Datos agrupados por año guardados en: {json_file_path}")

    return json_file_path, graph_file_path

# json_path, graph_path = analyze_femicidios_by_year(data)


def analyze_femicidios_by_country_and_year(data):
    # Agrupar por país y año, y sumar los feminicidios
    femicidios_por_pais_año = data.groupby(['País__ESTANDAR', 'Años__ESTANDAR'])['Número de femicidios o feminicidios'].sum().reset_index()

    # Obtener la lista de países únicos
    paises = femicidios_por_pais_año['País__ESTANDAR'].unique()

    # Definir la ruta para guardar los resultados
    graphics_dir = '/home/alex/Escritorio/feminicidios_Latam/graphics'
    data_dir = '/home/alex/Escritorio/feminicidios_Latam/data'

    # Crear carpetas si no existen
    os.makedirs(graphics_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)

    # Crear gráficos de dispersión separados para cada país
    for pais in paises:
        plt.figure(figsize=(10, 6))  # Tamaño de la figura para cada gráfico
        data_pais = femicidios_por_pais_año[femicidios_por_pais_año['País__ESTANDAR'] == pais]
        
        plt.scatter(data_pais['Años__ESTANDAR'], data_pais['Número de femicidios o feminicidios'], color='blue')
        plt.title(f'Número de Feminicidios por Año - {pais}')
        plt.xlabel('Año')
        plt.ylabel('Número de Feminicidios')
        plt.grid()
        plt.xticks(rotation=45)

        # Guardar el gráfico
        graph_file_path = os.path.join(graphics_dir, f'femicidios_por_año_{pais}.png')
        plt.savefig(graph_file_path, bbox_inches='tight')
        plt.close()  # Cerrar el gráfico después de guardarlo
        print(f"Gráfico guardado en: {graph_file_path}")

    # Guardar los datos agrupados en formato JSON
    json_file_path = os.path.join(data_dir, 'femicidios_por_pais_año.json')
    femicidios_por_pais_año.to_json(json_file_path, index=False)
    print(f"Datos agrupados por país y año guardados en: {json_file_path}")

    return json_file_path

# json_path = analyze_femicidios_by_country_and_year(data)
