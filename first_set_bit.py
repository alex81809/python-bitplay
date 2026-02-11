def find_rightmost_set_bit(n):
    if n == 0:
        return 0
    return n & -n

try:
    num = int(input("Enter a number: "))
    result = find_rightmost_set_bit(num)
    
    if result == 0:
        print("The number 0 has no set bits.")
    else:
        print(f"Number: {num} (Binary: {bin(num)})")
        print(f"Rightmost set bit value: {result} (Binary: {bin(result)})")
except ValueError:
    print("Please enter a valid integer.")
