farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

locations = []

for entry in farms:
    locations.append(entry['name'])

animalList = ["sheep","cows","pigs","chickens","llamas","cats"]

for entry in locations:
    print(entry)

choice = input("Please choose a farm: ")

while not choice in locations:
    choice = input("Please choose a farm: ")

for entry in farms:
    if entry['name'] == choice:
        print(f"The animals from {choice}:")
        for animals in entry['agriculture']:
            if animals in animalList:
                print(animals)
