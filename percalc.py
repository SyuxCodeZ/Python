# the inputs

operator = input("Enter An Operator (+ - * /): ")

num1 = float(input("Enter The 1st Number: "))

num2 = float(input("Enter The 2nd Number: "))

# the results

if operator == "+":

    result = num1 * num2

    result = int(result)

    print(result)

elif operator == "-":

    result = num1 - num2

    result = int(result)

    print(result)

elif operator == "*":

    result = num1 * num2

    result = int(result)

    print(result)

elif operator == "/":

    result = num1 / num2

    result = int(result)

    print(result)

#the errror message

else:

    print(f"{operator} Is Not A Valid Operator")