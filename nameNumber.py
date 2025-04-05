def sum_to_single_digit(n):
    """Reduce a number to a single digit by summing its digits repeatedly."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def get_name_number(name):
    """Calculate the Name Number by summing letter values and reducing to a single digit."""
    name = name.upper()  # Convert name to uppercase for matching
    letter_values = {
        'A': 1, 'I': 1, 'J': 1, 'Y': 1,'Q':1,
        'B': 2, 'K': 2, 'R': 2,
        'C': 3, 'G': 3, 'L': 3, 'S': 3,
        'D': 4, 'M': 4, 'T': 4,
        'E': 5, 'H': 5, 'N': 5,
        'U': 6, 'V': 6, 'W': 6, 'X': 6,
        'O': 7, 'Z': 7,
        'P': 8, 'F': 8
    }
    
    total = sum(letter_values[char] for char in name if char in letter_values)
    
    return sum_to_single_digit(total)  # Reduce to a single digit

# Example usage
name = input("Enter your name: ")
print("Name Number:", get_name_number(name))
