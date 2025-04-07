from datetime import datetime

def sum_to_single_digit(n):
    """Reduce a number to a single digit by summing its digits repeatedly."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def kuaNumber(dob_str, gender):
    """Calculate the Kua Number based on year of birth and gender."""
    dob = datetime.strptime(dob_str, "%Y-%m-%d")  # Convert string to datetime
    year = dob.year  # Extract only the year

    year_digit_sum = sum_to_single_digit(year)  # Reduce year to a single digit

    if gender.lower() == "male":
        result = 11 - year_digit_sum  # Male formula
        if result == 5:
            result = 2

    elif gender.lower() == "female":
        result = year_digit_sum + 4  # Female formula
        if result == 5:
            result = 8
    else:
        return "Invalid gender! Please enter 'male' or 'female'."

    return sum_to_single_digit(result)  # Convert final result to a single digit

kua_lucky_directions = {
    1: {"Money and Prosperity": "SE", "Health": "E", "Relationships": "S", "Personal Growth": "N"},
    2: {"Money and Prosperity": "NE", "Health": "W", "Relationships": "NW", "Personal Growth": "SW"},
    3: {"Money and Prosperity": "S", "Health": "N", "Relationships": "SE", "Personal Growth": "E"},
    4: {"Money and Prosperity": "N", "Health": "S", "Relationships": "E", "Personal Growth": "SE"},
    5: {"Money and Prosperity": "NW", "Health": "W", "Relationships": "NW", "Personal Growth": "SW"},
    6: {"Money and Prosperity": "W", "Health": "NE", "Relationships": "SW", "Personal Growth": "NW"},
    7: {"Money and Prosperity": "NW", "Health": "W", "Relationships": "NE", "Personal Growth": "SW"},
    8: {"Money and Prosperity": "SW", "Health": "NW", "Relationships": "W", "Personal Growth": "NE"},
    9: {"Money and Prosperity": "N", "Health": "SE", "Relationships": "N", "Personal Growth": "S"},
}

# Example usage
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
gender = input("Enter your gender (male/female): ")
kua_num = kuaNumber(dob_str, gender)
if isinstance(kua_num, int):
    print(f"Your Kua Number is: {kua_num}")
    print("Lucky Directions:")
    for category, direction in kua_lucky_directions.get(kua_num, {}).items():
        print(f"{category}: {direction}")
else:
    print(kua_num)