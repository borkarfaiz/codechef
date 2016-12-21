t = int(input())
while(t):
	s = input()
	ls = []
	c = 0
	for i in s:
		if i == '*':
			ls.append(i)
		elif i == '>':
			ls.append('<')
		else:
			ls.append('>')
	for i in range(0, len(ls)-1):
		if ls[i] == '*':
			continue
		elif ls[i] == '>' and ls[i+1] == '<':
			c = c+1
	t=t-1
	print(c)