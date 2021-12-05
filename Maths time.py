name = input("Enter our name to begin")
print("Hey there " + name, "welcome to Maths time")

num1 = float(input("Enter a number"))
op = input("Choose your operator")
num2 = float(input("Enter another number"))
if op == "+":
    print(num1 + num2),
elif op == "-":
    print(num1 - num2),
elif op == "*":
    print(num1 * num2),
elif op == "/":
    print(num1 / num2),
else:
    print("Syntax Error")
