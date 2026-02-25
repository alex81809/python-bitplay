def longest_ones(n):
    # Convert number to binary string (stripping the '0b' prefix)
    binary_str = bin(n)[2:]
    
    max_count = 0
    current_count = 0
    
    for bit in binary_str:
        if bit == '1':
            current_count += 1
            # Update max_count if current streak is longer
            max_count = max(max_count, current_count)
        else:
            # We hit a 0, so reset the current streak
            current_count = 0
            
    return max_count


num = int(input("Enter a number: "))
print(f"The longest consecutive 1s in {bin(num)} is: {longest_ones(num)}")
