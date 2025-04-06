from datetime import datetime

def reduce_to_single_digit(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def bhagyank(dob_str):
    """Calculate the Bhagyank (single-digit sum) of the full date of birth."""
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")  # Convert to datetime object
        day = reduce_to_single_digit(dob.day)
        month = reduce_to_single_digit(dob.month)
        year = reduce_to_single_digit(dob.year)
        return reduce_to_single_digit(day + month + year)
    except ValueError:
        return "Invalid date format. Use 'YYYY-MM-DD' format."

def name_number(name):
    """Calculate the Name Number by summing the values of each letter and reducing to a single digit."""
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
    name = name.upper()
    total = sum(letter_values.get(char, 0) for char in name if char.isalpha())
    return reduce_to_single_digit(total)

# Example usage
name = input("Enter your name: ")
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
print(f"Bhagyank: {bhagyank(dob_str)}")
print(f"Name Number: {name_number(name)}")
total = bhagyank(dob_str) + name_number(name)
total = reduce_to_single_digit(total)
print(f"Maturity Number: {total}")
