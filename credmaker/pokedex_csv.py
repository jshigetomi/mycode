import csv
  
with open("pokedex_gen1.txt") as pokedata:
    for x in csv.DictReader(pokedata):
        if x['Type 1'] == 'Grass':
            print(f"{x['Name']} has Sp. Attack of {x['Sp. Atk']}")
        if x['Legendary'] == 'True':
            with open('lengends.txt', "w") as f:
                f.seek(0,2)
                f.write('\n')
                f.write(f"{x['Name']} is a Legendary Pokemon!\n")
