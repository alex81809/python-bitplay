def divide(a, b):
    total = 0
    count = 0

    while total + b <= a:
        total = total + b 
        count = count + 1

    return count 


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Answer is: ", divide(a, b))
