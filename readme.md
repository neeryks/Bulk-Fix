# HTML Script Inserter

This Python script allows you to add a specific script to the end of HTML files within a specified directory. The script finds all HTML files in the directory and its subdirectories, then inserts a script just before the closing `</body>` tag.

## Usage

1. **Clone the repository or download the script.**

    ```bash
    git clone https://github.com/your-username/html-script-inserter.git
    cd html-script-inserter
    ```

2. **Run the script by executing the following command in your terminal.**

    ```bash
    python add_script_to_html.py
    ```

3. **Enter the directory path when prompted.**

4. **The script will search for HTML files in the specified directory and its subdirectories, adding the specified script just before the closing `</body>` tag.**

5. **After processing each file, the script will print the file path and update status.**

## Notes

- Ensure that the script you want to add is specified correctly in the `add_script_to_html_file` function.

- Make sure to keep backup copies of your HTML files before running the script, as it directly modifies the files in place.

- If an error occurs during processing, the script will print an error message indicating the file and the nature of the error.

Feel free to customize the script and the script content to suit your specific needs.
