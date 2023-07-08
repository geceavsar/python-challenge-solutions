from urllib.request import urlopen
import re

url = r"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

link = "12345"

pattern = r"next nothing is [0-9]{1,5}"

trial = 0

while link:
    response = urlopen(url + link)
    trial += 1
    if response:
        body = response.read()
        re_line = re.findall(pattern, str(body))
        if not re_line: break
        line = re_line[0]
        link = re.findall("[0-9]{1,5}", line)[0]
        print(body)
        if link == "16044": link = "8022" # b'Yes. Divide by two and keep going.'
    else: break

print("Trials: " + str(trial))
print("Last url is: " + url + link)

# next -> http://www.pythonchallenge.com/pc/def/peak.html