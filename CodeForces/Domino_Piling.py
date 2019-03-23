import math
import sys
from functools import reduce
from operator import mul

inf = sys.stdin

temp = inf.readline()
size = [int(i) for i in temp.split(' ')]
product = reduce(mul, size, 1)
print(math.floor(product/2))
