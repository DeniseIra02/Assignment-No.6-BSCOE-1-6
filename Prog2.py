print("---------------------------------")
print("Hi, Good day!")
print("Welcome to ADDITION QUIZ!")
print("---------------------------------")
print("Please answer the questions below:")
print("---------------------------------")

import operator
import random 

u_quest = {}
k_score = 0

for adding in range(10):
    num_a = random.randint (0,99)
    num_b = random.randint (0,99)
    operator = '+'
    _operator = operator
    your_quest = str(num_a)+' '+str(_operator)+' '+str(num_b)
    answer = eval(your_quest)
    your_quest += ': '

    u_quest.update({your_quest: str(answer)})

for ans in u_quest.keys():
    your_ans = input(ans)
    if u_quest.get(ans) == str(your_ans):
        k_score += 1
        print("You're CORRECT!")
    else:
        print("Sorry, Your answer is WRONG!")

print('Your score: '+str(k_score)+'/10.')