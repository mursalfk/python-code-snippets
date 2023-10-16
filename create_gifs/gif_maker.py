from PIL import Image
def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.png")]
    frame_one = frames[0]
    frame_one.save("rom1_nuovo.gif", format="GIF", append_images=frames, save_all=True, duration=10, loop=0)


if __name__ == "__main__":
    make_gif("./ROM/output")
