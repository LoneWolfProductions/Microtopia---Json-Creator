from utils.json_saver import save_json_to_file, to_json
from utils.fods_loader import load_fods
from utils.sheet_manipulation import cleanup_data

def process_fods_to_json(fods_file, *sheet_names):
    """
    Processes FODS sheets and converts to cleaned JSON, skipping empty or garbage sheets.
    """
    for sheet_name in sheet_names:
        print(f"Processing sheet: {sheet_name}")

        # Load data from file
        fods_data = load_fods(fods_file)

        if sheet_name not in fods_data:
            print(f"Sheet '{sheet_name}' not found in {fods_file}")
            continue

        sheet_data = fods_data[sheet_name]

        # Filter out rows that are completely empty or whitespace-only
        non_empty_rows = [
            row for row in sheet_data
            if isinstance(row, list) and any(str(cell).strip() for cell in row)
        ]

        if not non_empty_rows:
            print(f"Skipping sheet '{sheet_name}' - no usable rows.")
            continue

        try:
            clean_sheet_data = cleanup_data(non_empty_rows)
        except Exception as e:
            print(f"Error cleaning sheet '{sheet_name}': {e}")
            continue

        json_output = to_json(clean_sheet_data)
        save_json_to_file(json_output, fods_file, sheet_name)
