def divide(a, b):
    count = 0

    while a >= b:
        a = a - b
        count = count + 1

    return count


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = divide(a, b)

print("Answer is: ", result)
