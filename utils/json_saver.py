import os
import json

def to_json(rows):
    return json.dumps(rows, ensure_ascii=False, indent=2)

def generate_filename(file_path, sheet_name):
    original_filename = os.path.basename(file_path).split('.')[0].lower()
    sheet_name_clean = sheet_name.replace(" ", "").replace("_", "")
    
    return f"{original_filename}-{sheet_name_clean}.json"

def save_json_to_file(json_data, file_path, sheet_name):
    filename = generate_filename(file_path, sheet_name)
    current_dir = os.getcwd()
    json_dir = os.path.join(current_dir, "json")

    if not os.path.exists(json_dir):
        os.makedirs(json_dir)

    output_file_path = os.path.join(json_dir, filename)
    with open(output_file_path, "w", encoding="utf-8") as json_file:
        json_file.write(json_data)

    print(f"JSON saved to: {output_file_path}")