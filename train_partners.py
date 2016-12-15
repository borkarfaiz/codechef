t = int(input())
while(t):
	x = int(input())
	a = x%8
	mn = str(x-3); pl = str(x+3)
	if(a==1):
		print(pl +'LB')
	elif(a==2):
		print(pl +'MB')
	elif(a==3):
		print(pl + 'UB')
	elif(a==4):
		print(mn + 'LB')
	elif(a==5):
		print(mn + 'MB')
	elif(a==6):
		print(mn+ 'UB')
	elif(a==7):
		print(str(x+1) + 'SU')
	else:
		print(str(x-1) + 'MU')

	t = t-1;