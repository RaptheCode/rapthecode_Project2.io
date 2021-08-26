import requests


api_address="https://newsapi.org/v2/top-headlines?country=in&apiKey=5bcecb601d6148ab935f581a883f3839"
json_data = requests.get(api_address).json()

ar = []

def news():
    for i in range(3):
        ar.append("number " + str(i+1)+", " + json_data["articles"][i]["title"]+".")

    return ar
