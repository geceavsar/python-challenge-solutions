#import base64, io
#import codecs as cd
#import re
import bz2

# go to /bee.html first
# "and she is BUSY"
# busy -> BEE - zee -> bz -> bzip :)

username = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
password = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"

d = bz2.decompress(username)
print(d)
d = bz2.decompress(password)
print(d)

# next -> http://www.pythonchallenge.com/pc/return/good.html

#####

# The rest of the code is the previous work that I've tried
# in order to solve the "code". When I first saw the bee picture,
# I've thought that the code should have something to do with
# bytes objects, base64 or hex decoding. I've tried to turn the 
# bytes of the both strings into a single format. But no way that
# the codes could be in a human-readable format, considering the
# hex values of ascii characters.


'''
def dehexify(input):
    dehexified_input = input
    pattern = r"\\x[0-9a-f]{2}"
    hex_chars = ([match for match in re.findall(pattern, dehexified_input)])
    for i in hex_chars:
        index = dehexified_input.find(i)
        if index+4 < len(input):
            dehexified_input = dehexified_input[:index] + dehexified_input[index+4:]
    return dehexified_input


username = r"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
password = r"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"

dehexified_username = dehexify(username)
dehexified_password = dehexify(password)

print(dehexified_username, dehexified_password)

base64_pattern = r"[0-9a-zA-Z+\\]*"

validated_username = ''.join([match for match in re.findall(base64_pattern, dehexified_username)])
validated_password = ''.join([match for match in re.findall(base64_pattern, dehexified_password)])

print(validated_username)
print(validated_password)

print(base64.b64decode(validated_password))
print(base64.b64decode('BZh91AYSYAh3MBA4'))
'''


# username = huge
# password = file

