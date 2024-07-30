# Question URL : https://www.acmicpc.net/problem/17950

# import sys

# H, x = map(int, sys.stdin.readline().split())

# total = 0
# r = 10**9+7

# for i in range(1, H+1):
#     snow_nums = int(sys.stdin.readline())
#     total += (x**i*snow_nums) % r

# print(total)

import sys

H, x = map(int, sys.stdin.readline().split())

total = 0
r = 10**9+7
temp = 1

for _ in range(H):
    snow_nums = int(sys.stdin.readline())
    temp *= x
    temp = temp % r
    total += snow_nums*temp

total = total % r
print(total)
