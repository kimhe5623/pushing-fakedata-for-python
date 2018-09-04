import requests, random, time

url = "http://192.241.221.155:8081/api/data/aqi/insert/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVU04iOjEsImlhdCI6MTUzNDE3MzU2MjY0MiwiZXhwIjoxNTM0MTczNTY2MjQyfQ.Go_X-sQNcRcqn-rTQVkS3WPDWeacVHe_j-ZVBlULQiM"


data = {
	"CO": 22.4234,
	"NO2": 21.2343,
	"SO2": 21.123,
	"O3": 11.2423,
	"PM25": 1.2434,
	"PM10": 2.232,
	"temperature": 22.23,
	"timestamp": "2011-07-29 19:17:17",
	"lat": 232.323,
	"lng": 223.263,
	"SSN": 2
}

for i in range(500):

    from_t = (2018, 6, 13, 10, 39, 45, 1, 48, 0)
    from_t = time.mktime(from_t)
    to_t = time.mktime(time.localtime())

    data['CO'] = random.uniform(0.0, 500.0)
    data['NO2'] = random.uniform(0.0, 500.0)
    data['SO2'] = random.uniform(0.0, 500.0)
    data['O3'] = random.uniform(0.0, 500.0)
    data['PM25'] = random.uniform(0.0, 500.0)
    data['PM10'] = random.uniform(0.0, 500.0)
    data['temperature'] = random.uniform(0.0, 40.0)
    data['timestamp'] = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(random.uniform(from_t, to_t)))
    data['lat'] = random.uniform(32.830302, 32.947776)
    data['lng'] = random.uniform(-117.250579, -117.122796)


    r = requests.post(url+token, data=data)

    if(i%100==0):
        print(r.json())