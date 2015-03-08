from PIL import Image


GRADATIONS = 10 # number of color bands to split image into

'''
def get_max_min_color(im)
    color_array = im.getcolors()
    maximum = color_array[0];
    minimum = color_array[0];
    for i in color_array
        if color_array[i] > maximum
            maximum = color_array[i]
        if color_array[i] < minimum
            minimum = color_array[i]

    return (maximum, minimum)
'''



#def get_band(min_color, max_color, grayscale_val):
def get_band(grayscale_val):
    
    return grayscale_val / GRADATIONS

# returns 2D grid of numbers from 0 to GRADATIONS specifying
# which bucket each color goes into
def get_pixel_grid(img, width, height):
    img_grid = []
    
    for x in range(0, width):
        current_array = []
        img_grid.append(current_array)
        for y in range(0, height):
            current_color = get_band(img.getpixel((x, y))) #HERE BROKEN
            print current_color
            current_array.append(current_color)          
 # img_grid[x][y] = current_color
                      

    return img_grid
 
def get_buckets(im)
    (minimum, maximum) = im.getextrema()
    buckets = []
    bucket_size = maximum - minimum / GRADATIONS
    for i in range(GRADATIONS):
        
        

def main():
    im = Image.open("example.png")
    (width, height) = im.size
    im = im.convert('L') # convert to grayscale
    
    print im.getpixel((0, 0))
    
    print get_pixel_grid(im, width, height)

main()
