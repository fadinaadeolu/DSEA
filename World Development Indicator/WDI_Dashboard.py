import pandas as pd
import streamlit as st
import folium
import json
from streamlit_folium import folium_static

df = pd.read_csv("./data/WDLProcesses_tableau.csv")
country_geo = json.load(open("./data/countries.geojson"))

years = df.year.unique().tolist()
indicators = df.indicator.unique().tolist()

st.write("""# World Development Indicator""")

indicator = st.sidebar.selectbox("Select Indicator", options=indicators)

if indicator:
    indicator = indicator
else:
    indicator = 'Adjusted savings: energy depletion (current US$)'

year = st.sidebar.selectbox("Select Year", options=years)

if year:
    year = year
else:
    year = 1995

select_map = st.sidebar.selectbox(
    "Select Map Type",
    ("OpenStreetMap",
     "Stamen Terrain",
     "Stamen Toner"))


# indicator, year, select_map = user_input_features()

pd.set_option('display.max_colwidth', None)
df_temp = df[(df["indicator"] == indicator) & (df["year"] == year)]
df_input = df_temp[["country_code", "indicator_value"]]

m = folium.Map(location=[10.85, -2.35],
               tiles=select_map,
               zoom_start=3, min_zoom=1.4,
               min_lat=-90, max_lat=90)  # min_long=-60, max_long=60)


def show_maps(df_input):
    maps = folium.Choropleth(geo_data=country_geo,
                             name="choropleth",
                             data=df_input,
                             columns=["country_code", "indicator_value"],
                             key_on="feature.properties.ISO_A3",
                             fill_color='YlOrRd',
                             fill_opacity=0.7,
                             line_opacity=0.2,
                             bin=10,
                             legend_name=indicator,
                             highlight=True,
                             overlay=True,
                             reset=True).add_to(m)
    
    folium.LayerControl().add_to(m)
    maps.geojson.add_child(folium.features.GeoJsonTooltip(fields=["ADMIN"],
                                                          aliases=["Country"],
                                                          labels=True))
    folium_static(m)


show_maps(df_input)
st.write("Data", df_temp)
