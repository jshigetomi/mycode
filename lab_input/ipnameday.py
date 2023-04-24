#!/usr/bin/python3
from string import Template
ipname = input("what is your name? \n")
ipday = input("what day of the week is it? \n")

template = Template("Hello, $name! Happy $day!")
print(template.substitute(name=ipname,day=ipday))
