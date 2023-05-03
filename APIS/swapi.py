#!/usr/bin/python3

import requests

lookups = ['people','planets','starships']

for lookup in lookups:
    url = f"https://swapi.dev/api/{lookup}"
    response = requests.get(url)
    pyData = response.json()
    print(f"There are {pyData['count']} entries in {lookup}.")
    while not pyData['next'] == None:
        for entry in pyData['results']:
            print(entry['name'])
        url = pyData['next']
        response = requests.get(url)
        pyData = response.json()
