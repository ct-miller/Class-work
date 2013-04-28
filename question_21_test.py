
def calc_average(grades):
    return float(sum(grades) / len(grades))

def determine_grade(grades):
    for l in grades:
        if l >= 90 and l <= 100:
            print('A')
        elif l >= 80 and l <= 89:
            print('B')
        elif l >= 70 and l <= 79:
            print('C')
        elif l >= 60 and l <= 69:
            print('D')
        elif l <= 59:
            print('F')


grades = []

try:
    for g in range(5):
        grades.append(float(input('Enter a test grade: ')))
        determine_grade(grades)

except ValueError:
    print('Not a valid entry.', '\n')

finally:
    average = calc_average(grades)
    print("The average is {}".format(average))
