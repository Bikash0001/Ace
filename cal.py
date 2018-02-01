print("Calculation of two numbers")
i = 0
while i != 1:
    a = float(input('Enter a number : '))
    b = float(input('Enter a number : '))
    c = input('Enter the operation "+,-,*,/,**,% to operate : ')
    i = i + 1
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '/':
        print(a / b)
    elif c == '*':
        print(a * b)
    elif c == '**':
        print(a ** b)
    elif c == '%':
        print(a % b)
    else:
        i = int(input("Wrong choice please try again by pressing 0 : "))
    
    

