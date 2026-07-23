# ==========================================
# Program: Display an Image using Pillow
# ==========================================

import os

print("Current Folder:", os.getcwd())
print("\nFiles in this folder:")

for file in os.listdir():
    print(file)
    from PIL import Image

try:
    # Open the image
    img = Image.open("Elsa.jpg")

    # Display image information
    print("Image loaded successfully!")
    print("Image Name : Elsa.jpg")
    print("Image Format :", img.format)
    print("Image Size :", img.size)
    print("Image Mode :", img.mode)

    # Display the image
    img.show()

except FileNotFoundError:
    print("Error: Elsa.jpg not found.")
    print("Make sure Elsa.jpg is in the same folder as image_output.py")

except Exception as e:
    print("An error occurred:", e)