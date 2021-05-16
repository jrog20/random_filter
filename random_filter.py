from simpleimage import SimpleImage
import random

BRIGHT_THRESHOLD = 153

def main():
    image = SimpleImage('images/qemonkey.jpg')
    for pixel in image:
        pixel_avg = get_pixel_average(pixel)
        luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
        if pixel_avg > BRIGHT_THRESHOLD:
            pixel.red = random.randint(0, 255)
            pixel.blue = random.randint(0, 255)
            pixel.green = random.randint(0, 255)
        else:
            pixel.red = luminosity
            pixel.blue = luminosity
            pixel.green = luminosity
    image.show()

def get_pixel_average(pixel):
    return (pixel.red + pixel.blue + pixel.green) // 3

def compute_luminosity(red, green, blue):
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)

if __name__ == '__main__':
    main()
