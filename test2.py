import time
import requests

#http://127.0.0.1:5000/
BASE = "http://192.168.0.107:5000/"

a = "Green"
b = "Red"
count = 0


while 1:
    response = requests.put(BASE + "state/1", {"cc": count})
    count += 2

    time.sleep(2)



#response = requests.put(BASE + "state/3", {"s1": "Green", "s2": "Red"})
#print(response.json())
#input()
#response = requests.put(BASE + "state/3", {"s1": "Red", "s2": "Green"})
#print(response.json())
#input()
#response = requests.get(BASE + "state/0")
#print(response.json())