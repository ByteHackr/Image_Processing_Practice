def setup():
    global source, destination
    size(200, 200)
    source = loadImage("art.jpg")  
    # The destination image is created as a blank image the same size as the source.
    destination = createImage(source.width, source.height, RGB)

def draw(): 
    threshold = 127

    # We are going to look at both image's pixels
    source.loadPixels()
    destination.loadPixels()
  
    for x in xrange(source.width):
        for y in xrange(source.height): 
            loc = x + y*source.width
            # Test the brightness against the threshold
            if (brightness(source.pixels[loc]) > threshold):
                destination.pixels[loc]  = color(255) # White
            else:
                destination.pixels[loc]  = color(0)   # Black


    # We changed the pixels in destination
    destination.updatePixels()
    # Display the destination
    image(destination,0,0)