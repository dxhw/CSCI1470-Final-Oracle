import json,os

g_path = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/oracle_preprocess/JSON_SOURCES/G.json"

def make_g_json():
    dict = {}
    with open(g_path, 'r') as f:
        data = json.load(f)
    
    for key in data.keys():
        l = data[key]

        new_list = []
        for path in l:
            idx = 35
            s = path[idx:len(path)]
            s.encode('utf-8', 'replace').decode('utf-8')
            ps = path[0:idx] + s

            # flag if ??
            if "?" in ps:
                print("flagging: ", key, " ", ps)

            new_list.append(ps)
        
        dict[key] = new_list
    return dict

def save_file(label_dict, output_file):
    with open(output_file, 'w') as f:
        json.dump(label_dict, f, ensure_ascii=False, indent=4)

directory = '../JSON_SOURCES'

# Ensure the directory exists, if not, create it
if not os.path.exists(directory):
    os.makedirs(directory)

output_file = "G_json_new.json"
path = os.path.join(directory, output_file)

dict = make_g_json()
save_file(dict, path)