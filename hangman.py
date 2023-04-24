#!/usr/bin/python3
#SHEBANG!

word = "secret"
myBlanks =[]
myList = []

def loadList():
    for letter in word:
        myList.append(letter)
        myBlanks.append('_')

def findletter(letter):
    if word.find(letter)==-1:
        return False
    else:
        adjustletters(letter)
        return True

def adjustletters(letter):
    index = 0
    for c in word:
        if c == letter:
            myBlanks[index] = letter

def showboard():
    for i in myBlanks:
        print(i,end="")
    print("\n")

def main():
    counter = 0
    while counter < 9:
        showboard()
        letter = input("please guess a letter")
        if findletter(letter):
            print("good job!")
        else:
            counter += 1
            print("try again, lost one life")

if __name__ == "__main__":
    main()


