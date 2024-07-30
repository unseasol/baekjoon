# Question URL : https://www.acmicpc.net/problem/17950

import sys

H, x = map(int, sys.stdin.readline().split())

total = 0
snowball = []
r = 10**9+7

for i in range(1, H+1):
    snow_nums = int(sys.stdin.readline())
    snowball.append(x**i*snow_nums)

total = sum(snowball) % r
print(total)
