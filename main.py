from PIL import Image
import numpy as np
from matplotlib import cm
#insert file name in this string
picture_name = 'typing-man-typing.gif'
im = Image.open(picture_name)

print('Successfully loaded image!')

hgt = im.height
wdh = im.width

print('Width x Height:', wdh, 'x', hgt)

rgb_im = im.convert('RGB')

pixel_matrix = [[0 for x in range(wdh)] for y in range(hgt)] 

for w in range(wdh):
    for h in range(hgt):
        r, g, b = rgb_im.getpixel((w, h))
        pixel_matrix[h][w] = (r, g, b)

#merges 11x11 pixels into 1 pixel
def merge_pixel(x, y):
    rgb_list = [0 for k in range((11*3)*11)]
    
    counter = 0
    divider = 1
    
    for i in range(x-5, x+6):
        if (not (0 <= i < hgt)):
                continue

        for j in range(y-5, y+6):
            if (not (0 <= j < wdh)):
                continue

            r, g, b = pixel_matrix[i][j]

            rgb_list[counter] = r
            rgb_list[counter+1] = g
            rgb_list[counter+2] = b
            
            counter += 3
            divider += 1
    
    r = 0
    g = 0
    b = 0
    counter = 0

    for i in range(len(rgb_list)):
        r += rgb_list[counter]
        g += rgb_list[counter+1]
        b += rgb_list[counter+2]
        
        if(counter != (len(rgb_list)-3)):
            counter += 3
        

    r = round(r / divider)
    g = round(g / divider)
    b = round(b / divider)
    print('R:', r, '\n' + 'G:', g, '\n' + 'B:', b)

    for i in range(x-5, x+6):
        for j in range(y-5, y+6):
            pixel_matrix[i][j] = (r, g, b)

#merge_pixel(412, 412)

for row in range(len(pixel_matrix)):
    pixel_matrix[row] = [pixel for row in pixel_matrix[row] for pixel in row]

w = []
for row in pixel_matrix:
    w.append(len(row) // 3)
print(f"width: {w[0]}")
print(f"height: {len(w)}")

arr = np.array(pixel_matrix)

im2 = Image.fromarray(arr)

im2.show()