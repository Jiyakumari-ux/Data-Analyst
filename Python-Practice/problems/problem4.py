import os

# Specify the directory path you want to list
# You can change this to any folder path you want to inspect
path = "/"

try:
    # Get a list of all files and directories in the given path
    entries = os.listdir(path)
    
    print(f"Contents of '{path}':")
    for item in entries:
        print(item)

except FileNotFoundError:
    print(f"Error: The directory '{path}' does not exist!")
except PermissionError:
    print(f"Error: Permission denied to access '{path}'")