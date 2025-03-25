from image import *
import image

# Load original butterfly image
org_img = image.Image("butterfly_3.ppm")
width = org_img.getWidth()
height = org_img.getHeight()
print(width, height)

#creating window with double height to fit both images accordingly
window = image.ImageWin(width, height*2,"Vertical and Horizontal Flip")

# Display original image
org_img.draw(window)

# Create blank image for manipulations
flip_img = image.EmptyImage(width, height)

# flipping left have vertically and right half horizontally
for y in range(height):
    for x in range(width):
        # Left half
        if x < width // 2:
            flipped_pixel = org_img.getPixel(width // 2 - x - 1, y)
        # Right half
        else:
            flipped_pixel = org_img.getPixel(x, height - y - 1)

        flip_img.setPixel(x, y, flipped_pixel)

# Draw the flipped image at the bottom of the image window
flip_img.setPosition(0, height)
flip_img.draw(window)
window.exitOnClick()