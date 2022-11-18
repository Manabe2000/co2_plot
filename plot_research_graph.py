import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import sys
from data import data

args = sys.argv
date = args[1]
n_date = args[2]

apikey = data.AIRSENSOR4_APIKEY_R
channelid = data.AIRSENSOR4_CHANNELID

url = 'https://api.thingspeak.com/channels/'+channelid +'/feed.csv'
url += '?api_key='+apikey
url += '&start= '+date +'%2000:00:00'+ '&end='+ n_date +'%2000:00:00'+'&timezone=Asia/Tokyo'
resp = requests.get(url)
text = resp.text
code = resp.status_code
resp.close()
if code != 200 :
     print("error")

strtime=[]
floatppm=[]
floattem=[]
floathum=[]
splitline = text.split('\n')
splitline.pop()
splitline.pop(0)

for w in splitline: 
     s = w.split(',')
     strtime.append(s[0])
     floatppm.append(float(s[2]))
     floattem.append(float(s[3]))
     floathum.append(float(s[4]))

apikey    = data.ROOM_STATE_APIKEY_R
channelid = data.ROOM_STATE_CHANNELID
url = 'https://api.thingspeak.com/channels/'+channelid +'/feed.csv'
url += '?api_key='+apikey
url += '&results'+'&timezone=Asia/Tokyo'
resp = requests.get(url)
text = resp.text
code = resp.status_code
resp.close()
if code != 200 :
     print("error")

strtimeofattend=[]
intattend = []
splitline = []
splitline = text.split('\n')
splitline.pop()
splitline.pop(0)

for w in splitline: 
     s = w.split(',')
     strtimeofattend.append(s[0])
     intattend.append(int(s[2]))

x = pd.to_datetime(strtime)
x2 = pd.to_datetime(strtimeofattend)
fig = plt.figure(facecolor="white")
xmin = pd.to_datetime(date+' 00:00 +0900')
xmax = pd.to_datetime(n_date + ' 00:00 +0900')

ax1 = fig.add_subplot(4, 1, 1)
ax1.plot(x, floattem)
ax1.axes.xaxis.set_visible(False)
ax1.set_xlim(xmin,xmax)
ax1.set_ylim(15,35)
ax1.set_ylabel("Temperature [℃]")

ax2 = fig.add_subplot(4, 1, 2)
ax2.plot(x, floatppm)
ax2.axes.xaxis.set_visible(False)
ax2.set_xlim(xmin,xmax)
ax2.set_ylim(300,1200)
ax2.set_ylabel("Co2 [ppm]")

ax3 = fig.add_subplot(4, 1, 3)
ax3.plot(x, floathum)
ax3.axes.xaxis.set_visible(False)
ax3.set_xlim(xmin,xmax)
ax3.set_ylim(30,90)
ax3.set_ylabel("Humidity [%]")

ax4 = fig.add_subplot(4, 1, 4)
ax4.step(x2, intattend,where = 'post')
ax4.set_xlim(xmin,xmax)
ax4.set_ylabel("Attend")

filename = date + "_" +n_date

fig.savefig("graph/"+filename+".png", facecolor=fig.get_facecolor())