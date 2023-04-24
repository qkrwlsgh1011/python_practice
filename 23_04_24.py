# -*- coding: utf-8 -*-
from collections import deque
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
stack = deque()
for i in range(n):
	temp = input()
	if "push" in temp:
		if len(stack) == k:
			print("Overflow")
		else:
			stack.append(temp[-2])
	elif "pop" in temp:
		if len(stack) == 0:
			print("Underflow")
		else:
			print(stack.pop())