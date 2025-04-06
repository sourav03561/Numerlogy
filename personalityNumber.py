def calculate_personality_number(name):
    letter_values = {
        'A': 1, 'I': 1, 'J': 1, 'Y': 1, 'Q': 1,
        'B': 2, 'K': 2, 'R': 2,
        'C': 3, 'G': 3, 'L': 3, 'S': 3,
        'D': 4, 'M': 4, 'T': 4,
        'E': 5, 'H': 5, 'N': 5,
        'U': 6, 'V': 6, 'W': 6, 'X': 6,
        'O': 7, 'Z': 7,
        'P': 8, 'F': 8
    }
    name = name.upper()
    consonants = set(letter_values.keys()) - {'A', 'E', 'I', 'O', 'U'}
    
    valid_consonants = []
    words = name.split()
    
    for word in words:
        for i, char in enumerate(word):
            if char in consonants:
                if char == 'Y' and i != 0:
                    continue  # Skip 'Y' if it's not the first letter
                valid_consonants.append(letter_values[char])
    
    personality_number = sum(valid_consonants)
    
    # Reduce to single digit
    while personality_number > 9 and personality_number not in {11, 22, 33}:
        personality_number = sum(int(digit) for digit in str(personality_number))
    
    return personality_number

# Example Usage
name = "sourav sarkar"
print(f"Personality Number for {name}: {calculate_personality_number(name)}")