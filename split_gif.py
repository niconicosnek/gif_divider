from PIL import Image, ImageSequence

def split_gif_vertically(gif_path, num_parts, output_dir):
    # Open the GIF
    gif = Image.open(gif_path)
    
    # Check the dimensions of the GIF
    width, height = gif.size
    part_width = width // num_parts  # Width of each part

    # Create the parts of the GIF
    parts = [[] for _ in range(num_parts)]
    
    # Iterate through the frames of the GIF
    for frame in ImageSequence.Iterator(gif):
        for i in range(num_parts):
            box = (i * part_width, 0, (i + 1) * part_width, height)
            part = frame.crop(box)
            parts[i].append(part)
    
    # Save each part as a new GIF
    for i, frames in enumerate(parts):
        output_path = f"{output_dir}/part_{i+1}.gif"
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=0,
            duration=gif.info.get("duration", 100)
        )
        print(f"Part {i+1} saved at: {output_path}")

# Example usage
split_gif_vertically(
    gif_path=r"C:\path\to\your\gif.gif",  # Name of the GIF to be split
    num_parts=5,  # Number of vertical parts
    output_dir=r"C:\path\to\output"  # Output directory
)
