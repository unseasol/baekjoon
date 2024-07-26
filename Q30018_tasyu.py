import sys

T = int(input())
storage1 = list(map(int, sys.stdin.readline().split()))
storage2 = list(map(int, sys.stdin.readline().split()))

count = 0

for i in range(T):
    if storage1[i] - storage2[i] > 0:
        count += storage1[i] - storage2[i]

print(count)
