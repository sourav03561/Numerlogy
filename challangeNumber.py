import bhagyank  # Import the module
from datetime import datetime

def sum_to_single_digit(n):
    """Reduce a number to a single digit by summing its digits repeatedly."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Ask for DOB once
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob_str, "%Y-%m-%d")  # Convert input to datetime object

b = bhagyank.bhagyank(dob_str)  # Calculate Bhagyank

# Calculate Challenge Number Cycles
cnc1 = 36 - b
cnc2 = cnc1 + 9
cnc3 = cnc2 + 9

print(f"Bhagyank: {b}")  # Print Bhagyank once

# Calculate Root Numbers
rn1 = sum_to_single_digit(sum_to_single_digit(dob.month) + sum_to_single_digit(dob.day))
rn2 = sum_to_single_digit(sum_to_single_digit(dob.day) + sum_to_single_digit(dob.year))
rn3 = sum_to_single_digit(rn1 + rn2)
rn4 = sum_to_single_digit(sum_to_single_digit(dob.month) + sum_to_single_digit(dob.year))

print(f"Challenge cycle 1: 0 to {cnc1} years challenge number {rn1}")
print(f"Challenge cycle 2: {cnc1 + 1} to {cnc2} years challenge number {rn2}")
print(f"Challenge cycle 3: {cnc2 + 1} to {cnc3} years challenge number {rn3}")
print(f"Challenge cycle 4: {cnc3 + 1} to till death challenge number {rn4}")