import html
import requests
import pprint
import os

url = 'http://10.11.203.199:2224/' 

def main():
    os.system('clear')
    print("Welcome to the yugioh serach API")
    choice = input('What would you like to search? [search,imgSearch,typeSearch,priceSearch]')
    if choice == 'search':
        name = input("Please input the name of the card you want to search: ")
        query = 'search?name='
        name = html.escape(name)
        pprint.pprint(requests.get(url+query+name).json())
    elif choice == 'imgSearch':
        name = input("Please input the name of the card you want to serach: ")
        query = 'imgSearch?name='
        name = html.escape(name)
        pprint.pprint(requests.get(url+query+name).json())
    elif choice == 'typeSearch':
        name = input("Please enter the type of cards you want to see: [trap card, spell card, normal monster, effect monster, ritual monster, synchro monster, xyz monster, pendulum monster, link monster, fusion monster]: ")
        query = 'typeSearch?type='
        name = html.escape(name)
        pprint.pprint(requests.get(url+query+name).json())
    elif choice == 'priceSearch':
        name = input("Please enter a price and the amazon price that matches or is less than the entered price in order of descending price list and the name of the card will display: ")
        query = 'priceSearch?price='
        pprint.pprint(requests.get(url+query+name).json())
    else:
        print("That is not a valid input")

if __name__=='__main__':
    main()
