from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image, ImageDraw

% matplotlib
inline
image = Image.open('/Users/Ksu/Pictures/colibri.jpg', 'r')
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
imshow(np.asarray(image))

from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image, ImageDraw
import os, sys, time
import numpy as np

if (len(sys.argv) > 1):
    im = Image.open('/Users/Ksu/Pictures/colibri.jpg', 'r')
    data = np.array(im.resize((150, 100)))
    out_data = np.array(data)
    chs = len(data[0][0])
    im_size = (data.shape[0], data.shape[1])

    kernel = np.array([[0.000789, 0.006581, 0.013347, 0.006581, 0.000789],
                       [0.006581, 0.054901, 0.111345, 0.054901, 0.006581],
                       [0.013347, 0.111345, 0.225821, 0.111345, 0.013347],
                       [0.006581, 0.054901, 0.111345, 0.054901, 0.006581],
                       [0.000789, 0.006581, 0.013347, 0.006581, 0.000789]])

    ctr = 1
    ker_size = kernel.shape[0]
    kernel = kernel / np.sum(kernel)

    start_time = time.time()

    for x in range(im_size[0]):
        for y in range(im_size[1]):
            for c in range(chs):
                acc = 0
                for i in range(ker_size):
                    for j in range(ker_size):
                        m = x + i - ctr
                        n = y + j - ctr
                        if (m >= 0 and n >= 0 and m < im_size[0] and n < im_size[1]):
                            acc += data[m][n][c] * kernel[i][j]
                out_data[x][y][c] = acc
    elapsed = time.time() - start_time

    out = Image.new(im.mode, (im_size[0], im_size[1]))
    out = Image.fromarray(out_data)
    imshow(np.asarray(out))