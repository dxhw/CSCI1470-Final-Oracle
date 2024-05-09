import json
path = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/oracle_preprocess/MOCO_train.json"
# Load the JSON file
with open(path, 'r') as file:
    data = json.load(file)

# Extract the list of labels
labels = [item['label'] for item in data]

# Count the number of unique labels
unique_labels = set(labels)
num_unique_labels = len(unique_labels)

print("Number of unique labels:", num_unique_labels)
