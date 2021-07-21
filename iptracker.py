import sys, requests, json, folium, webbrowser

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
    
    filepath = '/home/pedro/Desktop/Programar/iptacker/map.html'
    m = folium.Map(location=[float(data['lat']), float(data['lon'])], zoom_start=10.5)
    folium.Marker([float(data['lat']), float(data['lon'])], popup=ip).add_to(m)
    m.save(filepath)
    webbrowser.open('file://' + filepath)
     
except KeyboardInterrupt:
    sys.exit(0)    