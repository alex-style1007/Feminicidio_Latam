from EDA.EDA_basic import *


save_dir=save_graphics()
file_path=data_json()

data=pd.read_json(file_path,lines=True)

save_femicidios_distribution_plot(data,save_dir,file_name='feminicidios por pais_.png')
save_femicidios_by_year_plot(data, save_dir, file_name='femicidios_por_año.png')
femicidios_por_pais=save_data_as_json(data)
plot_top_femicidios_by_country(femicidios_por_pais, save_dir, file_name='top_femicidios_por_pais.png')
json_path, graph_path = analyze_femicidios_by_year(data)
json_path = analyze_femicidios_by_country_and_year(data)
