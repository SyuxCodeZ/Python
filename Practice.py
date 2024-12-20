#the input fields

operator = (input("Enter The Operator(+ - * /): "))

num1 = float(input("Enter The 1st Number: "))

num2 = float(input("Enter The 2nd Number: "))

#the results

if operator == "+":
    
    result = num1 + num2

    print (round(result, 3))

elif operator == "-":

    result = num1 - num2

    print (round(result, 3))

elif operator == "*":

    result = num1 * num2

    print (round(result, 3))

elif operator == "/":

    result = num1 / num2

    print (round(result, 3))

else: print(f"{operator} Is Not Valid")