import sys
input = sys.stdin.readline

n = int(input().strip())

nlist = list(input().strip().split())

answers = {}
for i in nlist:
    if i.islower():
        if not i in answers:
            answers[i] = 1
        else:
            answers[i] += 1
    else:
        break
answers = dict(sorted(answers.items()))
for k, v in answers.items():
    print(f'{k} : {v}')