import bisect
from collections import deque

inter_list = deque()

bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 6)
bisect.insort(inter_list, 8)
print(inter_list)