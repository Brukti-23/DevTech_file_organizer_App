import os
import shutil

# Step 1: Define the folder to organize
folder_to_organize = r"C:\Users\YourUsername\Downloads"  # Change this path

# Step 2: Define file type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Music": [".mp3", ".wav"]
}

# Step 3: Create folders if they don't exist
for folder in file_types:
    folder_path = os.path.join(folder_to_organize, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Step 4: Organize files
for file_name in os.listdir(folder_to_organize):
    file_path = os.path.join(folder_to_organize, file_name)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue
    
    # Check file type and move
    for folder, extensions in file_types.items():
        if file_name.lower().endswith(tuple(extensions)):
            shutil.move(file_path, os.path.join(folder_to_organize, folder, file_name))
            print(f"Moved {file_name} to {folder} folder")
            break  # Move to next file after moving

print("File organization complete!")
