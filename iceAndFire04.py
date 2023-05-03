#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
url =  "https://www.anapioficeandfire.com/api/characters?page=1&pageSize=50"

def main():
        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotchars = requests.get(url)
        headerlinks = gotchars.links
        
        ## Decode the response
        got_dj = gotchars.json()
        
        inTv = 0
        notTv = 0
        total_count = 0

        for entry in got_dj:
            total_count += 1
            if entry['tvSeries'][0] == '':
                notTv += 1
            else:
                inTv +=1
                if entry['name'] == '':
                    print(f"{entry['aliases'][0]} was in {entry['tvSeries']}")
                else:
                    print(f"{entry['name']} was in {entry['tvSeries']}")
        gotchars = requests.get(headerlinks['next']['url'])
        headerlinks = gotchars.links

        try:
            while len(headerlinks) > 3:
                for entry in got_dj:
                    total_count += 1
                    if entry['tvSeries'][0] == '':
                        notTv += 1
                    else:
                        inTv += 1
                        if entry['name'] == '':
                            print(f"{entry['aliases'][0]} was in {entry['tvSeries']}")
                        else:
                            print(f"{entry['name']} was in {entry['tvSeries']}")
                
                gotchars = requests.get(headerlinks['next']['url'])
                headerlinks = gotchars.links
                got_dj = gotchars.json()
        except:
            print('last page')
        
        gotchars = requests.get(headerlinks['last']['url'])
        got_dj = gotchars.json()
        for entry in got_dj:
            total_count +=1
            if entry['tvSeries'][0] == '':
                notTv += 1
            else:
                inTv += 1
                print(f"{entry['name']} was in  {entry['tvSeries']}")

        print(f"Total number of characters: {total_count}")
        print(f"Total number of characters on TV: {inTv}")
        print(f"Total number of characters not on TV: {notTv}")
        print(f"Percentage of characters on Tv: {inTv/total_count*100}")
        print(f"Percentage of characters not on Tv: {notTv/total_count*100}")
        
if __name__ == "__main__":
        main()

