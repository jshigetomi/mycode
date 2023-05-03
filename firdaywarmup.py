#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import html
import random
import os

URL= "https://opentdb.com/api.php?amount=10&category=17&difficulty=hard&type=multiple"

def main():

    os.system('clear')
    numQ = input("How many questions do you want? ")
    catURL = "https://opentdb.com/api_category.php"
    os.system('clear')
    data = requests.get(catURL).json()
    for cat in data['trivia_categories']:
        print(f"{cat['id']}" + ": " + cat['name'])
    Cat = input("Please enter a category from 9-32: ")
    input(f"You selected {data['trivia_categories'][int(Cat)-data['trivia_categories'][0]['id']]['name']}")
    os.system('clear')
    diff = input("Please enter difficulty (easy,medium,hard): ")
    URL = f"https://opentdb.com/api.php?amount={numQ}&category={Cat}&difficulty={diff}&type=multiple"

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    total = int(numQ)
    correct = 0
    for entry in data['results']:
        os.system('clear')
        print(html.unescape(entry['question']))
        choices = []
        choices.append(html.unescape(entry['correct_answer']))
        for answers in entry['incorrect_answers']:
            choices.append(html.unescape(answers))
        random.shuffle(choices)
        i = 1
        for choice in choices:
            print(f"{i}. " + choice)
            i += 1
        answer = int(input("Please select 1-4: "))
        if choices[answer-1] == html.unescape(entry['correct_answer']):
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect! The correct answer was {html.unescape(entry['correct_answer'])}") 
    os.system('clear')
    print(f"You got a total of {correct} questions correct. You got {correct/total}%")
    
if __name__ == "__main__":
    main()
