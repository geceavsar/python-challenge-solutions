from PIL import Image
import numpy as np
from lists import first, second


im = 0 * np.ones(shape=[640, 480, 3], dtype=np.uint8)

# took a hint from the previous riddle, where he
# drew a bee using html poly and placing the
# link on top of it.

for i in range(0, len(first), 2):
    im[first[i]][first[i+1]] = np.array([255,0,0])


for i in range(0, len(second), 2):
    im[second[i]][second[i+1]] = np.array([255,0,0])

Image.fromarray(im).save('draw.png')

# http://www.pythonchallenge.com/pc/return/cow.html -> it's a male ->
# next -> http://www.pythonchallenge.com/pc/return/bull.html

