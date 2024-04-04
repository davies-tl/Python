'''
Program name: AverageWeightedGrade.py
Programmer: Tyler Davies
Date: 10-3-21
Algorithm:
    Analysis -> Given three test scores, one quiz score, and a score for programming assignments,
                calculate the average weighted grade for a student.
    Input ->    Student's name
                3 test scores (60% of the grade)
                1 quiz (10% of the grade)
                1 score for programming assignments (30% of the grade)
    Process ->  Prompt user for input values (verify scores are digits between 0-100; use if statements)
                Calculate the average (times each score by their weighted percents and add for total)
                Assign letter grade using the following table:
                    Average   Grade
                    90 -100	A
                    80 - 89	B
                    70 - 79	C
                    60 - 69	D
                    0 - 59	F
    Output ->   If input data is invalid, print an error message and stop the program.
                Print the results and student data in a formatted report (samples provided).
                Page format (all labels and values lined up, and real numbers have only 2 decimals points.
'''

name = input('Enter student name      :   ')

try:
    test1 = int(input('Enter first exam score  :   '))
except:
    print('Test score 1 is not valid, must be all digits.\nProgram stopped working.')
    exit()
if test1 < 0 or test1 > 100:
    print('Test score 1 is not valid, must be between 0 - 100 inclusive.\nProgram stopped working.')
    exit()

try:
    test2 = int(input('Enter second exam score :   '))
except:
    print('Test score 2 is not valid, must be all digits.\nProgram stopped working.')
    exit()
if test2 < 0 or test2 > 100:
    print('Test score 2 is not valid, must be between 0 - 100 inclusive.\nProgram stopped working.')
    exit()

try:
    test3 = int(input('Enter third exam score  :   '))
except:
    print('Test score 3 is not valid, must be all digits.\nProgram stopped working.')
    exit()
if test3 < 0 or test3 > 100:
    print('Test score 3 is not valid, must be between 0 - 100 inclusive.\nProgram stopped working.')
    exit()

try:
    quiz = int(input('Enter quiz score        :   '))
except:
    print('Quiz score is not valid, must be all digits.\nProgram stopped working.')
    exit()
if quiz < 0 or quiz > 100:
    print('Quiz score is not valid, must be between 0 - 100 inclusive.\nProgram stopped working.')
    exit()

try:
    programScore = float(input('Programming total       :   '))
except:
    print('Programming assignment score is not valid, must be all digits.\nProgram stopped working.')
    exit()
if programScore < 0 or programScore > 100:
    print('Programming assignment score is not valid, must be between 0 - 100 inclusive.\nProgram stopped working.')
    exit()

averageTest = (test1 + test2 + test3) / 3
finalGrade = (averageTest * 0.60) + (quiz * 0.10) + (programScore * 0.30)

if finalGrade >= 90:
    letter = 'A'
elif finalGrade >= 80:
    letter = 'B'
elif finalGrade >= 70:
    letter = 'C'
elif finalGrade >= 60:
    letter = 'D'
else:
    letter = 'F'

print('\nHello {}, here is your report:'.format(name))
print('              Test Scores:        {}, {}, {}'.format(test1, test2, test3))
print('              Test Average:       {:.2f}'.format(averageTest))
print('              Quiz Score:         {}'.format(quiz))
print('              Programming Score:  {:.2f}'.format(programScore))
print('              Grade Average:      {:.2f}'.format(finalGrade))
print('              Letter Grade:       {}'.format(letter))

exit()

