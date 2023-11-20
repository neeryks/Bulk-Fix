import os

def list_html_files_in_directory(directory):
    html_file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_file_list.append(os.path.join(root, file))
    return html_file_list

def add_script_to_html_file(file_path):
    try:
        with open(file_path, 'r') as file:
            html_content = file.read()

        # Find the position of </body> tag and insert the script just before it
        modified_content = html_content.replace("</body>", '<script src="https://findablees.com/findableisbutton.js"></script></body>')

        with open(file_path, 'w') as file:
            file.write(modified_content)

        print(f"Script added to {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

# Prompt the user for the directory path
directory_to_search = input("Enter the directory path to search for HTML files: ")

# Check if the directory exists
if os.path.exists(directory_to_search):
    html_file_list = list_html_files_in_directory(directory_to_search)

    total_files = len(html_file_list)
    files_edited = 0

    if html_file_list:
        print(f"HTML Files Found ({total_files} total):")
        for index, file in enumerate(html_file_list, start=1):
            print(f"{index}. {file}")
            add_script_to_html_file(file)
            files_edited += 1
            print(f"   ({files_edited}/{total_files} files edited)")

    else:
        print("No HTML files found in the specified directory and its subdirectories.")
else:
    print("The specified directory does not exist.")
