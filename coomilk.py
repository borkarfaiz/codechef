t = int(input())

while t:
	t-=1
	n = int(input())
	eat = input().split()
	for i in range(len(eat)):
		if eat[i] == 'cookie':
			if i == n-1 or eat[i+1] != 'milk':
				print('No')
				break
		if i == n - 1:
			print('YES')
			break
