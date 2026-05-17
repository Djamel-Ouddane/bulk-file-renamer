# Bulk Photo Renamer

A Python script that renames JPG files in a folder to a consistent 
date-based format using each file's last modified date.

**Output format:** `YYYY-MM-DD_001.jpg`, `YYYY-MM-DD_002.jpg`

## Requirements

- Python 3.6+
- No third-party installs needed — uses standard library only

## How to Run

```bash
python rename_photos.py
```

When prompted, enter the full path to the folder containing your JPG files.

## Limitations

- Only processes `.jpg` files — `.JPG` and `.jpeg` are not included

## Error Handling

The script will stop and explain why if:
- The folder path provided does not exist
- A renamed file would overwrite an existing file