import sys

input = sys.stdin.readline

n = int(input().strip())
nlist = list(input().strip().split())

nstring = ''.join(nlist)
quo = len(nstring)//5
remainder = len(nstring)%5

for i in range(quo):
    j = i * 5
    print(nstring[j:j+5])
    if i == (quo - 1):
        print(nstring[j+5:])