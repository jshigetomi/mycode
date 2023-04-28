
monsters_dict = {
            'zergling' : {
                'damage' : 5,
                'hp' : 35
                },
            'infested terran' : {
                'damage' : 100,
                'hp' : 100
                },
            'hydralisk' : {
                'damage' : 15,
                'hp': 75
                },
            'ultralisk' : {
                'damage' : 25,
                'hp' : 400
                },
            'mutalisk' : {
                'damage' : 10,
                'hp' : 120,
                }
            }
monsters = list(monsters_dict.keys())

rooms = {

            'Entry' : {
                  'south' : 'Corridor',
                  'east'  : 'Right Wing',
                  'item'  : 'gauss rifle'
                },

            'Corridor' : {
                  'north' : 'Entry',
                  'south' : 'South Corridor',
                  'monster'  : monsters[0]
                },
            'Right Wing' : {
                  'west' : 'Entry',
                  'south': 'Lab',
                  'monster' : monsters[0]
                },
            'Lab' : {
                  'north' : 'Right Wing',
                  'east' : 'Engineering Bay',
                  'south' : 'Security Room',
                  'monster': monsters[0]
                },
            'South Corridor' : {
                  'north' : 'Corridor',
                  'monster' : monsters[0]
                },
            'Engineering Bay' : {
                    'west' : 'Lab',
                    'monster' : monsters[1]
                }
         }


def main():
    print(rooms)

if __name__ == '__main__':
    main()
