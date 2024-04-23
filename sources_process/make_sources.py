# This class will make the 5 jsons with all the sources 
import csv, json, os

directory = 'sources_process'

# Ensure the directory exists, if not, create it
if not os.path.exists(directory):
    os.makedirs(directory)


file = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/oracle_preprocess/output.csv"
# Initialize dictionary
letter_dict = {'G': [], 'H': [], 'L': [], 'X': [], 'Y': []}
count_dict = {'G': 0, 'H': 0, 'L': 0, 'X': 0, 'Y': 0}

# Read the CSV file
with open(file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        for key in letter_dict.keys():
            val = int(row[key])
            if val != 0:
                count_dict[key] += val
                letter_dict[key].append(row['id'])

# Write the dictionary to a new file

def save_file(label_dict, output_file):
    with open(output_file, 'w') as f:
        json.dump(label_dict, f, indent=4)


output_file = "sources_process/index_list.json"
output_file_count = "sources_process/index_list_count.json"

save_file(letter_dict, output_file)
save_file(count_dict, output_file_count)

