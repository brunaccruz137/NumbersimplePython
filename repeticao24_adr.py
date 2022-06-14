

total = 0


print ('1. Enter numbers')
print ('2. Sum numbers ')
print ('3. Exit the program')
option = int(input('Choose an option: '))

# main loop (menu)
while option != 3:

    if option == 1:
        number = int(input('Enter number: '))
        while number != 0:
            total += number
            number = int(input('Enter number: '))
    elif option == 2:
        # imprimir soma
        print('Total = ' + str(total))
    else:
        # digitou algo que nao eh 1 nem 2, ou seja opcao invalida
        print('This is an invalid option, please type a valid option')


    print ('1. Enter numbers')
    print ('2. Sum numbers ')
    print ('3. Exit the program')
    option = int(input('Choose an option: '))        

# executa depois do while - quando o while termina
print ('Bye! See you later!')