import time
import requests

BASE = "http://127.0.0.1:5000/"

a = "Green"
b = "Red"
count = 0

while 1:
    if a == "Green":
        count += 1
        a, b = "Red", "Green"
        response = requests.put(BASE + "state/3", {"s1": a, "s2": b, "cc": count})
        #response1 = requests.get(BASE + "state/3")
    else:
        count += 2
        a, b = "Green", "Red"
        response = requests.put(BASE + "state/3", {"s1": a, "s2": b, "cc": count})
        #response1 = requests.get(BASE + "state/3")
    time.sleep(5)



#response = requests.put(BASE + "state/3", {"s1": "Green", "s2": "Red"})
#print(response.json())
#input()
#response = requests.put(BASE + "state/3", {"s1": "Red", "s2": "Green"})
#print(response.json())
#input()
#response = requests.get(BASE + "state/0")
#print(response.json())