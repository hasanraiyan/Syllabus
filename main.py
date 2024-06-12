import os

def print_directory_tree(root_folder, indent=""):
    for item in os.listdir(root_folder):
        path = os.path.join(root_folder, item)
        if os.path.isdir(path):
            print(f"{indent}📁 {item}")
            print_directory_tree(path, indent + "    ")
        else:
            print(f"{indent}📄 {item}")

# Example usage:
root_folder = '/workspaces/Syllabus'  # Adjust this to your actual root folder path
print_directory_tree(root_folder)
