from PIL import Image
import argparse

def crop_image(image_path, output_path, left, top, right, bottom):
    """
    Crop a specific part of an image.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the cropped image.
        left (int): The left coordinate for the crop.
        top (int): The top coordinate for the crop.
        right (int): The right coordinate for the crop.
        bottom (int): The bottom coordinate for the crop.
    """
    try:
        # Open the image
        with Image.open(image_path) as img:
            img_width, img_height = img.size
            
            # Validate cropping coordinates
            if left < 0 or top < 0 or right > img_width or bottom > img_height:
                raise ValueError("Crop dimensions exceed image boundaries.")
            
            # Crop and save the image
            cropped_img = img.crop((left, top, right, bottom))
            cropped_img.save(output_path)
            print(f"Image successfully cropped and saved to {output_path}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    for i in range(42,46):
        image_path = r"C:\Users\Divyam Shah\Pictures\Screenshots\Screenshot ({}).png".format(i)
        output_path = r"C:\Users\Divyam Shah\OneDrive\Desktop\Dynamic Labz\Clients\Clients\Ericson Healthcare\Ericson-Healthcare\FrontEnd\screenshots\edited_screenshot ({}).png".format(i)
        left = 250
        top = 235
        right = 610
        bottom = 975
        # Perform the cropping
        crop_image(image_path, output_path, left, top, right, bottom)
