
monsters_dict = {
            'zergling' : {
                'damage' : 5,
                'hp' : 35,
                'reward' : 5 
                },
            'infested terran' : {
                'damage' : 100,
                'hp' : 100,
                'reward' : 10
                },
            'hydralisk' : {
                'damage' : 15,
                'hp': 75,
                'reward' : 15 
                },
            'ultralisk' : {
                'damage' : 25,
                'hp' : 400,
                'reward' : 50
                },
            'mutalisk' : {
                'damage' : 10,
                'hp' : 120,
                'reward' : '30'
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
                    'monster' : monsters[1],
                    'upgrade' : 5,
                    'item' : 'stim pack'
                }
         }


def main():
    print(rooms)

if __name__ == '__main__':
    main()
