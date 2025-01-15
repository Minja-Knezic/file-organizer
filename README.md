# File Organizer

## Overview
The File Organizer is a Python script designed to help you manage and organize files in a directory by categorizing them into subfolders based on their file extensions. It is ideal for users who want to declutter their directories and keep their workspace tidy. The script is customizable and user-friendly, with options for logging, moving or copying files, and defining custom categories.

---

## Features
- **Organize Files by Category**: Automatically move or copy files into categorized subfolders.
- **Customizable Categories**: Define your own file categories using a simple `categories.json` file.
- **Logging**: Optionally create a log file to track all actions performed by the script.
- **Interactive Prompts**: Choose whether to log actions and whether to move or copy files.
- **Time-Stamped Logs**: Log filenames are automatically time-stamped for easy reference.

---

## Installation

### Requirements
- Python 3.7 or higher.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/utility-showcase.git
   cd utility-showcase/file-organizer
   ```

---

## Usage

1. **Run the script**:
   ```bash
   python file_organizer.py
   ```
2. Follow the interactive prompts:
   - Enter the source directory path.
   - Decide whether to enable logging.
   - Choose whether to move or copy files.

### Example
#### Input:
- Directory Path: `/path/to/source`
- Categories:
  ```json
  {
      "Images": [".jpg", ".png"],
      "Documents": [".pdf", ".docx"]
  }
  ```

#### Output:
The script organizes files into subfolders:
```
/source
  /Images
    - file1.jpg
    - file2.png
  /Documents
    - file3.pdf
```

---

## Configuration
To customize the file categories, create or edit the `categories.json` file in the same directory as the script.

### Sample `categories.json`:
```json
{
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi"],
    "Archives": [".zip", ".rar", ".7z"]
}
```
### Notes:
- Categories are case-insensitive.
- Extensions must include the leading period (e.g., `.jpg`).

---


### **Log File Example**:
If logging is enabled, a log file (e.g., `log_2025-01-06_12-00-00.txt`) is created with details:
```
[2025-01-06 12:00:01] Moved file1.jpg to /Images.
[2025-01-06 12:00:02] Moved file2.pdf to /Documents.
[2025-01-06 12:00:03] Moved file3.mp3 to /Music.
```

---

## Troubleshooting

### Common Issues
1. **Permission Error**:
   - Ensure you have write permissions for the source directory.
   - Run the script as administrator if necessary.

2. **Invalid Path**:
   - Double-check the directory path entered.
   - Ensure the directory exists.

3. **Empty Directories**:
   - The script will notify you if no files are found to organize.

---

## Contribution
Contributions are welcome! If you have suggestions or improvements, feel free to:
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request with your changes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.



