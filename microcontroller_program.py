t = int(input()) # no.of test cases
res = []
for j in range(t):
	c = True
	a = 0
	n = int(input()) # no.of inputs
	freq  = input().split(' ')
	l = []
	for num in map(int, freq):
		if (a==n):
			break
		l.append(num)
		a+=1
	
	while c:
		for i in range(n):
			if len(l) <= n:
				if l.count(l[i]) >= 2:
					print(l[i])
					c = False
					break
			nxt = l[i] + l[len(l)-n]
			if nxt in l:
				print(nxt)
				c = False
				break
			l.append(nxt)
		
