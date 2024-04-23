import json
# =============================================================================
# This class takes MOCO_train.json and creates two new jsons 
# 1. label_dict.json (id -> paths)
# 2. label_dict_sources.json (id -> source -> path)

# NOTE: all paths are currently absolute paths not relative paths 
# =============================================================================
# ================== LABEL_DICT ===============================================
def create_label_dict(json_file):
    label_dict = {}
    with open(json_file, 'r') as f:
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
    with open(output_file, 'w') as f:
        json.dump(label_dict, f, indent=4)

# =============================================================================
# ================== LABEL_DICT_sources =======================================
'''Making label dict with sources'''
def create_label_dict2(json_file):
    label_dict = {}
    with open(json_file, 'r') as f:
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
    with open(output_file, 'w') as f:
        json.dump(label_dict, f, indent=4)

# =============================================================================

json_file = '/Users/michelleding/Desktop/oracle/HUST-OBS/MoCo/MOCO_train.json'  
# CREATING A JSON OF ID -> SOURCES (LABEL_DICT.JSON)
label_dict = create_label_dict(json_file)
output_file = 'label_dict.json'
save_label_dict(label_dict, output_file)

# CREATING A JSON OF ID->SOURCES->[PATHS] (LABEL_DICT_SOURCES.JSON)
output_file2 = 'label_dict_sources.json'
label_dict2 = create_label_dict2(json_file)
save_label_dict2(label_dict2, output_file2)
