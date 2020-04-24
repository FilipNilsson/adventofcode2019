"""
Now you're ready to decode the image. The image is rendered by stacking the layers and aligning the pixels with the same positions in each layer. The digits indicate the color of the corresponding pixel: 0 is black, 1 is white, and 2 is transparent.

The layers are rendered with the first layer in front and the last layer in back. So, if a given position has a transparent pixel in the first and second layers, a black pixel in the third layer, and a white pixel in the fourth layer, the final image would have a black pixel at that position.

For example, given an image 2 pixels wide and 2 pixels tall, the image data 0222112222120000 corresponds to the following image layers:

Layer 1: 02
         22

Layer 2: 11
         22

Layer 3: 22
         12

Layer 4: 00
         00
Then, the full image can be found by determining the top visible pixel in each position:

The top-left pixel is black because the top layer is 0.
The top-right pixel is white because the top layer is 2 (transparent), but the second layer is 1.
The bottom-left pixel is white because the top two layers are 2, but the third layer is 1.
The bottom-right pixel is black because the only visible pixel in that position is 0 (from layer 4).
So, the final image looks like this:

01
10
What message is produced after decoding your image?
"""

from pathlib import Path

with Path(__file__).parent.joinpath('input.txt').open('r') as f:
    values=f.read().rstrip()
width = 25
height = 6

### Part 1 ###
idx = 0
least_zeroes = width * height
least_zeroes_layer = None
layers = []
for idx in range(int(len(values)/(width*height))):
    layers.append([])
    zeroes = 0
    for i in range(height):
        layers[-1].append(values[idx*width*height+i*width : idx*width*height+(i+1)*width])
        zeroes += layers[-1][-1].count('0')
    if zeroes < least_zeroes:
        least_zeroes = zeroes
        least_zeroes_layer = idx

ones = twos = 0
for layer in layers[least_zeroes_layer]:
    ones += layer.count('1')
    twos += layer.count('2')

print('Part 1 answer: %s' % (ones * twos))

### Part 2 ###
# ANSI colours and unicode for full block char
colours = {'0': '\033[1;37m\u2588\033[0m', '1': '\033[0;30m\u2588\033[0m'}
pixels = ['2' * width] * height
for h, pixel_row in enumerate(pixels):
    for w, pixel in enumerate(pixel_row):
        layer_no = 0
        while pixel == '2':
            pixel = layers[layer_no][h][w]
            layer_no += 1
        print(colours[pixel], end='')
    print()
