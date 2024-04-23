# making the 5 jsons for each source with {id: path}
import json, os
dict = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/oracle_preprocess/sources_json/label_dict_sources.json"
id_json = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/sources_process/index_list.json"

def make_json(s, path_json, id_json):
    return_dict = {}
    with open(path_json, 'r') as f:
        data = json.load(f)
    
    with open(id_json, 'r') as f:
        id_dict = json.load(f)
    
    assert s in ["G", "H", "L", "X", "Y"]
    id_list = id_dict[s]

    for i in id_list:
        path_dict = data[i]
        path_list = path_dict[s]
        return_dict[i] = path_list

    return return_dict

def save_file(dict, output_file):
    with open(output_file, 'w') as f:
        json.dump(dict, f, indent=4)


directory = 'oracle_preprocess/JSON_SOURCES'

# Ensure the directory exists, if not, create it
if not os.path.exists(directory):
    os.makedirs(directory)


for s in ["G", "H", "L", "X", "Y"]:
    file = os.path.join(directory, s+".json")
    letter_dict = make_json(s, dict, id_json)
    save_file(letter_dict, file)
