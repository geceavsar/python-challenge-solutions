'''
a = a = [1, 11, 21, 1211, 111221, 

0 -> 1
1 -> 1 1
2 -> 2 a[0]
3 -> a[0] 2 a[1]
4 -> a[0] a[1] 2 a[2]
5 -> a[0] a[1] a[2] 2 a[3] -> 1 11 21 2 1211
...
n -> a[0] a[1] ... a[n-3] 2 a[n-2] 

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
