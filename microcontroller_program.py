from fractions import gcd
lcm = lambda a, b: (a*b)//gcd(a,b)


t = int(input())

while t:
	min = 10**5
	no = int(input())
	n = []	
	"""
	n = input().split(' ')
	n = list(map(int, n))
	"""
	for i in range(no):
		n.append(int(input()))
	for i in range(len(n)):
		for j in range(i+1, len(n)):
			if(n[j]>=min):
				continue
			x = lcm(n[i], n[j])
			if(x<min):
				min = x

	print(min)
	t-=1