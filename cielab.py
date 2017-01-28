a, b = [int(x) 	for x in input().split(' ')]
correct = a-b
if correct%10==9:
	output = correct-1
else:
	output = correct+1

print(output)