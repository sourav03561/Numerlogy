def calculate_soul_urge(name):
    letter_values = {'A': 1, 'I': 1, 'Y': 1, 'E': 5, 'U': 6, 'O': 7}
    name = name.upper()
    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
    
    valid_vowels = []
    words = name.split()
    
    for word in words:
        name_length = len(word)
        
        for i, char in enumerate(word):
            if char in vowels:
                if char == 'Y':
                    # 'Y' should not be the first letter of any word
                    if i == 0:
                        continue  # Skip 'Y' if it's the first letter of any word
                    elif i == name_length - 1 or (i > 0 and i < name_length - 1):
                        valid_vowels.append(letter_values[char])
                else:
                    valid_vowels.append(letter_values[char])
    
    soul_urge_number = sum(valid_vowels)
    
    # Reduce to single digit
    while soul_urge_number > 9 and soul_urge_number not in {11, 22}:
        soul_urge_number = sum(int(digit) for digit in str(soul_urge_number))
    
    return soul_urge_number

# Example Usage
name = "souyrav ysarykar"
print(f"Soul Urge Number for {name}: {calculate_soul_urge(name)}")
