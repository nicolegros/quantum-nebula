import pandas as pd
import sys


def extract_data_to_csv(text_file_path: str, csv_file_path: str):
    """
    Extracts data from a text file and saves it as a CSV file.

    Parameters:
    - text_file_path: Path to the input text file.
    - csv_file_path: Path to the output CSV file.
    """
    # Reading the content of the text file, skipping the first two lines
    with open(text_file_path, 'r') as file:
        lines = file.readlines()[2:]

    # Processing each line to extract data
    data = []
    for line in lines:
        # Splitting each line by commas and then separating the last value
        parts = line.strip().split(', ')
        value = parts[-1].split()[-1]
        column_name = ' '.join(parts[:-1])
        data.append((column_name, value))

    # Creating a DataFrame
    df = pd.DataFrame(data, columns=['Column Name', 'Value'])

    # Saving the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)
    print(f'Data successfully extracted to {csv_file_path}')


def extract_data_to_wide_csv(text_file_path, csv_file_path):
    """
    Extracts data from a text file and saves it as a CSV file with a single row,
    turning each unique prefix into a column header.

    Parameters:
    - text_file_path: Path to the input text file.
    - csv_file_path: Path to the output CSV file.
    """
    # Reading the content of the text file, skipping the first two lines
    with open(text_file_path, 'r') as file:
        lines = file.readlines()[2:]

    # Dictionary to hold our data with column names as keys
    data = {}
    for line in lines:
        parts = line.strip().split(', ')
        # The value is the last element after the last space
        value = parts[-1].split()[-1]
        # Column name is everything before the last comma
        column_name = ' '.join(parts[:-1])
        data[column_name] = value

    # Creating a DataFrame from the dictionary (which automatically creates columns)
    # and transposing it to match the desired output format
    df = pd.DataFrame([data])

    # Saving the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)
    print(f'Data successfully extracted to {csv_file_path}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_text_file_path> <output_csv_file_path>")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        extract_data_to_csv(input_path, output_path)
