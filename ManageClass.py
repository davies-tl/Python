'''
Program name: ManageClass.py
Programmer:  Tyler Davies
Date: 12-16-21
Algorithm:
    Analysis -->  This program prompts the user for a file name, and reads/processes a course's student data. It then
                  calculates the students' average grade, and prints a report for the user. There are included features
                  to add, update, and remove a student.
    Design -->
        Input   - File containing the following information (names and IDs are unique).
                      Course_Name
                      Course_Id
                      Location
                      First Last
                      ID Quiz Test1 Test2 Test3 Test4 Test5 Test6

        Process - Prompt user for input file, read and store course information in a dictionary.
                      Name (Course Name)
                      ID (Course ID)
                      Location
                      List of Student Dictionaries (name, ID, test scores list, quiz score, letter grade, and average)
                      Class Average
                - Process data
                      Verify all scores are between 0-100; if not, set average to -1 and letter grade to I.
                      Calculate average using the highest five test scores (worth 90%) and the quiz score (worth 10%).
                      Assign letter grade using the following grading scale.
                          Average   Grade
                          90-100    A
                          80-89.9   B
                          70-79.9   C
                          60-69.9   D
                          0-59.9    F        
                - Print course content to the monitor (sample output below).
                - Search for a student using partial or full last name (not case sensitive), and print the details.
                - Add a new student to the list, prompting user for appropriate data; do not add duplicates.
                      When adding a new student, the data must be pick up in the following order:
                          Last name
                          First name
                          ID
                          Quiz score
                          Six test scores (one per line)
                - Remove a student from the list using last name.
                - Sort the list of students alphabetically (by last name) and print to the monitor.
                - Prompt user for output file and print course content to file.
                - Edit a student's data.
                      Prompt user for student's last name ("Enter last name:").
                      If not found, output an error ("Error: Smith is not on the list.").
                      If found, print menu.
                          ("To change quiz score enter 1:
                            To change a test score enter 2:
                            To exit enter 3:")
                      If choice 2 is selected, print the list of scores and indexes; allow user to select a test.
                          ("Test #        Score
                                 0        100.00
                                 1        80.00
                                 2        70.00
                                 3        50.00
                                 4        100.00
                                 5        90.00
                            Enter test number to change:
                            Enter new score:")
                - Before terminating the program, prompt user for an input file name to update and save for later use.    
                                
        Output - Provided Output File Sample.
                     Course Name:       Introduction to Computer Programming Fundamentals 
                     Course ID:         CSCI 1
                     Class Location:    MBA 315

                     Name               ID               Average      Grade
                     Adams, John        111-22-3333      91.5         A
                     Smith Jr., Willy   222-11-4444      87.0         B
                     Jordan, Phil       777-88-6666     -1            I

                     Class Average for 2 students is:    89.25

               - Provided Monitor Output Sample.
                     Name               Average    Grade
                     Adams, John        91.5        A
                     Smith Jr., Will    87.0        B
                     Jordan, Phil       -1          I
'''

#The openFile function prompts the user for an input file, and saves the course information. It calls saveStudentData.
def openFile():
    course = {'courseName': '', 'courseID': '', 'location': '', 'students': list(), 'classAverage': 0}
    myFile = input('Enter input file name:\n')
    print()    #print newline for formatting 
    try:
        file = open(myFile)
        course['courseName'] = file.readline().strip('\n')
        if course['courseName'] == '':    #Checks if courseName is empty, if so raises EOFError.
            raise EOFError
    except FileNotFoundError:
        print('Error: file {} does not exist.'.format(myFile))
        exit(0)
    except EOFError:
        print('Error: Data file {} is blank.'.format(myFile))
        exit(0)   
    course['courseID'] = file.readline().strip('\n')
    course['location'] = file.readline().strip('\n')   
    course['students'] = saveStudentData(file, course['students'])
    file.close()
    return course

