import csv, json
import pandas as pd

# get array of IDs that each source has 
file = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/oracle_preprocess/intermediary_files/csv/output.csv"
df = pd.read_csv(file) 
source_list = ["G","H","L","X","Y"]

'''
Returns list of unique IDs for that source
'''
def get_list(s: str):
    assert s in source_list
    sdf = df.loc[:,["id", s]]
    mask = sdf[s] != 0
    sdf=sdf[mask]
    # list of all the IDs that are in G 
    list = sdf['id'].tolist()
    return list

id_dict = {}
id_dict_shape = {}
for s in source_list:
    l = get_list(s)
    id_dict[s] = l
    id_dict_shape[s] = len(l)

print(id_dict_shape)

'''
Returns set of ids where test contains train 
'''
def return_overlapping(train:list, test:list):
    pass