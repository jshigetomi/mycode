luke_skywalker = {
    'Title': ['Jedi Knight', 'Jedi Master', 'Red Five', 'Rogue Leader'
              ],
    'Occupation': ['Apprentice', 'Moisture Farmer', 'Pilot', 'Jedi'],
    'Affiliation': [
        'Skywalker family',
        'Rebel Alliance',
        'Rogue Squadron',
        'Jedi',
        'New Republic',
        'New Jedi Order',
        'Resistance',
        'Galactic Alliance',
        'Jedi Council',
        ],
    'Family': ['Padm\xc3\xa9 Amidala (mother)',
               'Anakin Skywalker (father)', 'Leia Organa (twin sister)'
               , 'Owen Lars (paternal step-uncle)',
               'Beru Lars (paternal step-aunt)'],
    }

luke_skywalker.update({"fictional":True})

count = 1
for key in luke_skywalker.keys(): 
    print(count, key)
    count += 1

choice = int(input("Enter one of the keys: "))
key = list(luke_skywalker.keys())[choice - 1]
output = luke_skywalker.get(key,"That was not one of the keys!")
print(f"{output}")
