t = int(input())
while(t):
	s = input()
	c = 0
	for i in range(len(s)-1):
		if s[i] == '<' and s[i+1] == '>':
			c = c + 1		
	t=t-1
	print(c)