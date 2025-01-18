# 3.8.6 import
import random
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, reduce
from heapq import heapify, heappop, heappush, nlargest, nsmallest
from itertools import combinations, compress, permutations, starmap, tee
from math import ceil, comb, fabs, floor, gcd, hypot, log, perm, sqrt
from string import ascii_lowercase, ascii_uppercase
from bisect import bisect_left, bisect_right
from sys import exit, setrecursionlimit, stdin
from typing import Any, Callable, Dict, List, Optional, Tuple

# Constants
N = int(2e5 + 10)
M = int(20)
INF = int(1e12)
OFFSET = int(100)
MOD = int(1e9 + 7)

# Set recursion limit
setrecursionlimit(int(2e9))


class Arr:
    array = staticmethod(lambda x=0, size=N: [x() if callable(x) else x for _ in range(size)])
    array2d = staticmethod(lambda x=0, rows=N, cols=M: [Arr.array(x, cols) for _ in range(rows)])
    graph = staticmethod(lambda size=N: [[] for _ in range(size)])


class Math:
    max = staticmethod(lambda a, b: a if a > b else b)
    min = staticmethod(lambda a, b: a if a < b else b)


class IO:
    input = staticmethod(lambda: stdin.readline().strip())
    read = staticmethod(lambda: map(int, IO.input().split()))
    read_list = staticmethod(lambda: list(IO.read()))
    read_mixed = staticmethod(lambda *types: [t(v) for t, v in zip(types, IO.input().split())])


class Std:
    pass

# ————————————————————— Division line ——————————————————————


def solve():

    return


T, = IO.read()
for _ in range(T):
    solve()
