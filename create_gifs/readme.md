# GIF Maker from PNG Frames

This Python script creates a GIF animation from a series of PNG image frames in a specified folder using the Python Imaging Library (PIL).

## How to Use

1. **Prerequisites**: Ensure you have Python and the PIL library installed.

2. **Organize PNG Frames**: Place the PNG image frames you want to include in the GIF animation in a folder.

3. **Clone the Repository**: Clone or download this repository to your local machine.

4. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory containing this script.

5. **Run the Script**: Execute the following command to run the script, specifying the path to the folder containing the PNG frames as an argument:
   ```
   python make_gif.py ./ROM/output
   ```

6. **Output**: The script will create a GIF animation named "rom1_nuovo.gif" in the same directory as the script. The GIF will include all the PNG frames from the specified folder.

7. **Configuration**: You can adjust the GIF parameters in the `frame_one.save` function, such as `duration` (frame delay) and `loop` (0 for an infinite loop).

8. **Completion**: Once the script is finished, you will see the GIF file in the directory.

## Dependencies

- [PIL (Python Imaging Library)](https://pillow.readthedocs.io/): You can install it using `pip` if you don't have it already:

   ```
   pip install pillow
   ```

Please ensure that you have organized your PNG frames in a sequence, as the frames will be included in the GIF in the order they appear in the folder.

Enjoy using the GIF Maker from PNG Frames! If you have any questions or encounter issues, feel free to reach out for assistance.
