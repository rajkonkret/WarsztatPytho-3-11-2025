from typing import List

import requests
from pydantic import BaseModel

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
print(response)
# <Response [200]>
# 2xx - ok
# 3xx - warningi, przekierowania
# 4xx - 404 - brak zasobu, 400 Bad Req - błada w zapytania
# 5xx - błedy po stronie serwera

print(response.text)
response_data = response.json()
print(response_data)

for i in response_data:
    print(i)  # wypisze klucze
# people
# number
# message
print(response_data['people'])


# pydantic waliduje typy danych
class Astronaut(BaseModel):
    name: str
    craft: str


class AstroData(BaseModel):
    message: str
    people: List[Astronaut]
    number: int


data = AstroData(**response.json())
print(data)

for astronaut in data.people:
    print(f"Name: {astronaut.name}")
# Name: Oleg Kononenko
# Name: Nikolai Chub
# Name: Tracy Caldwell Dyson
# Name: Matthew Dominick
# Name: Michael Barratt
# Name: Jeanette Epps
# Name: Alexander Grebenkin
# Name: Butch Wilmore
# Name: Sunita Williams
# Name: Li Guangsu
# Name: Li Cong
# Name: Ye Guangfu
