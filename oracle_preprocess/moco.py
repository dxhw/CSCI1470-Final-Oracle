import json

def json_shape(json_file):
    # f = open (json_file, "r")
    # data = json.loads(f.read())
    # print(data)
    # f.close()
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, list):
        # If data is a list of items
        rows = len(data)
        if rows > 0:
            cols = len(data[0].keys())
        else:
            cols = 0
    elif isinstance(data, dict):
        # If data is a dictionary
        rows = 1
        cols = len(data.keys())
    else:
        # If data is neither list nor dictionary
        rows = 0
        cols = 0
    
    return rows, cols

def create_label_dict(json_file):
    label_dict = {}
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in data:
        label = item['label']
        path = item['path']
        if label in label_dict:
            label_dict[label].append(path)
        else:
            label_dict[label] = [path]
    
    return label_dict

def save_label_dict(label_dict, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(label_dict, f, indent=4)

'''Making label dict with sources'''
def create_label_dict2(json_file):
    label_dict = {}
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in data:
        label = item['label']
        path = item['path']
        png = path.split("\\")[-1]
        id = png[0]
        if label not in label_dict:
            source_dict = {"G":[], "H":[], "L":[], "X":[], "Y":[]}
            label_dict[label] = source_dict
        id_dict = label_dict[label]
        assert id in id_dict
        id_dict[id].append(path)

    return label_dict

def save_label_dict2(label_dict, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(label_dict, f, indent=4)

# Example usage:
json_file = '/Users/michelleding/Desktop/oracle/HUST-OBS/MoCo/MOCO_train.json'  
rows, cols = json_shape(json_file)
print(f"JSON shape: {rows} rows x {cols} columns")

# CREATING A JSON OF ID -> SOURCES
label_dict = create_label_dict(json_file)
output_file = 'label_dict.json'
save_label_dict(label_dict, output_file)

# CREATING A JSON OF ID->SOURCES->[PATHS]
output_file2 = 'label_dict_sources.json'
label_dict2 = create_label_dict2(json_file)
save_label_dict2(label_dict2, output_file2)