#The saveStudentData function saves the students' information in a list of dictionaries (within the course dictionary).
def saveStudentData(myFile, students):
    name = myFile.readline().strip('\n')
    while name != '':
        student = {}
        index = name.index(' ')
        student['firstName'] = name[:index]
        student['lastName'] = name[(index + 1):]       
        information = myFile.readline().strip('\n').split()
        student['studentID'] = information[0]
        try:
            student['quiz'] = int(information[1])
        except ValueError:
            student['quiz'] = -1            
        student['tests'] = information[2:]       
        #remove 7th test if found (needed in order to match the sample output on zyBooks).
        if len(student['tests']) == 7:
            student['tests'].pop(-1)
        size = len(student['tests'])
        i = 0
        while i < size:
            try:
                student['tests'][i] = int(student['tests'][i])
            except ValueError:
                student['tests'][i] = -1
            i += 1            
        student['average'] = 0    #temporary value
        student['grade'] = ' '    #temporary value
        students.append(student)      
        name = myFile.readline().strip('\n')
    return students   

#The processStudents function iterates through the student list, passing each student to processAverage and
#processLetterGrade.
def processStudents(students):
    size = len(students)
    i = 0
    while i < size:
        students[i] = processAverage(students[i])
        students[i] = processLetterGrade(students[i])
        i += 1    
    return students

#The processAverage function passes a student's quiz and test scores to verifyScore. If all scores are valid, it then
#calculates the average for the student; otherwise, it sets average to -1.
def processAverage(student):
    if verifyScore(student['quiz']) == False:
        student['average'] = -1
        return student
    else:
        i = 0
        while i < 6:
            if verifyScore(student['tests'][i]) == False:
                student['average'] = -1
                return student
            i += 1
        else:
            student['average'] = (student['quiz'] * 0.1) + (((sum(student['tests']) - min(student['tests'])) / (len(student['tests']) - 1)) * 0.9)
            return student

#The verifyScore function checks that a score is between 0-100; and returns True if valid, otherwise it returns False.
def verifyScore(score):
    if score < 0 or score > 100:
        return False
    else:
        return True

#The processLetterGrade uses the students' average to calculate their letter grade. If the average is -1, it sets the
#letter grade to I.
def processLetterGrade(student):
    if student['average'] >= 90 and student['average'] <= 100:
        student['grade'] = 'A'
    elif student['average'] >= 80 and student['average'] < 90:
        student['grade'] = 'B'
    elif student['average'] >= 70 and student['average'] < 80:
        student['grade'] = 'C'
    elif student['average'] >= 60 and student['average'] < 70:
        student['grade'] = 'D'
    elif student['average'] >= 0 and student['average'] < 60:
        student['grade'] = 'F'
    else:
        student['grade'] = 'I'
    return student 

#The addStudent function prompts the user for a new student's last name. It then calls the searchStudent to make sure
#student is not already in the dictionary; no duplicates are added. If student is not in the dictionary, it prompts the
#user for the new student's first name, ID, quiz score, and test scores. It adds the student to the dictionary.
def addStudent(students):
    last = input('\nEnter student\'s last name to add student to the course:\n')
    size = len(students)    #addStudent searches the list itself, since searchStudent allows for partial search.
    i = 0
    while i < size:
        if last.lower() == students[i]['lastName'].lower():
            print('Error: {} is on the list, duplicates are not allowed.'.format(last))
            return students
        i += 1
    first = input('Enter student\'s first name:\n')
    ID = input('Enter student\'s ID:\n')
    try:
        quizScore = int(input('Enter student\'s quiz score:\n'))
    except ValueError:
        quizScore = -1    
    testScores = []
    i = 0
    while i < 6:
        try:
            grade = int(input('Enter student\'s test score {}:\n'.format(i + 1)))
        except:
            grade = -1            
        testScores.append(grade)
        i += 1
    students.append({'firstName': first, 'lastName': last, 'studentID': ID, 'quiz': quizScore, 'tests': testScores, \
                     'average': 0, 'grade': ' '})
    print('{} has been added to the list.'.format(last))
    students[-1] = processAverage(students[-1])
    students[-1] = processLetterGrade(students[-1])    
    return students

