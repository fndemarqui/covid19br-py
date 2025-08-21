
#Downloading Brazilian COVID-19 data:
from covid19br import download_covid19

#Downloading Brazilian COVID-19 data:
brazil_df = download_covid19(level="brazil")
regions_df = download_covid19(level="regions")
states_df = download_covid19(level="states")
cities_df = download_covid19(level="cities")

# Downloading world COVID-19 data:
world_df = download_covid19(level="world")

 
