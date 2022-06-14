total = 0
print ('1. Enter numbers')
print ('2. Sum numbers ')
print ('3. Exit the program')

option = int(input('Choose an option: '))

number = int(input('Enter a number: ' ))
    
while option == 1 and number != 0:
    total += number
    number = int(input('Enter a number: '))
option = int(input('Choose an option: '))

if option == 2:
    print ('Sum of numbers equal to: ' + str(total))
option = int(input('Choose an option: '))

if option == 3:
    print ('Bye! See you later!')
