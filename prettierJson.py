import os
import json


def parse_json(file_path, key):
    with open(file_path, "r") as file:
        data = json.load(file)
        try:
            edges = data["result"]["pageContext"]["postsData"][key]["edges"]
        except Exception as e:
            print(f"Error while parsing JSON file for {key}: {e}")
            return None
        return edges


def overwrite_json(data, file_path):
    with open(file_path, "w") as output_file:
        json.dump(data, output_file, indent=4)


def save_json(directory_path):
    valid_keys = ["chapters", "maps", "characters"]

    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            key = None
            for valid_key in valid_keys:
                if valid_key in filename:
                    key = valid_key
                    break

            if key is not None:
                try:
                    file_path = os.path.join(directory_path, filename)
                    edges = parse_json(file_path, key)
                    if edges is not None:
                        overwrite_json(edges, file_path)
                except Exception as e:
                    print(f"Error while parsing JSON folder for {key}: {e}")
