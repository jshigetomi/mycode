#!/usr/bin/python3

import random

wordbank = ["identation","spaces"]

tlgstudents= ["Brandon", "Caleb", "Cat", "Chad the Beardulous", "Chance", "Chris", "Jessica", "Jorge", "Joshua", "Justin", "Lui", "Stephen"]

wordbank.append(4)

num = input("enter number between 0 and 11 or enter a name or do something else for a random result!")

if num.isdigit():
    student_name = tlgstudents[int(num)]

elif num in tlgstudents:
    student_name = num  

else:
    student_name = random.choice(tlgstudents)

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent")

