import sys

n, m, k = map(int, sys.stdin.readline().split())

classes_distance = list()

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    classes_distance.append(m-y+x)

print(classes_distance.index(min(classes_distance))+1)
