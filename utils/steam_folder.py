import winreg
import os

def get_steam_folder():
    try:
        # Access the registry to get Steam installation path
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Valve\Steam")
        
        # Query the 'SteamPath' registry value which contains the installation folder
        steam_folder, _ = winreg.QueryValueEx(registry_key, "SteamPath")
        
        # Return the Steam folder path
        return steam_folder
    except FileNotFoundError:
        # The key doesn't exist, Steam might not be installed or installed elsewhere
        return None
    except Exception as e:
        # Catch other unexpected errors and print the error message
        print(f"An error occurred: {e}")
        return None

def get_microtopia_assets_path():
    steam_folder = get_steam_folder()
    if steam_folder:
        # Construct the full path to the StreamingAssets directory
        assets_path = os.path.join(steam_folder, 'steamapps', 'common', 'Microtopia', 'Microtopia_Data', 'StreamingAssets')
        
        # Ensure the path uses backslashes only
        assets_path = assets_path.replace('/', '\\')
        
        return assets_path
    else:
        return None
