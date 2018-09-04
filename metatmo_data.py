import requests, random, time

url = "http://192.241.221.155:8081/api/data/metatmo/insert/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVU04iOjEsImlhdCI6MTUzMzU5MzI0NywiZXhwIjoxNTMzNTk2ODQ3fQ.6YqtM8J2ynHOs6a1KLWqxytnYSYBbdK5_-TieeDC1m0"

data = {}

for i in range(1000):

    from_t = (2018, 7, 13, 10, 39, 45, 1, 48, 0)
    from_t = time.mktime(from_t)
    to_t = time.mktime(time.localtime())

    data['CO2'] = random.uniform(0.0, 500.0)
    data['lat'] = random.uniform(32.830302, 32.947776)
    data['lng'] = random.uniform(-117.250579, -117.122796)
    data['timestamp'] = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(random.uniform(from_t, to_t)))


    r = requests.post(url+token, data=data)

    if(i%100==0):
        print(r.json())