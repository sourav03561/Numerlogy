def reduce_to_single_digit(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def success_number(dob):
    """
    Calculate the Success Number from a given full DOB (DD-MM-YYYY format).
    :param dob: str, date of birth in "DD-MM-YYYY" format
    :return: int, Success Number
    """
    try:
        dd, mm, _ = map(int, dob.split('-'))
        sum_of_digits = sum(int(digit) for digit in str(dd) + str(mm))
        return reduce_to_single_digit(sum_of_digits)
    except ValueError:
        return "Invalid date format. Use 'DD-MM-YYYY' format."

# Example usage
dob = "12-05-1999"
print(f"Success Number for {dob}: {success_number(dob)}")