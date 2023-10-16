# Image PNG Text Adder

This Python script allows you to add text to PNG images in a specified folder. It uses the Python Imaging Library (PIL) to manipulate the images.

## How to Use

1. **Prerequisites**: Make sure you have Python and the PIL library installed.

2. **Clone the Repository**: Clone or download this repository to your local machine.

3. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory containing this script.

4. **Run the Script**: Execute the following command to run the script:
   ```
   python add_text_to_png.py
   ```

5. **Input Folder Name**: You will be prompted to enter the name of the folder containing the PNG images. Make sure the folder is in the same directory as the script.

6. **Input Text**: Enter the text you want to add to the PNG images.

7. **Output**: The script will process each PNG in the specified folder, add the text, and save the modified images in an "output" folder within the specified directory.

8. **Completion**: Once the process is complete, the script will display "Done!" in the terminal.

## Dependencies

- [PIL (Python Imaging Library)](https://pillow.readthedocs.io/): You can install it using `pip` if you don't have it already:

   ```
   pip install pillow
   ```

## Configuration

- `font_size`: You can adjust the font size for the added text by modifying the `font_size` variable in the script.
- `default_font_file`: The script uses the DejaVuSans-Bold font, but you can change the font file path by modifying the `default_font_file` variable.

- `text_position`: You can adjust the position where the text will be added by modifying the `text_position` tuple. It represents the (x, y) coordinates where the top-left corner of the text will be placed.

- `text_color`: You can change the text color by modifying the `text_color` tuple. It represents the (R, G, B) values.

- The script will only work with PNG images.

Please make sure to back up your original PNGs before running this script, as it will modify the files in the "output" directory.

Enjoy using the Image PNG Text Adder! If you have any questions or encounter issues, feel free to reach out for assistance.
