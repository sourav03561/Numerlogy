from datetime import datetime

def sum_to_single_digit(n):
    """Reduce a number to a single digit by summing its digits repeatedly."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def kuaNumber(dob_str, gender):
    """Calculate the Angle Number based on year of birth and gender."""
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

# Example usage
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
gender = input("Enter your gender (male/female): ")
print("Angle Number:", kuaNumber(dob_str, gender))
