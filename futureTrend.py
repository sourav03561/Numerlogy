from datetime import datetime

# Get the current year
current_year = datetime.now().year
current_month = datetime.now().month
current_day = datetime.now().day
# Function to reduce a number to a single digit
def single_digit(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Calculate Universal Year
universal_year = single_digit(current_year)
print(f"Universal Year: {universal_year}")

# Take user input for DOB
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

# Convert input string to datetime object
dob = datetime.strptime(dob_input, "%Y-%m-%d")

# Calculate Personal Year
personal_year = single_digit(dob.day + dob.month + universal_year)
print(f"Personal Year: {personal_year}")

personal_month = single_digit(personal_year + current_month)
print(f"Personal month: {personal_month}")

personal_day = single_digit(personal_month + current_day)
print(f"Personal month: {personal_day}")
