import pandas as pd
import os
import sys

def processfiles(root_directory_path, csv_file_path, filepattern):
    """
    Recursively processes all 'load' files in the given root directory and compiles them into a single CSV file.

    Parameters:
    - root_directory_path: Path to the root directory containing the text files.
    - csv_file_path: Path to the output CSV file.
    """
    # Initialize a list to hold all rows of data
    all_data = []

    # Walk through the directory
    for subdir, dirs, files in os.walk(root_directory_path):
        for filename in files:
            # Check if the filename starts with 'load' and ends with '.txt'
            if filename.startswith(filepattern) and filename.endswith('.txt'):
                # Construct the full file path
                file_path = os.path.join(subdir, filename)
                # Process the file
                with open(file_path, 'r') as file:
                    lines = file.readlines()[2:]
                    data = {}
                    for line in lines:
                        parts = line.strip().split(', ')
                        value = parts[-1].split()[-1]
                        column_name = ' '.join(parts[:-1])
                        data[column_name] = value
                    all_data.append(data)

    # Create a DataFrame from all the data
    df = pd.DataFrame(all_data)

    # Saving the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)
    print(f'Data from all load files successfully compiled into {csv_file_path}')

