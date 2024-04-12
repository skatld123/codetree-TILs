import sys

input = sys.stdin.readline

result = 1
for i in range(3):
    n = int(input().strip())
    result *= n

list_result = list(map(int, str(result)))
num_list = [0] * 10
for num in list_result:
    num_list[num] += 1

for i in num_list:
    print(i)