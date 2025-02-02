import fitz  # PyMuPDF
import json
from collections import defaultdict
import pdb
# Load the PDF file
file_path = r"C:\Users\Divyam Shah\Downloads\City-List.pdf"
pdf = fitz.open(file_path)

# Extract text from each page
text = ""
for page in pdf:
    text += page.get_text()

# Process the text to extract states and cities
lines = text.split('\n')
data = defaultdict(list)

current_state = ""
for ind, line in enumerate(lines):
    if 'Andaman & Nicobar' in line:
        pdb.set_trace()
    # if lines[ind-1] != '4':
    #     pdb.set_trace()
    line = line.strip()
    if line.isupper() and len(line.split()) <= 3:  # Assuming state names are in uppercase
        current_state = line
    elif current_state and line and not line.startswith('4') and len(line) > 2:  # Assuming city names follow
        data[current_state].append(line)

# Convert to JSON
output_data = dict(data)

# Save to JSON file
with open('india_cities_states_from_pdf.json', 'w') as json_file:
    json.dump(output_data, json_file, indent=4)

print("Data extraction complete.")
