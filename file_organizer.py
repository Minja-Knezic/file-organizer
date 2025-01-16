import os
import shutil
import json
from pathlib import Path
from datetime import datetime

# Default file categories
DEFAULT_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Others": []
}

CONFIG_FILE = "categories.json"

def load_categories():
    """Load file categories from the configuration file or use defaults."""
    if not Path(CONFIG_FILE).is_file():
        print(f"No config file found. Creating default '{CONFIG_FILE}'.")
        save_categories(DEFAULT_CATEGORIES)
        return DEFAULT_CATEGORIES

    try:
        with open(CONFIG_FILE, "r") as config_file:
            categories = json.load(config_file)
            print(f"Loaded categories from '{CONFIG_FILE}'.")
            return categories
    except Exception as e:
        print(f"Error loading config file: {e}")
        print("Using default categories.")
        return DEFAULT_CATEGORIES

def save_categories(categories):
    """Save categories to the configuration file."""
    with open(CONFIG_FILE, "w") as config_file:
        json.dump(categories, config_file, indent=4)
    print(f"Default categories saved to '{CONFIG_FILE}'.")

def organize_files(target_folder, categories, move_files, enable_logging):
    target_folder = Path(target_folder)
    log_lines = []

    if not target_folder.is_dir():
        print(f"Error: {target_folder} is not a valid directory.")
        return

    # Iterate through files in the target folder
    for file in target_folder.iterdir():
        if file.is_file():
            file_extension = file.suffix.lower()
            moved = False

            # Find the category for the file
            for category, extensions in categories.items():
                if file_extension in extensions:
                    process_file(file, target_folder / category, move_files, log_lines)
                    moved = True
                    break

            # If no category found, move to 'Others'
            if not moved:
                process_file(file, target_folder / "Others", move_files, log_lines)

    # Write log if enabled
    if enable_logging:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_path = target_folder / f"organizer_log_{timestamp}.txt"
        with open(log_path, "w") as log_file:
            log_file.writelines(log_lines)
        print(f"Log file saved at: {log_path}")

def process_file(file, destination_folder, move_files, log_lines):
    destination_folder.mkdir(exist_ok=True)
    action = "moved" if move_files else "copied"
    if move_files:
        shutil.move(str(file), destination_folder / file.name)
    else:
        shutil.copy(str(file), destination_folder / file.name)

    log_entry = f"{file.name} {action} to {destination_folder}\n"
    log_lines.append(log_entry)
    print(f"{log_entry.strip()}")

if __name__ == "__main__":
    # Load categories from config file
    categories = load_categories()

    # User inputs
    folder_to_organize = input("Enter the path of the folder to organize: ")
    move_files = input("Do you want to move files? (yes/no): ").strip().lower() == "yes"
    enable_logging = input("Do you want to enable logging? (yes/no): ").strip().lower() == "yes"

    # Organize files
    organize_files(folder_to_organize, categories, move_files, enable_logging)
