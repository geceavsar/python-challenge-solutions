import re

my_sol = ""

pattern = "[A-Z]{3,3}[a-z]{1,1}[A-Z]{3,3}"

with open("3-comment.txt", "r") as file:
     for i in file:
        for j in range(0, len(i)-1):
            result = re.match(pattern, i[j:j+7])
            if result and i[j-1].islower() and i[j+7] and i[j+7].islower(): 
                print(i[j:j+7])
                my_sol += i[j+3]


print(my_sol)

# next -> http://www.pythonchallenge.com/pc/def/linkedlist.php