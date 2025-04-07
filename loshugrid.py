from collections import Counter
from datetime import datetime

def sum_to_single_digit(n):
    """Reduce a number to a single digit by summing its digits repeatedly."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def bhagyank(dob_str):
    """Calculate the Bhagyank (single-digit sum) of the full date of birth."""
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    day, month, year = dob.day, dob.month, dob.year
    
    return sum_to_single_digit(sum_to_single_digit(day) + sum_to_single_digit(month) + sum_to_single_digit(year))

def mulank(dob_str):
    """Calculate the Mulank (single-digit sum) of the day of birth."""
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    return sum_to_single_digit(dob.day)

def kuaNumber(dob_str, gender):
    """Calculate the Kua Number based on year of birth and gender."""
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    year_digit_sum = sum_to_single_digit(dob.year)
    
    if gender.lower() == "male":
        result = 11 - year_digit_sum
        if result == 5:
            result = 2
    elif gender.lower() == "female":
        result = year_digit_sum + 4
        if result == 5:
            result = 8
    else:
        return "Invalid gender! Please enter 'male' or 'female'."
    
    return sum_to_single_digit(result)

def get_name_number(name):
    """Calculate the Name Number by summing letter values and reducing to a single digit."""
    name = name.upper()
    letter_values = {
        'A': 1, 'I': 1, 'J': 1, 'Y': 1, 'Q': 1,
        'B': 2, 'K': 2, 'R': 2,
        'C': 3, 'G': 3, 'L': 3, 'S': 3,
        'D': 4, 'M': 4, 'T': 4,
        'E': 5, 'H': 5, 'N': 5,
        'U': 6, 'V': 6, 'W': 6, 'X': 6,
        'O': 7, 'Z': 7,
        'P': 8, 'F': 8
    }
    total = sum(letter_values[char] for char in name if char in letter_values)
    return sum_to_single_digit(total)

def get_loshu_grid(dob_str, gender, name):
    """Generate the Lo Shu Grid from Date of Birth (DOB), including Bhagyank, Mulank, Kua Number, and Name Number."""
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    day = dob.day
    
    digits = [int(digit) for digit in dob_str if digit.isdigit()]
    digit_counts = Counter(digits)
    
    b = bhagyank(dob_str)
    m = mulank(dob_str)
    k = kuaNumber(dob_str, gender)
    n = get_name_number(name)
    
    digit_counts[b] = digit_counts.get(b, 0) + 1
    if day not in [1,2,3,4,5,6,7,8,9,10,20,30]:
        digit_counts[m] = digit_counts.get(m, 0) + 1
    if isinstance(k, int):  # Ensure Kua Number is valid before adding
        digit_counts[k] = digit_counts.get(k, 0) + 1
    digit_counts[n] = digit_counts.get(n, 0) + 1
    
    loshu_grid = [
        [digit_counts.get(4, 0), digit_counts.get(9, 0), digit_counts.get(2, 0)],
        [digit_counts.get(3, 0), digit_counts.get(5, 0), digit_counts.get(7, 0)],
        [digit_counts.get(8, 0), digit_counts.get(1, 0), digit_counts.get(6, 0)]
    ]
    missing_numbers = missing_numbers = [i for i in range(1, 10) if digit_counts.get(i, 0) == 0]
    return loshu_grid, missing_numbers

def print_loshu_grid(grid):
    """Print the Lo Shu Grid in a formatted way."""
    print("\nLo Shu Grid based on your DOB:")
    for row in grid:
        print(" | ".join(str(num) for num in row))
        print("-" * 13)

# Example usage:
dob_str = input("Enter your Date of Birth (YYYY-MM-DD): ")
gender = input("Enter your gender (male/female): ")
name = input("Enter your name: ")

loshu_grid, missing_numbers = get_loshu_grid(dob_str, gender, name)
print_loshu_grid(loshu_grid)

print("\nNumbers with count 0 in the Lo Shu Grid:", missing_numbers)
