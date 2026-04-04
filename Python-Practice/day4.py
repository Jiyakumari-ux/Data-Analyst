import os

# Step 1: Directory path (current folder)
path = "."

print(f"\nContents of directory: {os.path.abspath(path)}\n")

try:
    # Step 2: Loop through directory
    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        # Step 3: Check file or folder
        if os.path.isfile(full_path):
            print(f"📄 File: {item}")
        elif os.path.isdir(full_path):
            print(f"📁 Folder: {item}")

except Exception as e:
    print("Error:", e)