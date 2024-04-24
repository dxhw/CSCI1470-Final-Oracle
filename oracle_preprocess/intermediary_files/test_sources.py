# TESTING TO MAKE SURE THE 5 JSON SOURCES HAVE THE CORRECT NUMBER OF IMAGES
import json 

G_path = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/oracle_preprocess/JSON_SOURCES/G.json"
H_path = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/oracle_preprocess/JSON_SOURCES/H.json"
L_path = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/oracle_preprocess/JSON_SOURCES/L.json"
X_path = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/oracle_preprocess/JSON_SOURCES/X.json"
Y_path = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/oracle_preprocess/JSON_SOURCES/Y.json"

path_dict = {
    "G": G_path,
    "H": H_path,
    "L": L_path,
    "X": X_path,
    "Y": Y_path
}

for s in ["G", "H", "L", "X", "Y"]:
    path = path_dict[s]
    with open(path, 'r') as f:
        data = json.load(f)
    
    count = 0
    for id in data.keys():
        list = data[id]
        count += len(list)

    print(s, " count: ", count)
