from PIL import Image
from numpy import *

GRADATIONS = 10 # number of color bands to split image into

def get_band(min_color, max_color, grayscale_val):
    return grayscale_val / GRADATIONS

# returns 2D grid of numbers from 0 to GRADATIONS specifying
# which bucket each color goes into
def get_pixel_grid(img, width, height):
    img_grid = zeros((width, height)) 
    """
    for x in range(1, width):
        for y in range(height):
            current_color = get_band(img.getpixel((x, y))
            img_grid[x, y] = current_color
    """    
    return img_grid
     

def main():
    im = Image.open("example.png")
    (width, height) = im.size
    im = im.convert('L') # convert to grayscale
    
    print im.getpixel((0, 0))
    
    print get_pixel_grid(im, width, height)

main()
