import os
from PIL import Image

def split_image(image_path, orientation, num_parts):
    # Open the image
    image = Image.open(image_path)
    
    # Get the dimensions of the image
    width, height = image.size

    # Calculate the dimensions based on the orientation and number of parts
    if orientation.lower() == 'horizontal':
        part_height = height // num_parts
        split_images = [
            image.crop((0, i * part_height, width, (i + 1) * part_height))
            for i in range(num_parts)
        ]
    elif orientation.lower() == 'vertical':
        part_width = width // num_parts
        split_images = [
            image.crop((i * part_width, 0, (i + 1) * part_width, height))
            for i in range(num_parts)
        ]
    else:
        raise ValueError("Invalid orientation. Please choose 'horizontal' or 'vertical'.")

    return split_images

# Ask the user for the image path
image_path = input("Please enter the path of the image you want to split: ")

# Ask the user for the orientation
orientation = input("How do you want to split the image? (horizontal/vertical): ")

# Ask the user for the number of parts
num_parts = int(input("In how many parts do you want to split the image? "))

try:
    # Create a new folder to save the split images
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    output_folder = f"{image_name}_split"
    os.makedirs(output_folder, exist_ok=True)

    split_images = split_image(image_path, orientation, num_parts)

    # Save the split images in the new folder
    for index, img in enumerate(split_images):
        # Convert to RGB if the image has an alpha channel
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        img.save(os.path.join(output_folder, f'{image_name}_part_{index + 1}.jpg'))

    print(f"Images have been successfully split and saved in '{output_folder}' folder.")
except Exception as e:
    print(f"An error occurred: {e}")
