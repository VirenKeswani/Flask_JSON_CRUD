from urllib import response
import requests

BASE = "http://127.0.0.1:5000/"


data = [{"likes": 78,"name":"Joe", "views": 10000},
        {"likes": 256,"name":"Tim", "views": 6435},
        {"likes": 1,"name":"idk", "views": 123}]

for i in range (len(data)):
    response = requests.put(BASE  + "video/" + str(i), data=data[i])
    print(str(i))
    print(response.json())
    input()
# response = requests.get(BASE + "helloworld/bill")
# response = requests.put(BASE + "video/1" ,{"likes":100,"name":"bill","views":10000})
# print(response.json())

response = requests.get(BASE + "video/1")
print(response.json())
input()
response = requests.delete(BASE + "video/1")
print(response)
input()
response = requests.get(BASE + "video/1")

print(response.json())
response = requests.get(BASE + "video/0")

print(response.json())
print("update")
input()
response = requests.post(BASE + "video/2", data={"likes":100,"name":"bill","views":10000})
print(response)
print(response.json())
print("get")
input()
response = requests.get(BASE + "video/2")
print(response.json())