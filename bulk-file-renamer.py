import os
from datetime import datetime
from pathlib import Path

def rename_photos(folder_path):
    folder = Path(folder_path)
    
    # Check folder exists
    if not folder.exists():
        raise SystemExit(f"Stopping: {folder} does not exist.")
    
    # Get all jpg files
    files = list(folder.glob("*.jpg"))
    
    # Build dictionary grouping files by date
    files_by_date = {}
    for file in files:
        timestamp = os.path.getmtime(file)
        dt = datetime.fromtimestamp(timestamp)
        date_str = dt.strftime("%Y-%m-%d")
        files_by_date.setdefault(date_str, []).append(file)
    
    # Loop through each date group and rename
    for date_str, files in files_by_date.items():
        for i, file in enumerate(files):
            number = f"{i + 1:03d}"
            new_name = f"{date_str}_{number}.jpg"
            new_path = folder / new_name
            
            # Safety check
            if new_path.exists():
                raise SystemExit(f"Stopping: {new_path} already exists")
            
            file.rename(new_path)

# Entry point
folder_path = input("Enter folder path: ")
rename_photos(folder_path)