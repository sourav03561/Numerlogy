from datetime import datetime 

def bhagyank(dob_str):
    """Calculate the Bhagyank (single-digit sum) of the full date of birth."""
    dob = datetime.strptime(dob_str, "%Y-%m-%d")  # Convert to datetime object
    day = dob.day  
    month = dob.month
    year = dob.year

    # Reduce day, month, and year to single digits
    while day >= 10:
        day = sum(int(digit) for digit in str(day))
    
    while month >= 10:
        month = sum(int(digit) for digit in str(month))
    
    while year >= 10:
        year = sum(int(digit) for digit in str(year))
    
    # Sum all single-digit values
    total = day + month + year 

    # Reduce total to a single digit
    while total >= 10:
        total = sum(int(digit) for digit in str(total))
    
    return total

# Example usage
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
print("Bhagyank:", bhagyank(dob_str))
