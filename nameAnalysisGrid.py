# Define letter categories based on the provided grid
grid_categories = {
    "Mental": set("AHJNPGL"),
    "Physical": set("EWDM"),
    "Emotional": set("ORIZBSTX"),
    "Intuitive": set("KFQUYCV"),
}

def categorize_name(name):
    # Convert name to uppercase to match grid categories
    name = name.upper()
    categorized_counts = {"Mental": 0, "Physical": 0, "Emotional": 0, "Intuitive": 0}
    
    # Categorize each letter in the name
    for letter in name:
        for category, letters in grid_categories.items():
            if letter in letters:
                categorized_counts[category] += 1
                break
    
    return categorized_counts

# Example usage
name = input("Enter a name: ")
categorized_result = categorize_name(name)
print("Categorized Counts:")
for category, count in categorized_result.items():
    print(f"{category}: {count}")