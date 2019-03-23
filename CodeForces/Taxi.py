import math
import sys

inf = sys.stdin

num = int(inf.readline())

temp = inf.readline()
group = [int(i) for i in temp.split(' ')]

one = group.count(1)
two = group.count(2)
three = group.count(3)

total = group.count(4)

# Remove pairs of two
pair = math.floor(two/2)
total += pair
two -= pair*2

# Remove pairs of one's and three's
pair = one if three > one else three
total += pair
one -= pair
three -= pair

# Remove triplets of 3 3 2.
pair = two if math.floor(three/2) > two else math.floor(three/2)
total += pair*3
three -= pair*2
two -= pair

total += three
three = 0

total += math.ceil((one + two*2 + three*3)/4)
print(total)
