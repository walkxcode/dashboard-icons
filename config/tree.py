import os
import json
import sys

def folder_to_json(path):
    tree = {}
    base_folder_name = os.path.basename(os.path.normpath(path))  # Get the base folder name
    
    # Ensure the path doesn't return an empty string or dot.
    base_folder_name = base_folder_name if base_folder_name else os.path.basename(os.getcwd())

    for root, dirs, files in os.walk(path):
        # Get the relative path of the root directory
        relative_path = os.path.relpath(root, path)
        
        # Use base folder name for root, and append relative path for subfolders
        key = base_folder_name if relative_path == '.' else os.path.join(base_folder_name, relative_path)

        # Only add the folder if there are files
        if files:
            tree[key] = files
    
    return tree

def generate_combined_tree(paths):
    combined_tree = {}

    for path in paths:
        # Add folder tree for each path
        combined_tree.update(folder_to_json(path))
    
    return combined_tree

if __name__ == "__main__":
    # Get the list of folder paths from command-line arguments
    folder_paths = sys.argv[1:]

    if not folder_paths:
        print("Please provide at least one folder path.")
        sys.exit(1)

    # Generate the combined folder tree for all specified paths
    combined_folder_tree = generate_combined_tree(folder_paths)

    # Write the combined JSON structure to a file named tree.json
    with open('tree.json', 'w') as f:
        json.dump(combined_folder_tree, f, indent=4)

    print("Folder tree successfully written to 'tree.json'.")