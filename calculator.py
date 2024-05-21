#import sys library
import sys
#let user know that they need Python 3 to run program
print('Before continuing you must have Python 3 to run this program')
#Asks users to select from the list to decide which program they would like to run
print('Please select which type of math problem you would like to run')
print('[1] Addition\n[2] Subtraction\n[3] Division\n[4] Multiplication\n[5] Power of X\n[0] Exit Program')

#Takes the input from the user from the list provided
math = int(input('Enter number for the type of Math problem please: '))
equation = ''
#Checks if they select 0 and tells them goodbye and exits program
if math == 0:
    print('Goodbye!')
    sys.exit()
elif math == 1:
    print('You selected ADDITION')
elif math == 2:
    print('You selected SUBTRACTION')
elif math == 3:
    print('You selected DIVISION')
elif math == 4:
    print('You selected MULTIPLICATION')
elif math == 5:
    print('You selected TO THE POWER OF X')
elif math > 5:
    print('Sorry, that is not a selection.')
    sys.exit()
firstNumber = int(input('Enter first number: '))
print('You entered: ', firstNumber)
secondNumber = int(input('Enter second number (if you selected 5 this will be the exponent): '))
print('You entered: ', secondNumber)

if math == 1:
    answer = firstNumber + secondNumber #Adding both numbers
    equation = 'plus'
elif math == 2:
    answer = firstNumber - secondNumber #Subtracting both numbers
    equation = 'minus'
elif math == 3:
    answer = firstNumber / secondNumber #Dividing both Numbers
    equation = 'divided by'
elif math == 4:
    answer = firstNumber * secondNumber #Multiplying both Numbers
    equation = 'times'
elif math == 5:
    answer = firstNumber ** secondNumber #Rasing to the power of X
    equation = 'to the power of'
    

print(firstNumber, equation, secondNumber, 'equals', answer)
                    
