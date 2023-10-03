import json

import json

def read_config(file_path):
    file_paths = []
    entry_names = []
    target_names = []

    try:
        with open(file_path, 'r') as config_file:
            config_data = json.load(config_file)
            file_paths = config_data.get("file_paths", [])
            function_names = config_data.get("function_names", {})
            entry_names = function_names.get("entry", [])
            target_names = function_names.get("target", [])
    except FileNotFoundError:
        print(f"Config file '{file_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}")

    return file_paths, entry_names, target_names

