'''
Program name: CalculateInterestRate.py
Programmer: Tyler Davies
Date: 10-14-21
Algorithm:
    Analysis -> Given a person's full name, amount of deposit, number of years on deposit,
                and the account code, calculate the interest rate and print a report.
    Input ->    First Name
                Deposit Amount
                Years
                Account Code
                (No need to verify data types, but check that digits are not negative numbers;
                if negative, print an error message and terminate the program).
    Process ->  5 Functions (getUserData, deCode, findInterest, calcInterestEarned, and printReport).
                6 Functions including the main function.
		Determine interest to be paid based on the following schedule:
                    Time on Deposit                     Interest Rate
                    >= 5 years                          4.5%
                    Less than 5 and >=4 years           4%
                    Less than 4 and >=3 years           3.5%
                    Less than 3 and >=2 years           2.5%
                    Less than 2 and >=1 years           2%
                    Less than 1 year                    1.5%
                Determine number of times compound interest is calculated and paid per year,
                depending on the code passed using the following table:
                    Code        Number of times calculated
                    A           4
                    B           2
                    C           1
                    D           12
                    E           365
                Calculate the interest using this formula: A = P(1+ r/n)^nt
                    P = principal amount (the initial amount you borrow or deposit)
                    r  = annual rate of interest (as a decimal)
                    t  = number of years the amount is deposited for
                    A = amount of money accumulated after n years, including interest
                    n  =  number of times the interest is compounded per year
    Output ->   Output a report with the depositor's name, years, original deposit, interest
                earned, and the new balance with the interested added to the deposit.
'''

# This function prompts the user for their name, deposit amount, years, and interest code; and returns a
# tuple. It checks to make sure deposit amount is positive, or prints an error and terminates the program.
def getUserData():
    name = input('Enter the depositor\'s name:\n')
    deposit = float(input('Enter deposit amount:\n'))
    if deposit <= 0:
        print('Invalid deposit must be greater than 0.')
        exit()
    years = int(input('Enter number of years:\n'))
    code = input('Enter compound interest code (A-E):\n')
    return name, deposit, years, code

# This function accepts a string code as its parameter, and returns the number of times per year
# interest is calculated. If code is not A-E or a-e, it prints an error and terminates the program.
def deCode(code):
    if code == 'A' or code == 'a':
        return 4
    elif code == 'B' or code == 'b':
        return 2
    elif code == 'C' or code == 'c':
        return 1
    elif code == 'D' or code == 'd':
        return 12
    elif code == 'E' or code == 'e':
        return 365
    else:
        print('Invalid code, must be A-E.')
        exit()

# This function accepts an integer for number of years and returns the interest rate percentage,
# represented as a decimal. If years is a negative number, it prints an error and terminates the program.
def findInterest(years):
     if years >= 5:
        return 0.045
    elif years < 5 and years >= 4:
        return 0.04
    elif years < 4 and years >= 3:
        return 0.035
    elif years < 3 and years >= 2:
        return 0.025
    elif years < 2 and years >= 1:
        return 0.02
    elif years < 1 and years > 0:
        return 0.015
    else:
        print('Invalid years, must be greater than 0.')
        exit()

# This function accepts parameters for the principal amount, interest rate, years, and number of times
# interest is compounded per year. It calculates and returns the total amount with interest earned.
def calcInterestEarned(principal, interestRate, years, numTimesCompound):
    return principal * (1 + (interestRate / numTimesCompound)) ** (numTimesCompound * years)

# This function accepts parameters for the user's name, years on the deposit, initial deposit
# amount, and total amount after interest earned. It prints a report for the user.
def printReport(name, years, deposit, total):
    print('Name                    Years      Deposit Amount   Interest Earned      Total')
    print('{}        {:.2f}       ${:.2f}            ${:.2f}           ${:.2f}'.format(name, years, deposit, total - deposit, total)
)

# This is the main function. It will run if the source file is executed as the main program (see if statement).
def main():
    name, deposit, years, code = getUserData()
    compound = deCode(code)
    interestRate = findInterest(years)
    total = calcInterestEarned(deposit, interestRate, years, compound)
    printReport(name, years, deposit, total)
    exit()

# Interpreter will set variable __name__ to '__main__' if source file is executed as the main program.
if __name__ == '__main__':
    main()