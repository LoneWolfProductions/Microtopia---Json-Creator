import os
from utils.system import clear_screen
from utils.steam_folder import get_microtopia_assets_path
from utils.process_fods_to_json import process_fods_to_json

if __name__ == "__main__":
    clear_screen()

    # Get the dynamic file path for the .fods file
import os
from utils.system import clear_screen
from utils.steam_folder import get_microtopia_assets_path
from utils.fods_loader import load_fods


if __name__ == "__main__":
    clear_screen()

    # Get the dynamic file path for the .fods file
    folder_path = get_microtopia_assets_path()
    fods_files = [f for f in os.listdir(folder_path) if f.endswith(".fods")]

    for fods_file in fods_files:
        full_path = os.path.join(folder_path, fods_file)
        fods_data = load_fods(full_path)

        sheet_names = fods_data.keys()
        process_fods_to_json(full_path, *sheet_names)  # Calling the function imported from process_fods_to_json.py
