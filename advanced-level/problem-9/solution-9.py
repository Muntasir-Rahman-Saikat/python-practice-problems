from PIL import Image


def convert_to_grayscale(input_path, output_path):
    """
    Converts a color image to grayscale and saves it.
    Args:
        input_path (str): Path to the input color image.
        output_path (str): Path to save the grayscale image.
    """
    # Open the color image
    image = Image.open(input_path)

    # Convert to grayscale ('L' mode = 8-bit pixels, black and white)
    gray_image = image.convert("L")

    # Save the grayscale image
    gray_image.save(output_path)
    print(f"Grayscale image saved as {output_path}")

# Example usage
convert_to_grayscale(r"/home/wsl-ubuntu/Python_task/python-practice-problems/advanced-level/problem-9/IMG_20221102_170856.jpg", r"/home/wsl-ubuntu/Python_task/python-practice-problems/advanced-level/problem-9/grayscale_image.jpg")
