import folium
import pandas
import requests

#m = folium.Map(location=(31.7619, -106.4850))
m = folium.Map(location=[48, -102], zoom_start=3)

state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
).json()

state_data = pandas.read_csv("https://raw.githubusercontent.com/valentinaranzbah/hostdata/main/drug_mortality_by_state.csv")


m = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Drug Overdose Mortality"],
    key_on="feature.id",
    
    fill_opacity=0.9,
    line_opacity=0.5,
    legend_name="Drug Overdose Mortality (Deaths per State)",
).add_to(m)

folium.LayerControl().add_to(m)

m.save("drug_mortality_by_state.html")