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

# id_dict["M1"] = [1,2,3]
# id_dict["M2"] = [1,4]
# id_dict["M3"] = [1,2,5,6]

'''
Returns set of ids where test contains train 
'''
def return_overlapping(train:list, test:list):
    # train = [H,G,L,Y]
    # test = X
    # make train set
    train_list = []
    for s in train:
        train_list += id_dict[s]
    train_set = set(train_list)

    # make test set 
    test_list = []
    for p in test:
        test_list += id_dict[p]
    test_set = set(test_list)

    # get list of elements to remove
    filtered_test_set = set(test_set)
    removed_list = []
    for id in test_set:
        if id not in train_set:
            removed_list.append(id)
            filtered_test_set.remove(id)
    
    print("=== TRAIN:", train, "TEST:", test, "===")
    print(">> train set:", len(train_set))
    print(">> test set:", len(test_set))
    print(">> filtered_test set:", len(filtered_test_set))
    print(">> removed list:", len(removed_list))
    
    return train_set, filtered_test_set, removed_list

# return_overlapping(["M1", "M2"], ["M3"])
# return_overlapping(["H","X","L","Y"], ["G"])
# return_overlapping(["H","G","L","Y"], ["X"])
# return_overlapping(["H","X","G"], ["L","Y"])

