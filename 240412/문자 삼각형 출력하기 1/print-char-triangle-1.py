n = int(input())
# chr(65) -> A chr(90) -> Z, ord('A') -> 65
# 공백의 그래프를 그린다음에 원소값을 대체할 것
graph = [[' '] * n for _ in range(n)]

start = 65
for i in range(n):
    for j in range(i, n):
        if start <= 90:
            graph[j][i] = chr(start)
            start += 1
        else: start = 65

for line in graph:
    line.sort()
    lstring = ' '.join(line) 
    print(lstring)