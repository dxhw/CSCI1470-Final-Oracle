import csv
import os

def split_csv(input_file, output_dir, num_partitions=4):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the CSV file and count total rows
    headers = None
    total_rows = 0
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Read and store the header row
        total_rows = sum(1 for _ in reader) + 1  # Add 1 for the header row

    # Calculate rows per partition
    rows_per_partition = total_rows // num_partitions

    # Iterate through the CSV file and split into partitions
    partition_index = 1
    partition_rows = [headers]  # Add header row to each partition
    with open(input_file, 'r', newline='') as csvfile:
        next(csvfile)  # Skip header row
        for i, row in enumerate(csv.reader(csvfile)):
            partition_rows.append(row)
            if len(partition_rows) == rows_per_partition or i == total_rows - 2:
                # Save partition to CSV file
                partition_file = os.path.join(output_dir, f'partition_{partition_index}.csv')
                with open(partition_file, 'w', newline='') as partition_csv:
                    writer = csv.writer(partition_csv)
                    writer.writerows(partition_rows)
                partition_index += 1
                partition_rows = [headers]  # Reset partition rows with header row

# Example usage
input_file = "/Users/michelleding/Desktop/oracle/CSCI1470-Final-Oracle/preprocess_code/DATA/wang_train.csv"
output_dir = "TRAIN4"
split_csv(input_file, output_dir)
