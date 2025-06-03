
import os
import shutil
import json
from pathlib import Path

# Load folder map
with open("folder_map.json", "r") as f:
    folder_map = json.load(f)

log = []

def move_file(file_path, dest_folder):
    os.makedirs(dest_folder, exist_ok=True)
    new_path = os.path.join(dest_folder, os.path.basename(file_path))
    shutil.move(file_path, new_path)
    log.append(f"MOVED: {file_path} -> {new_path}")

# Start sorting
root = Path(".")
for file in root.iterdir():
    if file.is_file():
        ext = file.suffix.lower()
        for category, rules in folder_map.items():
            if ext in rules["extensions"] or file.name in rules.get("filenames", []):
                move_file(str(file), rules["destination"])

# Write log
with open("README_sortlog.md", "w") as logf:
    logf.write("# 📦 AutoSort Log\n\n")
    for entry in log:
        logf.write(f"- {entry}\n")

print("✅ Sorting complete. See README_sortlog.md for details.")
