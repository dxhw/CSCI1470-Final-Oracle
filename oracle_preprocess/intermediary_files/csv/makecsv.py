import json
import csv

# Load JSON data
with open('/Users/michelleding/Desktop/oracle/HUST-OBS/MoCo/label_dict_sources.json') as json_file:
    data = json.load(json_file)

# Extract headers
headers = ['id', 'G', 'H', 'L', 'X', 'Y']

# Write to CSV
with open('output.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)
    
    # Populate rows
    for id_key, value in data.items():
        row = [id_key]
        for letter in ['G', 'H', 'L', 'X', 'Y']:
            row.append(len(value.get(letter, [])))
        writer.writerow(row)