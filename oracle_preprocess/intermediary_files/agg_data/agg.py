test = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/oracle_preprocess/intermediary_files/agg_data/Validation_test.json"
train = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/oracle_preprocess/intermediary_files/agg_data/Validation_train.json"

import json, csv, os

def write_csv(csv_name, path):
    with open(path, 'r') as f:
        data = json.load(f)
    print(csv_name, "json size:", len(data))
    
    directory = '../WANG_CSVS'

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    csv_path = os.path.join(directory, csv_name)
    
    train_headers = ["label", "path"]

    count = 0
    with open(csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(train_headers)

        for item in data:
            label = item["label"]
            p = item["path"]
            p = p.replace("\\", "/")
            p = p.replace("../", "")
            writer.writerow([label, p])
            count+=1

    print(csv_name, "csv size:", count)

write_csv("wang_train.csv", train)
write_csv("wang_test.csv", test)