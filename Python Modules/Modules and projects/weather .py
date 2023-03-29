import requests
city_name="delhi"
data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=882bef32516f8990d82b762cae54604c").json()
# print(data)
# print(data["weather"][0]["main"])
# print(data["main"]["temp"])
# print(data["main"]["pressure"])
# print(data["name"])
# print(data["cod"])
for i in data:
    print(data[i])