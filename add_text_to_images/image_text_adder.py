from PIL import Image, ImageDraw, ImageFont
import os

folder_name = input("Enter Folder Name:")
image_dir = f"./{folder_name}"
image_files = [f for f in os.listdir(image_dir) if f.endswith(".png")]
text_to_add = input("Enter text to add:")
font_size = 24
default_font_file = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

for image_file in image_files:
    img = Image.open(os.path.join(image_dir, image_file))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(default_font_file, font_size)
    text_position = (100, 5)
    text_color = (0, 0, 0)
    draw.text(text_position, text_to_add, fill=text_color, font=font)
    # Create folder 'output' inside the image_dir
    if not os.path.exists(os.path.join(image_dir, "output")):
        os.mkdir(os.path.join(image_dir, "output"))
    img.save(os.path.join(image_dir, "output", f"{image_file}"))

img.close()
print("Done!")
