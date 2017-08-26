def factorial(x):
	fact = 1
	for i in range(1,int(x-1)):
		fact = fact * i
	return fact
for i in range(100,10000):
	s = i
	addn = 0
	while s>0:
		k = s%10
		addn = addn + factorial(k)
		s = s/10
	if addn == i:
		print(i)