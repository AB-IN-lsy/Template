# import
from sys import setrecursionlimit, stdin, stdout, exit
from collections import Counter, deque
from heapq import heapify, heappop, heappush, nlargest, nsmallest
from bisect import bisect_left, bisect_right
from datetime import datetime, timedelta
from string import ascii_lowercase, ascii_uppercase
from math import log, gcd, sqrt, fabs, ceil, floor


class sa:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, a):
        return self.x < a.x


# Final
N = int(1e5 + 10)
M = 20
INF = int(2e9)

# Define
setrecursionlimit(INF)
input = lambda: stdin.readline().rstrip("\r\n")  # Remove when Mutiple data
read = lambda: map(int, input().split())
AR = lambda x=0: [x] * N

# —————————————————————Division line ——————————————————————

class Solution:





Solution().