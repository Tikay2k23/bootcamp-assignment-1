num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}" if num2 != 0 else "Division by zero is not allowed")
print(f"{num1} % {num2} = {num1 % num2}" if num2 != 0 else "Modulo by zero is not allowed")
print(f"{num1} ** {num2} = {num1 ** num2}")
"wow"