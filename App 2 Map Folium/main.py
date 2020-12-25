import folium
import pandas as pd

data=pd.read_csv("Volcanoes.csv")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elev):
    if elev < 1000:
        return 'green'
    elif elev > 1000 and elev < 3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=[41.3125,-118.266],zoom_start=6,tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el)+" m",fill_color=color_producer(el),fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<20000000
else 'orange' if 20000000<= x['properties']['POP2005'] <=30000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
