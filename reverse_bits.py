def reverse_bits(n, bit_size=32):
    result = 0
    for i in range(bit_size):
        # Shift result left to make room for the next bit
        result = (result << 1) | (n & 1)
        # Shift the input number right to process the next bit
        n >>= 1
    return result

# Taking input from the user
try:
    num = int(input("Enter a number: "))
    # Using 8 bits for a simple visual example, but 32 is standard
    reversed_num = reverse_bits(num, 32)
    
    print(f"Original: {num} (Binary: {bin(num)[2:].zfill(32)})")
    print(f"Reversed: {reversed_num} (Binary: {bin(reversed_num)[2:].zfill(32)})")
except ValueError:
    print("Please enter a valid integer.")
