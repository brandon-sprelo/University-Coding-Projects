def createCityPopDict():
    file = open('pop3.txt','r')
    s = file.read()
    file.close()
    line = s.split('\n')
    while '' in line:
        line.remove('')
    D = {}
    Q = []
    W = []
    for z in line:
        x = z.split()
        Q.append(x)
    for c in Q:
        W.append((' '.join(c[1:-1]), c[-1]))
    for v in W:
        D[v[0]] = int(v[1])
    return D
        

def createCityLatLonDict():
    file = open('latLon3.txt')
    s = file.read()
    file.close()
    line = s.split('\n')
    while '' in line:
        line.remove('')
    D = {}
    Q = []
    W = []
    for z in line:
        x = z.split()
        Q.append(x)
    for c in Q:
        W.append((' '.join(c[2:]), float(c[0]), -float(c[1])))
    for v in W:
        D[v[0]] = (v[1], v[2])
    return D 

def createStateColorDict():
    file = open('stateAdj.txt')
    s = file.read()
    file.close()
    line = s.split('\n')
    while '' in line:
        line.remove('')
    D = {}
    Q = []
    W = []
    for z in range(len(line)):
        if z % 2 == 0:
            x = line[z].split(',')
            Q.append((x[0].lower(), int(line[z+1])))
    for c in Q:
        D[c[0]] = int(c[1])
    return D

cityPopDict = createCityPopDict()
cityLatLonDict = createCityLatLonDict()
stateColorDict = createStateColorDict()
colorList = ['blue', 'red', 'green', 'purple']

Z = []
lat = []
lon = []
for key in cityLatLonDict:
    Z.append(cityLatLonDict[key])
    for w in Z:
        lat.append(w[0])
        lon.append(w[1])
latMin = min(lat)
latMax = max(lat)
lonMin = min(lon)
lonMax = max(lon)

import math
import turtle as t
t.ht()
t.tracer(0,0)
t.up()
t.setworldcoordinates(lonMin-10 ,latMin-10, lonMax+10, latMax+10)



for key in cityLatLonDict:
    t.up()
    x = cityLatLonDict[key][1]
    y = cityLatLonDict[key][0]
    t.setposition(float(x), float(y))
    t.down()
    o = key.split(',')
    k = colorList[stateColorDict[o[1]]]

    if key in cityPopDict:
        t.dot(4 + math.ceil(math.sqrt(cityPopDict[key]/50000)),k)
    else:
        t.dot(4, k)


openfile = open('output.txt', 'w')
o = '{:30}{:<15}{:<15}{:<15}{:<15}{:<15}\n\n'.format('city name:', 'latitude:', 'longitude:', 'population:', 'dot size:', 'dot color:')
openfile.write(o)
fmt = '{:30}{:<15}{:<15}{:<15}{:<15}{:<15}\n'
s = ''
for key in cityLatLonDict:
    keyS = key
    latitude = cityLatLonDict[key][0]
    longitude = cityLatLonDict[key][1]
    longitude = -float(longitude)
    if key in cityPopDict:
        population = cityPopDict[key]
        dotSize = 4 + math.ceil(math.sqrt(cityPopDict[key]/50000))
    else:
        population = ''
        dotSize = 4
    o = key.split(',')
    color = colorList[stateColorDict[o[1]]]
    s += fmt.format(keyS, latitude, longitude, population, dotSize, color)
openfile.write(s)
openfile.close()
        
    
    

    
