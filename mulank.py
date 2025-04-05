from datetime import datetime

def mulank(dob_str):
    """Calculate the Mulank (single-digit sum) of the day of birth."""
    dob = datetime.strptime(dob_str, "%Y-%m-%d")  # Convert to datetime object
    day = dob.day  # Extract the day
    
    while day >= 10:  # Keep summing digits until a single digit is obtained
        day = sum(int(digit) for digit in str(day))
    
    return day

# Example usage
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
print("Mulank:", mulank(dob_str))
