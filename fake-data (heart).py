import requests, random, time

url = "http://192.241.221.155:8081/api/data/heart/insert/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVU04iOjEsImlhdCI6MTUzMzg4NjkwOTgwOSwiZXhwIjoxNTMzODg2OTEzNDA5fQ.-a4Xr-TSsd7DwXufAs0BOH3dnDos2DHwax_fby_4BGM"

data = {
    	"heart_rate": 120,
		"rr_interval":14.32 ,
		"timestamp": "2018-07-29 17:12:17",
		"lat": 332.323,
		"lng": 233.263
}

for i in range(500):

    from_t = (2018, 6, 13, 10, 39, 45, 1, 48, 0)
    from_t = time.mktime(from_t)
    to_t = time.mktime(time.localtime())

    data['heart_rate'] = random.randint(100, 170)
    data['rr_interval'] = random.uniform(330.0, 480.0)
    data['timestamp'] = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(random.uniform(from_t, to_t)))
    data['lat'] = random.uniform(32.830302, 32.947776)
    data['lng'] = random.uniform(-117.250579, -117.122796)
    data['USN'] = 1


    r = requests.post(url+token, data=data)

    if (i%100 == 0):
        print(r.json())