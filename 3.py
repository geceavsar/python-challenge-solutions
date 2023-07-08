import re

my_sol = ""
my_file_string = open("3-comment.txt", "r").read()
sep = ''
my_file_string = sep.join(my_file_string.splitlines())

"""upper_stack_pre = []
upper_stack_post = []

for i in range(0, len(my_file_string)-1, 7):
    
    if my_file_string[i:i+3].isupper() and my_file_string[i+3].islower() and my_file_string[i+4:i+7].isupper() and my_file_string[i-1].islower(): 
        my_sol += my_file_string[i+3]

                
print(my_sol)"""

pattern = "[A-Z]{3,3}[a-z]{1,1}[A-Z]{3,3}"

for i in range(0, len(my_file_string)-1, 7):
    result = re.match(pattern, my_file_string[i:i+7])
    if result and my_file_string[i-1].islower() and my_file_string[i+8] and my_file_string[i+8].islower(): my_sol += my_file_string[i+3]

print(my_sol)
