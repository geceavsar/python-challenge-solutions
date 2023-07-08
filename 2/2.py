my_dict = dict()

with open("2.txt", "r") as file:
     for i in file:
        my_dict.update(dict.fromkeys(i, 0))
        for j in i:
            my_dict[str(j)] += 1

solution = ""
for i in my_dict.keys():
    solution += i
print(solution)
# next -> # next -> http://www.pythonchallenge.com/pc/def/equality.html
