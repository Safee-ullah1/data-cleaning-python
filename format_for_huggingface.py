import csv
import json

# Function to convert a row to the desired JSON format
def convert_row_to_json(link, text, label):
    return {
        "messages": [
            {"role": "system", "content": text},
            {"role": "user", "content": "Is the statement true?"},
            {"role": "assistant", "content": "true." if label == "TRUE" else "false."},
        ]
    }

# Read the CSV and convert each row to JSON
def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        json_list = []

        for row in csv_reader:
            json_obj = convert_row_to_json(row["Link"], row["Text"], row["Label"])
            json_list.append(json_obj)

    # Write the JSON data to a file
    with open(json_file, mode='w', encoding='utf-8') as file:
        for item in json_list:
            json.dump(item, file)
            file.write('\n')

# Example usage
csv_file = 'data.csv'
json_file = 'data.json'
convert_csv_to_json(csv_file, json_file)
