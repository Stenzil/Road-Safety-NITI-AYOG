#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 11:10:10 2018

@author: xor
"""
import numpy as np
from geopy.geocoders import Nominatim
import json
path = 'niti.csv' 
xxx=[]
import matplotlib.pyplot as plt
#records = [json.loads(line) for line in open(path)]
import pandas as pd
data=pd.read_csv(path)
c=data.copy().filter(items='Event Time')
#data.drop(['Event Name']='Idling')
arr=np.array(data)
long2=[]
lat2=[]
long1=[]
lat1=[]
long05=[]
lat05=[]

#weight assigning to the accidents 
for xx in arr:
    if xx[0]=='Harsh Braking':
        xx[10]=2
    elif xx[0]=='Sharp Corner':
        xx[10]=1
    elif xx[0]=='Harsh Acceleration':
        xx[10]=0.5
    xxx.append(xx)
#plotting the hotspotts
for x in xxx:
    if x[10]==2:
        plt.scatter(x[8],x[9],c='black')
    elif x[10]==1:
        plt.scatter(x[8],x[9],c='red')
    elif x[10]==0.5:
        plt.scatter(x[8],x[9],c='blue')
    else :
        plt.scatter(x[8],x[9],c='green')
for maal in arr:
   if maal[10]==2:
       if not maal[9] in long2:
           long2.append(maal[9])
           lat2.append(maal[8])
           
       else:
           pass
   if maal[10]==1:
       if not maal[9] in long1:
           long1.append(maal[9])
           lat1.append(maal[8])
       else: 
           pass
   if maal[10]==0.5:
       if not maal[9] in long05:
           long05.append(maal[9])
           lat05.append(maal[8])
       else:
           pass
   else :
       pass
#to get the location 
geolocator = Nominatim(user_agent="Analysis")
location = geolocator.reverse("23.03962271,72.5385266")
print(location.address)
#googles function to find the distance 
import googlemaps
from datetime import datetime    
gmaps = googlemaps.Client(key='AIzaSyDo032cEqlbG99Ru9gBHbyh2UKytdlkL_A')
now = datetime.now()
def navfet():
   
    directions_result = gmaps.directions("23.002243  ,72.547849","23.039623  ,72.538527",mode="driving",avoid="ferries",departure_time=now)
    print(directions_result[0]['legs'][0]['distance']['text'])
    k=directions_result[0]['legs'][0]['distance']['text']
    print('Duration: ',directions_result[0]['legs'][0]['duration']['text'])
    print(directions_result[0]['legs'][0]['duration']['text'])
    z=directions_result[0]['legs'][0]['duration_in_traffic']['text']
    print('Duration in traffic: ',directions_result[0]['legs'][0]['duration_in_traffic']['text'])
    from gtts import gTTS
    import os
    import vlc    
    mytext='travel time is'
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("test.mp3")
    q = vlc.MediaPlayer("test.mp3")
    q.play()
    mytext = z
    
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("test.mp3")
    p = vlc.MediaPlayer("test.mp3")
    p.play()
    return k
from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter.from_geocode("Ahmedabad")

gmap.scatter(lat2,long2, 'Black', size=40, marker=False)
gmap.scatter(lat1,long1, 'Red', size=40, marker=False)
gmap.scatter(lat05,long05, 'Blue', size=40, marker=False)

# Marker
hidden_gem_lat, hidden_gem_lon = 23.0225, 72.5714
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'Black')

# Draw
gmap.draw("my_map2.html")
