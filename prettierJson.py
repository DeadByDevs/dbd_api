import os
import json


def format_json_file(input_file_path):
    try:
        with open(input_file_path, "r") as input_file:
            json_data = input_file.read()

        parsed_data = json.loads(json_data)
        formatted_json = json.dumps(parsed_data, indent=4)

        with open(input_file_path, "w") as output_file:
            output_file.write(formatted_json)

        print(f"JSON data in '{input_file_path}' has been formatted and overwritten.")
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error: {e}")


def format_json_folder(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            input_file_path = os.path.join(directory_path, filename)
            format_json_file(input_file_path)
