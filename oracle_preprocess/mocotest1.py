import json 
def compare_ids(json_file1, json_file2):
    with open(json_file1, 'r', encoding='utf-8') as f1, open(json_file2, 'r', encoding='utf-8') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
    
    common_ids = set(data1.keys()) & set(data2.keys())
    
    for id_ in common_ids:
        number1 = data1[id_]
        number2 = data2[id_]
        if number1 != number2:
            print(f"ID: {id_}, N1: {number1}, N2: {number2}")

# Example usage:
json_file1 = '/Users/michelleding/Desktop/oracle/HUST-OBS/MoCo/dict1_count'  # Replace 'your_json_file1.json' with the path to the first JSON file
json_file2 = '/Users/michelleding/Desktop/oracle/HUST-OBS/MoCo/dict2_count'  # Replace 'your_json_file2.json' with the path to the second JSON file
compare_ids(json_file1, json_file2)