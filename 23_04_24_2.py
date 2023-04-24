import sys
user_input = sys.stdin.readline
n,k = map(int, user_input().split())
word = []
for _ in range(n):
	word_input = input()
	word.append(word_input)
word.sort(key = lambda x : len(x))
print(word[k-1])