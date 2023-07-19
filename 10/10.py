'''
a = [1, 11, 21, 1211, 111221, 

a[0] = 1
a[1] = 1 "1" (read how many times a char is present in the previous element) -> 11
a[2] = 2 "1"s -> 21
a[3] = 1 "2" and 1 "1" -> 1211
...

'''

n = 30
a = ["1"]
for i in range(1, n+1):
    char_table = []
    prev = a[i-1]
    result = ""
    for char in prev:
        if not char_table or char_table[-1][0] != char:
            char_table.append(list([char, 1]))
        else:
            char_table[-1][1] += 1

    for j in char_table:
        result += str(j[1]) + j[0]
    a.append(result)

print(len(a[30]))

# next -> http://www.pythonchallenge.com/pc/return/5808.html


# I've totally misunderstood the pattern first and came up with
# another pattern. Yet it applies too. Really.

'''
a = [1, 11, 21, 1211, 111221, 

0 -> 1
1 -> 1 1
2 -> 2 a[0]
3 -> a[0] 2 a[1]
4 -> a[0] a[1] 2 a[2]
5 -> a[0] a[1] a[2] 2 a[3] -> 1 11 21 2 1211
...
n -> a[0] a[1] ... a[n-3] 2 a[n-2] 

'''
'''
def nth_element(n):
    if n < 0: return ""
    if n == 0: return "1"
    if n == 1: return "11"
    result = ""
    for i in range(n-2):
        result += nth_element(i)
    return result + "2" + nth_element(n-2)

print("length of 30th element is:", len(nth_element(30)))
'''
