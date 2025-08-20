import json

# Load the JSON file
with open("output.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Count the number of entries
print(f"Total entries: {len(data)}")
