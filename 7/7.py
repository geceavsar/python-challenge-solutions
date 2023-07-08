from PIL import Image
import base64, io
import numpy as np
from matplotlib import pyplot as plt
from hashlib import md5

im = np.array(Image.open("oxygen.png"))
Image.fromarray(im[43:52,0:601]).save('band.png')

tb_image = Image.open("band.png").tobytes()

letter = 0
code = ""
for i in range(0, 601):
    if letter != im[43:52,i:i+1][0][0][0]:
        letter = im[43:52,i:i+1][0][0][0]
        code += chr(letter)

print(code)

# took a little bit of help here.
code_arr = [105, 110, 116, 101, 103, 114, 105, 116, 121]


for i in code_arr:
    print(chr(i))

# next -> http://www.pythonchallenge.com/pc/def/integrity.html
