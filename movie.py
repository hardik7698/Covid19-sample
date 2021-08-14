import covid19dh
import pandas as pd

x, src = covid19dh.covid19() 
# x=x[['iso_alpha_2' is not Null ]]
x = x.dropna(axis=0, subset=['iso_alpha_2','confirmed','tests'])
columns=list(x.columns)
countriesid=list(x['iso_alpha_2'].unique())
countries=list(x['administrative_area_level_1'].unique())
latitude=list(x['latitude'].unique())
longitude=list(x['longitude'].unique())
# print(DataFrame(x.query('iso_alpha_2=="AF"')['confirmed']))

    
# print(len(country()))

