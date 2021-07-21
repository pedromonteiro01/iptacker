#890 () [] } =

import sys, requests, json

ip = input('Ip target: ')

try:
    response = requests.get(f"http://ip-api.com/json/{ip}").content
    data = json.loads(response)
    print("Ip: "+data['query'])
    print("City: "+data['city'])
    print("Country: "+data['country'])
    print("Lat: {}".format(float(data['lat'])))
    print("Lon: {}".format(float(data['lon'])))
    print("ISP: "+data['isp'])
    print("AS: "+data['as'])
     
except KeyboardInterrupt:
    sys.exit(0)    