#The removeStudent function prompts the user for a student's last name. If found, student is removed.
def removeStudent(students):
    last = input('\nEnter student\'s last name to remove student from the course:\n')
    index = searchStudent(students, last)
    if index != None:
        print('{} has been removed from the list.\n'.format(students[index]['lastName']))
        students.pop(index)
    else:
        print('Error: {} is not on the list.\n'.format(last))
    return students

#The editStudent function prompts the user for a student's last name. If found, it prints a menu and asks the user to
#choose whether to update the quiz or a test score. If the test scores option is chosen, it calls the printTestScores
#function and asks the user to choose which test to update.
def editStudent(students):
    try:
        last = input('Enter student\'s last name to edit student:\n')    #Changed prompt, so user knows they are editting.
    except EOFError:
        #Have to include in a try block, because zyBooks is not expecting the extra credit.
        return
    index = searchStudent(students, last)
    if index == None:
        print('Error: {} is not on the list.\n'.format(last))
        return students
    else:
        choice = int(input('To change quiz score enter 1:\nTo change a test score enter 2:\nTo exit enter 3:\n'))
        if choice == 1:
            try:
                students[index]['quiz'] = int(input('Enter new score:\n'))
            except ValueError:
                students[index]['quiz'] = -1            
        elif choice == 2:
            printTestScores(students[index]['tests'])
            testIndex = input('Enter test number to change:\n')
            try:
                students[index]['tests'][testIndex] = int(input('Enter new score:\n'))
            except ValueError:
                students[index]['tests'][testIndex] = -1            
        elif choice == 3:
            pass    #pass is ignored by the interpreter; allows for "do nothing"
        else:
            print('Error: selection not recognized!')
    processAverage(students[index])
    processLetterGrade(students[index])
    return students

#The search function prompts the user for a student's last name, and passes the student list and last name to the
#searchStudent function. If the student is found, printStudent is called; else an error message is displayed.      
def search(students):
    name = input('Enter the last name of the student for which to search:\n')
    index = searchStudent(students, name)  
    if index == None:
        print('Error: {} is not on the list.'.format(name))
    else:
        printStudent(students[index])

#The searchStudent function searches the student list using a partial or full last name; it is not case sensitive. If
#multiple students are found, user will be asked to choose between the choices found. If an invalid choice is seleted
#the program will print an error and no student will be selected.        
def searchStudent(students, name):
    searchList = []
    size = len(students)
    i = 0
    while i < size:
        if name.lower() in students[i]['lastName'].lower():
            searchDict = {}
            searchDict['last'] = students[i]['lastName']
            searchDict['first'] = students[i]['firstName']
            searchDict['index'] = i
            searchList.append(searchDict)
        i += 1
    if len(searchList) > 1:
        print('\nPlease select a student from the following choices:')
        i = 0
        while i < len(searchList):
            print('{} {}, {}'.format(i, searchList[i]['last'], searchList[i]['first']))
            i += 1
        try:
            choice = int(input('Make a selection based on the numbers list.\n'))
            return searchList[choice]['index']
        except (ValueError, TypeError, IndexError):
            print('\nError: invalid choice entered; search terminated.')
            return None            
    elif len(searchList) == 1:
        return searchList[0]['index']
    else:
        return None

#The sortStudents function sorts the student list by students' last name (A-Z); then it calls printToMonitor.
def sortStudents(students):  
    newList = sorted(students, key = checkLastName, reverse = False)
    printToMonitor(newList)
    return newList

#The checkLastName function is used by sorted to check a student's last name for sorting.
def checkLastName(student):
    return student['lastName']

#The printStudent function prints a student's information to the monitor.
def printStudent(student):
    print('\n{}, {}'.format(student['lastName'], student['firstName']))
    print('{:25}{}'.format('Student ID:', student['studentID']))
    print('{:25}{}'.format('Student Test Scores:', student['tests']))
    print('{:25}{:.2f}'.format('Student Quiz Score:', student['quiz']))
    print('{:25}{:.2f}'.format('Student Average:', student['average']))
    print('{:25}{}'.format('Student letter Grade:', student['grade']))

