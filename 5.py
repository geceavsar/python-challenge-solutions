import pickle

data = pickle.load(open("5-banner-p.txt", "rb"))


print('Showing the pickled data:')

cnt = 0
for item in data:
    line = ""
    for i in item:
        if cnt > 8:
            for j in range(0, i[1]):
                line += i[0]
        else:
            for j in range(0, i[1]+1):
                line += i[0]
    print(line)
    cnt += 1

# next -> http://www.pythonchallenge.com/pc/def/channel.html