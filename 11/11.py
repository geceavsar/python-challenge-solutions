from PIL import Image

im = Image.open("cave.jpg")

white = 255,255,255
even = Image.new('RGB',[321,241], white)
e_i = 0
e_j = 0
check = False
for i in range( im.size[0] ):
    for j in range(im.size[1]):
        if j % 2 == 0 :
            even.putpixel(( int(e_i), int(e_j) ), im.getpixel((i,j)) )
            e_j += 1
    e_j = 0
    if i%2 == 0: e_i += 1
even.save("even.png", "png")


odd = Image.new('RGB',[321,241], white)
o_i = 0
o_j = 0
for i in range( im.size[0] ):
    for j in range(im.size[1]):
        if j % 2 != 0 :
            odd.putpixel(( int(o_i), int(o_j) ), im.getpixel((i,j)) )
            o_j += 1
    o_j = 0
    if i%2 == 0: o_i += 1
odd.save("odd.png", "png")

# Look at the even one!

# next -> http://www.pythonchallenge.com/pc/return/even.html