#The printTestScores function prints the list of a student's test scores and their indexes to the monitor.
def printTestScores(tests):
    print('{:14}{}'.format('Test #', 'Score'))
    i = 0
    while i < 6:
        print('{:>6}{:9}{}'.format(i, ' ', tests[i]))

#The printToMonitor function prints all the students' name, average, and letter grade to the monitor.
def printToMonitor(students):
    size = len(students)
    i = 0
    print('{:25}{:15}{}'.format('Name', 'Average', 'Grade'))
    while i < size:
        name = students[i]['lastName'] + ', ' + students[i]['firstName']
        print('{:25}{:<15.2f}{}'.format(name, students[i]['average'], students[i]['grade']))
        i += 1
    print()    #print newline for formatting 

#The printToFile function prints all of the course information to a file.
def printToFile(course):
    fileName = input('Enter file name:\n')
    file = open(fileName, 'w')
    file.write('{:25}{}\n'.format('Course Name:', course['courseName']))
    file.write('{:25}{}\n'.format('Course ID:', course['courseID']))
    file.write('{:25}{}\n'.format('Course Location:', course['location']))
    file.write('\n')
    file.write('{:25}{:15}{:15}{}\n'.format('Name', 'ID', 'Average', 'Grade'))
    size = len(course['students'])
    i = 0
    totalAverage = 0
    invalidAvg = 0
    while i < size:      
        name = course['students'][i]['lastName'] + ', ' + course['students'][i]['firstName']
        file.write('{:25}{:15}{:<15.2f}{}\n'.format(name, course['students'][i]['studentID'], course['students'][i]['average'], \
                                              course['students'][i]['grade']))
        if course['students'][i]['average'] == -1:
            invalidAvg += 1
            i += 1
            continue
        totalAverage += course['students'][i]['average']
        i += 1
    file.write('\n')
    course['classAverage'] = totalAverage / (size - invalidAvg)
    file.write('Class Average for {} students is: {:.2f}'.format((size - invalidAvg), course['classAverage']))
    file.close()
    print()    #print newline for formatting 

#The saveInputFile function saves all of the course information to a file for later use. It is automatically called
#before the program is terminated.
def saveInputFile(course):
    try:
        fileName = input('Enter file name:\n')
    except EOFError:
        #Have to include in a try block, because zyBooks is not expecting the extra credit.
        return
    file = open(fileName, 'w')
    file.write('{} '.format(course['courseName']))
    file.write('{}\n'.format(course['courseID']))
    file.write('{}\n'.format(course['location']))
    size = len(course['students'])
    i = 0
    while i < size:
        file.write('{} {}\n'.format(course['students'][i]['firstName'], course['students'][i]['lastName']))
        file.write('{} {} '.format(course['students'][i]['studentID'], course['students'][i]['quiz']))
        j = 0
        while j < 6:
            file.write('{}'.format(course['students'][i]['tests'][j]))
            if j == 5:
                break
            file.write(' ')
            j += 1
        i += 1
        file.write('\n')
    file.close()

#The interpreter will set variable __name__ to '__main__' if source file is executed as the main program.
if __name__ == '__main__':    
    myCourse = openFile()                                              #open input file
    myCourse['students'] = processStudents(myCourse['students'])       #verify scores, calculate averages and letter grades
    printToMonitor(myCourse['students'])                               #print to monitor
    search(myCourse['students'])                                       #search for a student
    myCourse['students'] = addStudent(myCourse['students'])            #add a student
    myCourse['students'] = removeStudent(myCourse['students'])         #remove a student
    myCourse['students'] = sortStudents(myCourse['students'])          #sort students A to Z
    printToFile(myCourse)                                              #save output file
    myCourse['students'] = editStudent(myCourse['students'])           #edit a student
    saveInputFile(myCourse)                                            #save input file
    exit(0)
