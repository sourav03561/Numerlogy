from datetime import datetime

numerology_chart = {
    1: {"friends": [1, 2, 3, 5, 6, 9], "enemy": [8], "neutral": [4, 7]},
    2: {"friends": [1, 2, 3, 5], "enemy": [8, 4, 9], "neutral": [7, 6]},
    3: {"friends": [1, 2, 3, 5], "enemy": [6], "neutral": [4, 8, 7, 9]},
    4: {"friends": [1, 5, 7, 6], "enemy": [2, 9, 4, 8], "neutral": [3]},
    5: {"friends": [1, 2, 3, 5, 6], "enemy": [], "neutral": [4, 7, 8, 9]},
    6: {"friends": [1, 4, 5, 6, 7], "enemy": [3], "neutral": [2, 8, 9]},
    7: {"friends": [1, 3, 5, 4, 6], "enemy": [], "neutral": [8, 2, 7, 9]},
    8: {"friends": [5, 3, 6, 7], "enemy": [1, 2, 4, 8], "neutral": [9]},
    9: {"friends": [1, 3, 5], "enemy": [4, 2], "neutral": [9, 7, 6, 8]},
}
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

dob = input("Enter date of birth (YYYY-MM-DD): ")
m = mulank(dob)
b = bhagyank(dob)
mn = numerology_chart[m]['friends']
bn =  numerology_chart[b]['friends']
lucky_number = list(set(mn) & set(bn))
print("Lucky Number:",lucky_number)
unlucky_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
unlucky_number = list(set(unlucky_number) - set(lucky_number))
print("Unlucky Number:",unlucky_number)