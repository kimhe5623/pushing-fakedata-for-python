import requests, random, time

url = "http://192.241.221.155:8081/api/data/aqi/insert/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVU04iOjEsImlhdCI6MTUzMzg2NTE0NzIyNSwiZXhwIjoxNTMzODY1MTUwODI1fQ.zI062Tpg6z3yMOdo3D700WUJ2ojNnX4tXZUFMWLddfw"

specd = [{ 'SSN': 1, 'lat': 32.888600, 'lng': -117.241925 },
        { 'SSN': 2, 'lat': 32.858997, 'lng':-117.255630 },
        { 'SSN': 3, 'lat': 32.866441, 'lng': -117.231880 },
        { 'SSN': 4, 'lat': 32.867962, 'lng': -117.243413 },
        { 'SSN': 5, 'lat': 32.888286, 'lng': -117.252890}]
data={}



for i in range(5000):

    currentTime = time.mktime(time.localtime())

    for j in range(5):
        data['CO'] = random.uniform(0.0, 150.0)
        data['NO2'] = random.uniform(0.0, 150.0)
        data['SO2'] = random.uniform(0.0, 150.0)
        data['O3'] = random.uniform(0.0, 150.0)
        data['PM25'] = random.uniform(0.0, 150.0)
        data['PM10'] = random.uniform(0.0, 150.0)
        data['temperature'] = random.uniform(0.0, 40.0)
        data['timestamp'] = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(currentTime))
        data['lat'] = specd[j]['lat']
        data['lng'] = specd[j]['lng']
        data['SSN'] = specd[j]['SSN']


        r = requests.post(url+token, data=data)

    time.sleep(5)  

    if(i%100==0):
        print(r.json())