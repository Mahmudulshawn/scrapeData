from bs4 import BeautifulSoup
import json
import pandas as pd

# Step 1: Load the HTML file
with open("MedicinDatabase.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Step 2: Find the correct table using ID or class
table = soup.find("table", {"id": "example"})

# Step 3: Extract headers
headers = [th.get_text(strip=True) for th in table.find_all("th")]

# Step 4: Extract data rows
data = []
for row in table.find("tbody").find_all("tr"):
    cells = row.find_all("td")
    if len(cells) == len(headers):
        item = {headers[i]: cells[i].get_text(strip=True) for i in range(len(headers))}
        data.append(item)

# Step 5: Save to JSON
with open("output.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

# Step 6: Save to Excel
df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False)
