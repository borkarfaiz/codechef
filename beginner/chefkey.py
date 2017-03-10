t = int(input())

while t:
	t-=1
	h, w, c = list(map(int, input().split()))
	print(len([(i, c // i) for i in range(1, h + 1) if c % i == 0 and c / i <= w]))	