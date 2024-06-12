import folium
import pandas
import requests

#m = folium.Map(location=(31.7619, -106.4850))
m = folium.Map(location=[48, -102], zoom_start=3)

state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
).json()

state_data = pandas.read_csv()


m = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Missing Persons"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.9,
    line_opacity=0.5,
    legend_name="Missing Persons",
).add_to(m)

folium.LayerControl().add_to(m)

m.save("missing_persons_by_state.html")