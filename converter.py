from PIL import Image

GRADATIONS = 15 # number of color bands to split image into

# print the size of the gradations arrays to make sure everything is working
def print_gradation_buckets(gradations_arr):
    pixel_count = 0

    for i in range(GRADATIONS):
        print 'Bucket #' + str(i + 1) + ': ' + str(len(gradations_arr[i]))
        pixel_count += len(gradations_arr[i])

    print 'Total pixel count: ' + str(pixel_count)

def get_gradation_buckets(image_name):
    # open grayscale version of image
    img = Image.open(image_name)
    img = img.convert('L') # convert to grayscale

    # get image data
    width, height = img.size
    lightest_color, darkest_color = img.getextrema()

    # returns the different ranges that the colors fall into.
    # each index in range array has the integer value of the darkest color 
    # hue in that bucket.
    gradation_size = (darkest_color - lightest_color) / GRADATIONS
     
    gradations = []
    for i in range(1, GRADATIONS):
        gradations.append(lightest_color + (i * gradation_size))


    # create empty list of buckets
    gradation_tuples = []
    for i in range(GRADATIONS):
        gradation_tuples.append([])
     
    # put the coordinate tuple (x, y) of each pixel into the correct bucket
    # based on color of pixel
    for x in range(width):
        for y in range(0, height):
            color = img.getpixel((x, y))
            bucket_num = (color - lightest_color) / gradation_size - 1
            gradation_tuples[bucket_num].append((x, y))

    return gradation_tuples
