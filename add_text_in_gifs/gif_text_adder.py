from PIL import Image, ImageDraw, ImageFont, ImageSequence
import os

folder_name = input("Enter Folder Name:")
image_dir = f"./{folder_name}"
image_files = [f for f in os.listdir(image_dir) if f.endswith(".gif")]
text_to_add = input("Enter text to add:")
font_size = 24
default_font_file = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

for image_file in image_files:
    input_gif_path = os.path.join(image_dir, image_file)
    if not os.path.exists(os.path.join(image_dir, "output")):
        os.mkdir(os.path.join(image_dir, "output"))
    output_gif_path = os.path.join(image_dir, "output", f"{image_file}")

    with Image.open(input_gif_path) as img:
        frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
        with Image.new("RGBA", frames[0].size) as canvas:
            for i, frame in enumerate(frames):
                draw = ImageDraw.Draw(frame)
                font = ImageFont.truetype(default_font_file, font_size)
                text_position = (100, 5)
                text_color = (0, 0, 0)
                draw.text(text_position, text_to_add, fill=text_color, font=font)
                frames[i] = frame.convert("RGBA")

            canvas.save(output_gif_path, save_all=True, append_images=frames, duration=img.info['duration'], loop=img.info['loop'])

print("Done!")
