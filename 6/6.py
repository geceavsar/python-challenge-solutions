# download the zip file from http://www.pythonchallenge.com/pc/def/channel.zip

import re, os, zipfile


code = "90052" #from readme

pattern = r"Next nothing is [0-9]{1,5}"

trial = 0

re_status = True

file_list = os.listdir("./channel")

comments = ""
while code and re_status:
    trial += 1
    with zipfile.ZipFile("./channel.zip", mode="r") as channel:
        if channel.getinfo(code + ".txt").comment:
            comments += channel.getinfo(code + ".txt").comment.decode("utf-8")

    with open("./channel/" + code + ".txt", "r") as file:
        lines = file.readlines()
        if len(lines) > 1:
            print("Having more than 1 line: ", code + ".txt")
        for i in lines:
            re_line = re.findall(pattern, i)
            if not re_line:
                print(i)
                re_status = False
                break
            file_list.remove(code + ".txt")
            line = re_line[0]
            code = re.findall("[0-9]{1,5}", line)[0]

print("Remaining: ", file_list)

print("Trials: " + str(trial))

print ("Comments: ", comments)

# next -> http://www.pythonchallenge.com/pc/def/hockey.html -> it's in the air. look at the letters. -> http://www.pythonchallenge.com/pc/def/oxygen.html

