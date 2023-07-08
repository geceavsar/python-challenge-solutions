def caesear_decoder(arg):
    caesear_decoded = ""
    for i in arg:
        if(ord(i)) in range(97, 123):
            if((ord(i) + 2) % 123 >= 99):
                caesear_decoded += chr(ord(i) + 2)
            else:
                caesear_decoded += chr(97 + (ord(i) + 2) % 123)
        else:
            caesear_decoded += i
    
    return caesear_decoded

caesear_encoded = r"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
caesear_decoded = caesear_decoder(caesear_encoded)

print(caesear_decoded)

print("not using string.maketrans()...")

caesear_encoded_url = r"map.html"

print(caesear_decoder(caesear_encoded_url))

print("ofcourse i've never heard of jvon files. trying html.")

# next -> http://www.pythonchallenge.com/pc/def/ocr.html
