

#Write a program that gives simple math quizzes.
# The program should display two random numbers that are to be added, such as:
#247 + 129
#The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect, a message showing the correct answer should be displayed.


import random

#generate a random number
def generate_random_int(min=99,max=300):
    return random.randint(min,max)

#function to give addition problem
def give_addition_problem():
    num_1 = generate_random_int()
    num_2 = generate_random_int()
# Give addition problem.
    print('Enter the sum of these two numbers: ', num_1, 'and', num_2, '\n')
    result = num_1 + num_2
    answer = int(input('Enter your answer: '))
    check_answer(result, answer)

# function that gives the correct answer or congratulations.
def check_answer(r, a):
    if r != a:
        print('The answer is incorrect. The correct answer is: ', r)
    elif r == a:
        print('Congratulations!')

give_addition_problem()






#check_answer(give_addition_problem())


