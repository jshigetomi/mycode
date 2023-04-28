
import html
import random

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

question= trivia["question"]
correct= trivia["correct_answer"]
incorrect1= trivia["incorrect_answers"][0]
incorrect2= trivia["incorrect_answers"][1]
incorrect3= trivia["incorrect_answers"][2]

myList = [correct,incorrect1,incorrect2,incorrect3]
random.shuffle(myList)

print(question)
print("1",html.unescape(myList[0]))
print("2",html.unescape(myList[1]))
print("3",html.unescape(myList[2]))
print("4",html.unescape(myList[3]))

if int(input("Enter your Answer: "))-1 == myList.index(correct):
    print("Correct!")
else:
    print("Thats not it")
