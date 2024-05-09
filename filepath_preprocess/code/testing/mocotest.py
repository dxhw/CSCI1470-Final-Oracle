
# =================================================================================
# =========================== TESTING  =============================================
# test that each json has the correct ocunt 

import json

def print_item_counts(json_file):
    json_dict = {}
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for id_, items in data.items():
        total_items = len(items)
        json_dict[id_] = str(total_items)

    return json_dict

def print_item_counts1(json_file):
    json_dict = {}
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for id_, inner_dict in data.items():
        total_items = sum(len(items) for items in inner_dict.values())
        json_dict[id_] = str(total_items)

    return json_dict

def save_item_counts_dict(label_dict, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(label_dict, f, indent=4)

# Example usage:
json1 = "/Users/michelleding/Desktop/oracle/HUST-OBS/MoCo/label_dict.json"
json2 = '/Users/michelleding/Desktop/oracle/HUST-OBS/MoCo/label_dict_sources.json'  

output_file = "dict1_count"
output_file2 = "dict2_count"

dict1 = print_item_counts(json1)
dict2 = print_item_counts1(json2)

save_item_counts_dict(dict1, output_file)
save_item_counts_dict(dict2, output_file2)

