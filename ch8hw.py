
# The program should read the student’s answers for each of the 20 questions from a text file and store the
# answers in another list. (Create your own text file to test the application.)
# After the student’s answers have been read from the file, the program should display
# a message indicating whether the student passed or failed the exam.
# (A student must correctly answer 15 of the 20 questions to pass the exam.)
# It should then display the total number of correctly answered questions, the total number of incorrectly
# answered questions, and a list showing the question numbers of the incorrectly answered question


# Store Answer key in a list.
key = ['B','D','A','A','C',
       'A','B','A','C','D',
       'B','C','D','A','D',
       'C','C','B','D','A']

# Student answers
student_answers = ['C','D','A','A','C',
                   'A','B','C','C','D',
                   'B','C','D','A','A',
                   'D','C','B','A','A']

# Saved Student answers into student_answer file as a string.
#Opens and closes the file.
with open('student_answers.txt', 'w') as answers:
    for letter in student_answers:
        answers.write(letter + '\n')

# reading answers from the student_answer file.
#opens file and assigns each answer to another list.
answers = open('student_answers.txt', 'r')
a = []
for letter in answers:
    letter = answers.readlines()
    a.append(letter)

#deteriming if the lists match.
for a not in key:
    wrong_answers = []
    a.append(wrong_answers)
    if wrong_answers >= wrong_answers.index(4):
        print('Test Failed.')
        print(a.index(wrong_answers))
    else:
        print('Test Passed!')

answers.close()




