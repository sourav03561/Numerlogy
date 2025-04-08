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

def get_loshu_grid(dob_str):
    """Generate the Lo Shu Grid from Date of Birth (DOB), including Bhagyank and Mulank."""
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    day = dob.day
    
    # Extract individual digits from DOB
    digits = [int(digit) for digit in dob_str if digit.isdigit()]
    digit_counts = Counter(digits)
    
    # Calculate Bhagyank and Mulank
    b = bhagyank(dob_str)
    m = mulank(dob_str)

    # Add Bhagyank and Mulank to the grid if not already present
    digit_counts[b] = digit_counts.get(b, 0) + 1
    if day not in [1,2,3,4,5,6,7,8,9,10,20,30]:
        digit_counts[m] = digit_counts.get(m, 0) + 1

    # Create the Lo Shu Grid
    loshu_grid = [
        [digit_counts.get(4, 0), digit_counts.get(9, 0), digit_counts.get(2, 0)],
        [digit_counts.get(3, 0), digit_counts.get(5, 0), digit_counts.get(7, 0)],
        [digit_counts.get(8, 0), digit_counts.get(1, 0), digit_counts.get(6, 0)]
    ]
    missing_numbers = missing_numbers = [i for i in range(1, 10) if digit_counts.get(i, 0) == 0]
    present_numbers = [i for i in range(1, 10) if digit_counts.get(i, 0) > 0]
    return loshu_grid, missing_numbers, present_numbers

def print_loshu_grid(grid, dob):
    """Print the Lo Shu Grid in a formatted way."""
    print(f"\nLo Shu Grid for DOB: {dob}")
    print("-" * 13)
    for row in grid:
        print(" | ".join(str(num) for num in row))
        print("-" * 13)

# Take two dates of birth as input
dob1 = input("Enter first date of birth (YYYY-MM-DD): ")
dob2 = input("Enter second date of birth (YYYY-MM-DD): ")

# Generate and print Lo Shu Grids for both DOBs
grid1, missing_numbers1, present_numbers1 = get_loshu_grid(dob1)
grid2, missing_numbers2, present_numbers2 = get_loshu_grid(dob2)
m1 = mulank(dob1)
m2 = mulank(dob2)
print_loshu_grid(grid1, dob1)
print_loshu_grid(grid2, dob2)
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
score = 0
if m2 in numerology_chart[m1]['friends']:
    score+=1
p1 = False
p2 = False
print("missing numbers1: ",missing_numbers1)
print("present numbers1: ",present_numbers1)
print("missing numbers2: ",missing_numbers2)
print("present numbers2: ",present_numbers2)
print(missing_numbers2)

for mis in missing_numbers1:
    if mis in present_numbers2:
        p1 = True
        break 
    
for mis in missing_numbers2:
    if mis in present_numbers1:
        p2 = True
        break
if p1 and p2:
    score+=1
print(score)

mixed_numbers = list(set(present_numbers1 + present_numbers2))
print("mixed numbers:", mixed_numbers)

vision_plane = [3, 4, 8]
will_plane = [9, 5, 1]
action_plane = [2, 6, 7]
golden_plane = [4, 5, 6]
silver_plane = [2, 5, 8]

# Check if all numbers of any plane are present in mixed_numbers
if (all(num in mixed_numbers for num in vision_plane) or 
    all(num in mixed_numbers for num in will_plane) or 
    all(num in mixed_numbers for num in action_plane) or 
    all(num in mixed_numbers for num in golden_plane) or 
    all(num in mixed_numbers for num in silver_plane)):
    score += 1

if (all(num in mixed_numbers for num in golden_plane) or 
    all(num in mixed_numbers for num in silver_plane) ):
    score+=1

if ((5 in mixed_numbers) or (6 in mixed_numbers)):
    score+=1

print("score:",score)
print("score: {}%".format(score / 5 * 100))