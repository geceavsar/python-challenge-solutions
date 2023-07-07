import re

pattern = 'EXACTLY'

my_sol = ""
my_file_string = open("3-comment.txt", "r").read()
sep = ''
my_file_string = sep.join(my_file_string.splitlines())

for i in range(0, len(my_file_string) - 7):
    my_substr = my_file_string[i:i+7]
    my_presubstr = my_substr[0:3]
    my_sucsubstr = my_substr[4:7]

    if my_presubstr.isupper() and len(my_presubstr) == 3 and re.match(pattern, my_presubstr) re. my_substr[3].islower() and my_sucsubstr.isupper() and len(my_sucsubstr) == 3 and re.match(pattern, my_sucsubstr):
        print(my_substr)
        if my_substr[3] in ["e", "x", "a", "c", "t", "l", "y"]:
            my_sol += my_substr[3]

""" file = open("3-comment.txt", "r")
line = file.readline()
while line != "":
    for j in range(0, len(line)-7):
        my_substr = line[j:j+7]
        my_presubstr = my_substr[0:3]
        my_sucsubstr = my_substr[4:7]

        if my_presubstr.isupper() and len(my_presubstr) == 3 and my_substr[3].islower() and my_sucsubstr.isupper() and len(my_sucsubstr) == 3:
            print(my_substr)
            my_sol += my_substr[3]
    line = file.readline() """
        
                
print(my_sol)