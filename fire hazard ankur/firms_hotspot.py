# # -*- coding: utf-8 -*-
# """FIRMS_API_Hotspots.ipynb

# Automatically generated by Colab.

# Original file is located at
#     https://colab.research.google.com/drive/1KmdU43B1t5LlmMrom3SJhtfwZ9zC3K6v
# """

# import pandas as pd
# import folium
# import geopandas as gpd
# from folium.plugins import MarkerCluster

# MAP_KEY = '430c52106a780ccb3cd78318ad2dd3b9'

# # this url will return information about all supported sensors and their corresponding datasets
# # instead of 'all' you can specify individual sensor, ex:LANDSAT_NRT
# da_url = 'https://firms.modaps.eosdis.nasa.gov/api/data_availability/csv/' + MAP_KEY + '/all'
# df = pd.read_csv(da_url)
# display(df)

# # Function to fetch MODIS hotspots by country
# def get_hotspots_by_country(country_code, day_range):
#     url = f'https://firms.modaps.eosdis.nasa.gov/api/country/csv/{MAP_KEY}/MODIS_NRT/{country_code}/{day_range}'
#     try:
#         df = pd.read_csv(url)
#         print(f"Retrieved {len(df)} records for country {country_code}")
#         return df
#     except:
#         print("Error retrieving data for the specified country.")
#         return None

# #JAPAN FIRES
# japan_url = 'https://firms.modaps.eosdis.nasa.gov/api/country/csv/' + MAP_KEY + '/MODIS_NRT/NGA/5'
# df_japan = pd.read_csv(japan_url)
# df_japan

# df = df_japan

# # Initialize Folium Map
# m = folium.Map(location=[df["latitude"].mean(), df["longitude"].mean()], zoom_start=6)
# marker_cluster = MarkerCluster().add_to(m)

# # Add fire markers
# for _, row in df.iterrows():
#     popup_text = (f"<b>Brightness Temp:</b> {row['brightness']}<br>"
#                   f"<b>Confidence:</b> {row['confidence']}<br>"
#                   f"<b>FRP:</b> {row['frp']}<br>"
#                   f"<b>Date:</b> {row['acq_date']}<br>"
#                   f"<b>Satellite:</b> {row['satellite']}")
#     folium.Marker(
#         location=[row["latitude"], row["longitude"]],
#         popup=folium.Popup(popup_text, max_width=300),
#         icon=folium.Icon(color="red", icon="fire")
#     ).add_to(marker_cluster)

# # Display the map
# m

