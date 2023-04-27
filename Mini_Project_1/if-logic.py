#!/usr/bin/python3

from os import system, name

quiz = [
        {"prompt":"Do you repeatedly lie to or trick others for your own gain or pleasure?",
         "choices":"1. Very Inaccurate\n2. Moderately Inaccurate\n3. Neither Inaccurate nor Inaccurate\n4. Moderately Accurate\n5. Very Accurate"
         },
        {"prompt":"Do you act impulsively?",
         "choices":"1. Very Inaccurate\n2. Moderately Inaccurate\n3. Neither Inaccurate nor Inaccurate\n4. Moderately Accurate\n5. Very Accurate"
         },
        {"prompt":"Do you fail to plan ahead?",
         "choices":"1. Very Inaccurate\n2. Moderately Inaccurate\n3. Neither Inaccurate nor Inaccurate\n4. Moderately Accurate\n5. Very Accurate"
         },
        {"prompt":"Do you consistently fail to fulfill work obligations?",
         "choices":"1. Very Inaccurate\n2. Moderately Inaccurate\n3. Neither Inaccurate nor Inaccurate\n4. Moderately Accurate\n5. Very Accurate"
         },
        {"prompt":"Do you consistently fail to fulfill financial obligations?",
        "choices":"1. Very Inaccurate\n2. Moderately Inaccurate\n3. Neither Inaccurate nor Inaccurate\n4. Moderately Accurate\n5. Very Accurate"
         },
        {"prompt":"Have you ever engaged in criminal behavior?",
        "choices":"1. Very Inaccurate\n2. Moderately Inaccurate\n3. Neither Inaccurate nor Inaccurate\n4. Moderately Accurate\n5. Very Accurate"
         },
        {"prompt":"Do you find yourself unable to empathize with others dealing with difficult situations?",
        "choices":"1. Very Inaccurate\n2. Moderately Inaccurate\n3. Neither Inaccurate nor Inaccurate\n4. Moderately Accurate\n5. Very Accurate"
         },
        {"prompt":"If you hurt someone else’s feelings, do you lack remorse or guilt?",
        "choices":"1. Very Inaccurate\n2. Moderately Inaccurate\n3. Neither Inaccurate nor Inaccurate\n4. Moderately Accurate\n5. Very Accurate"
         },
        {"prompt":"Are you aggressive?",
        "choices":"1. Very Inaccurate\n2. Moderately Inaccurate\n3. Neither Inaccurate nor Inaccurate\n4. Moderately Accurate\n5. Very Accurate"
         },
        {"prompt":"Do you engage in unnecessary risk-taking or dangerous behavior with no regard for the safety of self or others?",
        "choices":"1. Very Inaccurate\n2. Moderately Inaccurate\n3. Neither Inaccurate nor Inaccurate\n4. Moderately Accurate\n5. Very Accurate"
         }
       ]
blerb = "Please enter your choice [1-5]: "

answers = []

def validate(choice):
    try:
        choice = int(choice)
    except:
        print("Please enter a number")
        return True
    if choice < 1 or choice > 5:
        print("Please enter 1,2,3,4, or 5")
        return True
    else:
        return False

def result(total):
    if total == 10:
        print("No Inidication of Antisocial Personality Disorder")
    elif 10 < total < 20:
        print("Negligible Indication of Antisocial Personality Disorder")
    elif 20 <= total < 30:
        print("Weak Indication of Antisocial Personality Disorder")
    elif 30 <= total < 40:
        print("Some Indication of Antisocial Personality Disorder")
    elif 40 <= total < 50:
        print("Moderate Indication of Antisocial Personality Disorder")
    elif total == 50:
        print("Strong Indication of Antisocial Personality Disorder")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    for q in quiz:
        clear()
        print(q["prompt"])
        print(q["choices"])
        choice = input(blerb)
        while validate(choice):
            choice = input(blerb)
        answers.append(int(choice))
    clear()
    result(sum(answers))
    input("Press enter to exit...")

if __name__ == "__main__":
    main()
