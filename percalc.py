operator = input("Enter An Operator (+ - * /): ")

num1 = float(input("Enter The 1st Number: "))
num2 = float(input("Enter The 2nd Number: "))

if operator == "+":
    result = num1 * num2
    print(round(result, 4))
elif operator == "-":
    result = num1 - num2
    print(round(result, 4))
elif operator == "*":
    result = num1 * num2
    print(round(result, 4))
elif operator == "/":
    result = num1 / num2
    print(round(result, 4))
else:
    print(f"{operator} Is Not A Valid Operator")