# Análisis de Femicidios en América Latina

Este proyecto realiza un análisis de datos sobre femicidios en América Latina a partir de un archivo Excel descargado de [kaggle](https://www.kaggle.com/datasets/natalyreguerin/femicides-in-lac) que contiene estadísticas. A continuación se describen las principales etapas del proceso:

## 1. Carga de Datos
- Se importa la biblioteca `pandas` para la manipulación de datos.
- Se carga un archivo Excel que contiene estadísticas sobre femicidios.
- Se convierte el DataFrame en formato JSON y se guarda en un archivo.

## 2. Análisis Exploratorio de Datos
- Se carga el archivo JSON y se realizan diversas estadísticas descriptivas, como dimensiones del conjunto de datos, las primeras filas, un resumen estadístico, información general y conteo de valores nulos.

## 3. Generación de Reportes de Datos
- Se utiliza la biblioteca `ydata_profiling` para generar un informe del perfil de datos, que se guarda en formato HTML.

## 4. Visualización de Datos
- Se generan gráficos para analizar la distribución de femicidios por país y por año utilizando las bibliotecas `matplotlib` y `seaborn`.
- Se agrupan los datos por país y año para realizar análisis adicionales.

## 5. Agrupación y Almacenamiento de Resultados
- Se agrupan los datos de femicidios por país y año, y se guardan los resultados en archivos JSON.

## 6. Análisis Geoespacial
- Se cargan datos geoespaciales en formato GeoJSON para visualizar los femicidios por país en un mapa.
- Se realizan reemplazos en los nombres de los países para asegurar consistencia.
- Se fusionan los datos de femicidios con los datos geoespaciales y se genera un gráfico que muestra el número de femicidios por país.
- Se guardan las visualizaciones en formatos PNG y SVG.

## 7. Resultados Finales
- Se presentan las visualizaciones y se almacenan los resultados del análisis en archivos gráficos y de datos.

## Explicación de la Estructura de Carpetas

- **data**: 
  - Contiene archivos de datos brutos y procesados utilizados en el análisis.
  - Incluye un archivo Excel con estadísticas de femicidios, metadatos, un archivo GeoJSON para información geoespacial y varios archivos JSON que almacenan datos procesados sobre femicidios por año y país.

- **data_manipulation**: 
  - Incluye scripts Python para manipular datos, en este caso, un archivo que convierte los datos de Excel a formato JSON.

- **data_profiling**: 
  - Contiene el informe de perfil de datos generado en formato HTML, que proporciona un resumen y análisis descriptivo del conjunto de datos.

- **EDA (Análisis Exploratorio de Datos)**:
  - Incluye scripts Python para realizar análisis exploratorios, como análisis de perfil de datos, gráficos básicos y mapas geográficos.
  - También incluye un directorio `__pycache__`, que almacena archivos compilados de Python para optimizar la carga de los módulos.

- **graphics**: 
  - Contiene imágenes generadas a partir de análisis y visualizaciones, como gráficos de femicidios por año y país. Los formatos incluyen PNG y SVG, que permiten mantener la calidad de las imágenes.

- **main.py**: 
  - El script principal que probablemente orquesta la ejecución de los distintos módulos y scripts del proyecto, realizando el análisis general y generando las salidas deseadas.

```bash
├── data
│   ├── CEPAL_statistics_feminicidios_20230627_copy.xlsx
│   ├── CEPAL_statistics_feminicidios_metadatos_20230627.xlsx
│   ├── custom.geo.json
│   ├── data.json
│   ├── femicidios_por_año.json
│   ├── femicidios_por_pais_año.json
│   └── femicidios_por_pais.json
├── data_manipulation
│   └── convert_to_json.py
├── data_profiling
│   └── data_profile_report.html
├── EDA
│   ├── data_profiling.py
│   ├── EDA_basic.py
│   ├── geomap.py
│   ├── __init__.py
│   └── __pycache__
│       ├── EDA_basic.cpython-310.pyc
│       └── __init__.cpython-310.pyc
├── graphics
│   ├── femicidios_por_año_Anguila.png
│   ├── femicidios_por_año_Argentina.png
│   ├── femicidios_por_año_Belice.png
│   ├── femicidios_por_año_Bolivia (Estado Plurinacional de).png
│   ├── femicidios_por_año_Brasil.png
│   ├── femicidios_por_año_Chile.png
│   ├── femicidios_por_año_Colombia.png
│   ├── femicidios_por_año_Costa Rica.png
│   ├── femicidios_por_año_Dominica.png
│   ├── femicidios_por_año_Ecuador.png
│   ├── femicidios_por_año_El Salvador.png
│   ├── femicidios_por_año_Guatemala.png
│   ├── femicidios_por_año_Honduras.png
│   ├── femicidios_por_año_Islas Vírgenes Británicas.png
│   ├── femicidios_por_año_México.png
│   ├── femicidios_por_año_Panamá.png
│   ├── femicidios_por_año_Paraguay.png
│   ├── femicidios_por_año_Perú.png
│   ├── femicidios_por_año.png
│   ├── femicidios_por_año_República Dominicana.png
│   ├── femicidios_por_año_Santa Lucía.png
│   ├── femicidios_por_año_Trinidad y Tabago.png
│   ├── femicidios_por_año_Uruguay.png
│   ├── femicidios_por_año_Venezuela (República Bolivariana de).png
│   ├── feminicidios por pais_.png
│   ├── feminicidios_map.png
│   ├── feminicidios_map.svg
│   ├── feminicidios_por_pais.png
│   └── top_femicidios_por_pais.png
├── main.py

```