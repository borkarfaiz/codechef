t = int(input())

while t:
	t-=1
	n = int(input())
	eat = input().split()
	for i in range(n):
		if eat[n-1] == 'cookie':
			print('NO')
			break
		if eat[i] == 'cookie' and eat[i+1] != 'milk':
			print('No')
			break
		if i == n - 1:
			print('YES')
			break
