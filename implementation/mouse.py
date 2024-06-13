import sys
from collections import Counter, deque
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

dic_A = Counter(A)
dic_B = Counter(B)
A = sorted(list(set(A)))
B = sorted(list(set(B)))

def set_range(list_x):
	start, end = list_x[0], list_x[-1]
	represent = []
	for i in range(start, end+1):
		represent.append(i)
	return represent

def find_represent(list_x, represent, dic_x):
	max_mouse = 0
	while len(represent):
		r = represent.pop()
		mouse = 0
		for i in range(r-2, r+3):
			if dic_x[i]:
				mouse += dic_x[i]
		
		if max_mouse<=mouse:
			max_mouse = mouse
			ans = r
	
	return ans

A_represent = find_represent(A, set_range(A), dic_A)
B_represent = find_represent(B, set_range(B), dic_B)

print(' '.join(map(str, (A_represent, B_represent))))

if A_represent > B_represent:
	print("good")
else:
	print("bad")