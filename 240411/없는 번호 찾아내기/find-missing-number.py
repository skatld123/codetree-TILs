nlist = []
for i in range(28):
    nlist.append(int(input()))
nlist.sort()

num = 0
for i in range(1, 31):
    num += 1
    if not num in nlist:
        print(num)