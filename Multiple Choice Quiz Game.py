#This game ask multiple choice question about Canada. The game will also keep track of the score and it is going to print it at the end.

import time

#Welcome the user
print("Welcome to the Simple Quiz Game!")
time.sleep(1)

#Chances
chances = 1
print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)

#Score
score = 0

#question number 1
question_1 = print("1) What day is Canada Day?\n(a) July 4\n(b) July 2\n(c) July 1\n(d) July 3\n\n ")
answer_1 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_1, "\n\n")

time.sleep(2)

#question number 2
question_2 = print("2) What is the capital of Canada?\n(a) Toronto\n(b) Montreal\n(c) Vancouver\n(d) Ottawa\n\n ")
answer_2 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_2, "\n\n")

time.sleep(2)

#question number 3
question_3 = print("3) What is the largest city of Canada?\n(a) Quebec\n(b) Toronto\n(c) Vancouver\n(d) Winnipeg\n(e) Edmonton\n(f) Montreal\n\n ")
answer_3 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_3, "\n\n")

time.sleep(2)

#question number 4
question_4 = print("4) How many provinces does Canada have?\n(a) 5\n(b) 6\n(c) 10\n(d) 12\n\n ")
answer_4 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_4, "\n\n")

time.sleep(2)

#question number 5
question_5 = print("5) What is Canada's national animal?\n(a) Beaver\n(b) Canadian Horse\n(c) Moose\n(d) Goose\n\n ")
answer_5 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_5, "\n\n")

time.sleep(1)

#print the score
while score >= 4:
    print("Well done! Your score was", score)
    break

while score <= 3:
    print("Better luck next time! Your score was", score)
    break
#Goodbye message
print("Thank you for playing the Simple Quiz Game!")