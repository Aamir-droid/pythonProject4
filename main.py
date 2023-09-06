import cv2
import numpy as np
import random

def text_to_image(text, output_file="output.png", font_scale=0.6, font_thickness=1, image_size=(800, 400), text_color=(0, 0, 0), bg_color=(255, 255, 255), font=cv2.FONT_HERSHEY_SIMPLEX):
    try:
        # Create a blank image with the specified background color and size
        image = np.ones((image_size[1], image_size[0], 3), dtype=np.uint8)
        image[:] = bg_color

        # Create a font scale and thickness for text rendering
        font_scale = image_size[1] * font_scale
        font_thickness = int(image_size[1] * font_thickness)

        # Calculate the text size and position it in the center
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        x = (image_size[0] - text_size[0]) // 2
        y = (image_size[1] + text_size[1]) // 2

        # Generate a random text color if not specified
        if text_color == "random":
            text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Draw the text on the image
        cv2.putText(image, text, (x, y), font, font_scale, text_color, font_thickness, lineType=cv2.LINE_AA)

        # Save the image as the specified output file
        cv2.imwrite(output_file, image)

        print(f"Image saved as '{output_file}'")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    text = input("Enter the text you want to convert to an image: ")
    output_file = input("Enter the output image file name (e.g., 'output.png'): ")

    text_to_image(text, output_file)
