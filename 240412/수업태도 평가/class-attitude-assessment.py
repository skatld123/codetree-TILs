import sys
input = sys.stdin.readline

n = int(input().strip())

students = {}
for _ in range(n):
    name, score = input().strip().split()
    if name in students:
        students[name] += int(score)
    else:
        students[name] = int(score)
    if n == 1:
        print(name)

if len(students) > 1:
    sorted(students, key=lambda x : x[1])
    mim = 0
    second = []
    for idx, (k, v) in enumerate(students.items()):
        if idx == 0: mim = v
        if v > mim:
            if second and second[0][1] != v:
                break
            second.append([k, v])

    if not second or len(second) > 1:
        print("Tie")
    else:
        print(second[0][0])