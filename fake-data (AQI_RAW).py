import requests, random, time

url = "http://192.241.221.155:8081/api/data/rawair/insert/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVU04iOjEsImlhdCI6MTUzMzU5MzI0NywiZXhwIjoxNTMzNTk2ODQ3fQ.6YqtM8J2ynHOs6a1KLWqxytnYSYBbdK5_-TieeDC1m0"

data = {}

for i in range(5000):

    from_t = (2018, 5, 13, 10, 39, 45, 1, 48, 0)
    from_t = time.mktime(from_t)
    to_t = time.mktime(time.localtime())

    data['CO'] = random.uniform(0.0, 50.4)
    data['NO2'] = random.uniform(0.0, 2049.0)
    data['SO2'] = random.uniform(0.0, 1004.0)
    data['O3'] = random.uniform(0.0, 604.0)
    data['PM25'] = random.uniform(0.0, 500.4)
    data['PM10'] = random.uniform(0.0, 604.0)
    data['temperature'] = random.uniform(0.0, 40.0)
    data['timestamp'] = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(random.uniform(from_t, to_t)))
    data['lat'] = random.uniform(32.830302, 32.947776)
    data['lng'] = random.uniform(-117.250579, -117.122796)
    data['SSN'] = 2


    r = requests.post(url+token, json=data)

    if(i%100 == 0):
        print(r.json())
