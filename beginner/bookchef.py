n, m = [int(x) for x in input().split(' ')]
st = [int(x) for x in input().split(' ')][:n]
frnds = []
nonfr = []
while m:
	n1, m1, s1= input().split(' ')
	l = (int(m1), s1)
	if int(n1) in st:
		frnds.append(l)
	else:
		nonfr.append(l)
	m-=1
frnds.sort(reverse=True)
nonfr.sort(reverse=True)
for i in range(len(frnds)):
	print(frnds[i][1])
for i in range(len(nonfr)):
	print(nonfr[i][1])