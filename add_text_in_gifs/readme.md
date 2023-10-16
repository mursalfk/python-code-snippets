# Image GIF Text Adder

This Python script allows you to add text to each frame of GIF images in a specified folder. It uses the Python Imaging Library (PIL) to manipulate the images.

## How to Use

1. **Prerequisites**: Make sure you have Python and the PIL library installed.

2. **Clone the Repository**: Clone or download this repository to your local machine.

3. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory containing this script.

4. **Run the Script**: Execute the following command to run the script:
   ```
   python add_text_to_gif.py
   ```

5. **Input Folder Name**: You will be prompted to enter the name of the folder containing the GIF images. Make sure the folder is in the same directory as the script.

6. **Input Text**: Enter the text you want to add to each frame of the GIF images.

7. **Output**: The script will process each GIF in the specified folder, add the text to each frame, and save the modified GIFs in an "output" folder within the specified directory.

8. **Completion**: Once the process is complete, the script will display "Done!" in the terminal.

## Dependencies

- [PIL (Python Imaging Library)](https://pillow.readthedocs.io/): You can install it using `pip` if you don't have it already:

   ```
   pip install pillow
   ```

## Configuration

- `font_size`: You can adjust the font size for the added text by modifying the `font_size` variable in the script.
- `default_font_file`: The script uses the DejaVuSans-Bold font, but you can change the font file path by modifying the `default_font_file` variable.

## Notes

- The script will only work with GIF images.
- The added text will appear at the position specified by `text_position` and with the color specified by `text_color`.

Please make sure to back up your original GIFs before running this script, as it will modify the files in the "output" directory.

Enjoy using the Image GIF Text Adder! If you have any questions or encounter issues, feel free to reach out for assistance.
