import requests

api_address='http://api.openweathermap.org/data/2.5/weather?q=Ahmedabad&appid=bdcbdf213d1e22d55886e0ecfeb15658'
json_data = requests.get(api_address).json()

def temp():
    temperature= round(json_data["main"]["temp"]-237,1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description

print(temp())
print(des())