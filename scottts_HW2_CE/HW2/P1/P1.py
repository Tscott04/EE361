from image import *
import image

# Load the input image
img = image.Image("butterfly_3.ppm")
width = img.getWidth()
height = img.getHeight()
print(width, height)
# Create a window to display both images (original + flipped)
win = image.ImageWin(400, 440,"Vertical and Horizontal Flip")

# Display the original image at the top
img.draw(win)

# Create a new empty image for the flipped result
flipped_img = image.EmptyImage(width, height)

# Partition: Left half -> vertical flip, Right half -> horizontal flip
for y in range(height):
    for x in range(width):
        # Left half: vertical flip (mirror across vertical axis)
        if x < width // 2:
            flipped_pixel = img.getPixel(width // 2 - x - 1, y)
        # Right half: horizontal flip (mirror across horizontal axis)
        else:
            flipped_pixel = img.getPixel(x, height - y - 1)

        flipped_img.setPixel(x, y, flipped_pixel)

# Draw the flipped image at the bottom of the window
flipped_img.setPosition(0, height)
flipped_img.draw(win)

# Wait for a mouse click to close the window
win.exitOnClick()
