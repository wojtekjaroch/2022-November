def ask_for_num1():
    num1 = None
    while num1 is None:
        try:
            num1 = float(input("Enter the first value: "))
        except ValueError:
            exit()
    return num1  


def valid_operator():
    while True:
        operator = input("Please provide an operator (one of +, -, *, /)! ")
        if operator == '+':
            # print(operator)=======================> konsultacje
            return operator
        elif operator == '-':
            return operator
        elif operator == '*':
            return operator
        elif operator == '/':
            return operator    
        else:
            print(f"{operator} is an invalid operator! ")


def ask_for_num2():
    num2 = None
    while num2 is None:
        try:
            num2 = float(input("Enter the second value: "))
        except ValueError:
            print("Invalid number, try again!")
    return num2

def operator():
    operator = input("Enter a proper operator: +, -, *, / !")
    return operator

def calculation(num1, operator, num2):

    # print("Provide your first value!")
    # first_number = ask_for_num1
    # print("Provide operator!")
    # operator = ask_for_operator
    # print("Provide your second value!")
    # second_number = ask_for_num2
    # print(operator)=======================> konsultacje
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero")
            return None
    return result  
   

#    answer = input("Do you want to continue? Y / N")
#     if answer == ("Y"):
#         simple_calculator()
#     elif answer == ('N'):
#         exit()
#     else:
#         print("Do you want to continue? Y / N") 


def simple_calculator():
    num1 = ask_for_num1()
    operator = valid_operator()
    num2 = ask_for_num2()

    result = calculation(num1, operator, num2)
    print (f"Result is {result}")

 
simple_calculator()




   
