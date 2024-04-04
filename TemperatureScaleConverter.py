'''

Program Name: TemperatureScaleConverter.py

Programmer: Tyler Davies

Date: 10-27-21

Version: 1.0

Algorithm:

    Analysis -> Write a program that asks the user if they would like to use a scale that (1) converts

                Fahrenheit to Celsius, or (2) converts Celsius to Fahrenheit. It then produces a table

                based on the given starting temperature, ending temperature, and increment amount.

    Design ->

        Input => choice (1 or 2; decides which scale to use)

                 start_temp (float; starting temperature)

                 end_temp (float; ending temperature)

                 temp_incr (float; increment amount)

        Process => Display menu (function 1)

                   Prompt user for choice (function 2)

       	           Prompt user for input values (function 3)

                   Display a two column F to C table or a two column C to F table (based on choice)

                   If choice 1: (function 4)

                   - first column labeled Fahrenheit (first value is start_temp)

                   - second column labeled Celsius (calculate using formula: C=(5.0/9.0)*(F–32.0))

                   If choice 2: (function 5)

                   - first column labeled Celsius (first value is start_temp)

                   - second column labeled Fahrenheit (calculate using formula: F=9.0/5.0*C+32.0)

                   Input data should be checked and validated. (function 6)

        Output => Display organized table; values increment by temp_incr, and end when the table value

                  would exceed end_temp. Display all values with 2 decimal of accuracy, justified and aligned.

                  If input is invalid, print an error message and terminate program.

'''



#This function prints the menu, and calls/returns the function chooseScale.

def printMenu():

    print('Choose a conversion type:\n             1. Convert F to C\n' +

          '               2. Convert C to F\n\n               What is your choice?\n')

    return chooseScale()



#This function checks to make sure the menu choice is valid. It returns the selection if it is valid.

def chooseScale():
        selection = input()

    if not(selection.isdigit()):

        print('Invalid data type, must be a number. Program terminated.')

        exit(0)

    selection = int(selection)

    if selection != 1 and selection != 2:

        print('Invalid choice. Program terminated.')

        exit(0)

    else:

        return selection



#This function prompts the user for each input data, sending them to the validateInput function

#to make sure the input is valid. The data is converted to a float, and returned via a tuple.

def getUserData():

    start_temp = input('Enter starting value (integer number):\n')

    validateInput(start_temp)

    start_temp = float(start_temp)


    end_temp = input('Enter ending value (integer number):\n')

    validateInput(end_temp)

    end_temp = float(end_temp)


    
temp_incr = input('Enter increment value (real number):\n\n')

    validateInput(temp_incr)

    temp_incr = float(temp_incr)


    
return start_temp, end_temp, temp_incr



#This function checks to make sure the input is a valid float, by checking each element in

#the string to make sure it is either a digit, a decimal point, or a negative sign.

def validateInput(user_val):

    for i in user_val:

        if i.isdigit() or i == '.' or i == '-':

            continue

        else:

            print('Invalid data type, must be a number. Program terminated.')

            exit(0)



#This function prints and calculates the Fahrenheit to Celsius table, which increments.

def fahrenheitToCelsius(start, end, incr):

    print('Fahrenheit          Celsius\n')

    i = start

    while i <= end:

        f = i

        c = (5.0 / 9.0) * (f - 32.0)

        if c < 0:

            print('{:.2f}               {:.2f}'.format(f, c))

        else:

            print('{:.2f}                {:.2f}'.format(f, c))

        i += incr



#This function prints and calculates the Celsius to Fahrenheit table, which decrements.

#It first checks that the decremental variable is negative, or terminates the program.

def celsiusToFahrenheit(start, end, decr):

    if decr > 0:

        print('Invalid range. Program terminated.')

        exit(0)

    print('Celsius             Fahrenheit\n')

    i = start

    while i >= end:

        c = i

        f = 9.0 / 5.0 * c + 32.0

        print('{:.2f}               {:.2f}'.format(c, f))

        i += decr



#The interpreter will set variable __name__ to '__main__' if source file is executed as the main program.

if __name__ == '__main__':

    choice = printMenu()

    start_temp, end_temp, temp_incr = getUserData()

    if choice == 1:

        fahrenheitToCelsius(start_temp, end_temp, temp_incr)

    else:

        celsiusToFahrenheit(start_temp, end_temp, temp_incr)

    exit(0)