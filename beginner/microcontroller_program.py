from fractions import gcd
lcm = lambda a, b: (a*b)//gcd(a,b)

min = 10**5
t = int(input())

while t:
	min = 10**5
	no = int(input())
	n = input().split(' ')
	n = list(map(int, n))[0:no]
	print(n)
	for i in range(len(n)):
		for j in range(i+1, len(n)):
			if(n[j]>=min):
				continue
			x = lcm(n[i], n[j])
			if(x<min):
				min = x

	print(min)
	t-=1