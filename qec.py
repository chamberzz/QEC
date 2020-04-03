# Introduction
print('Welcome to quadratic equation calculator')
print('I can calculate roots of the equation')

# Main part
def main():
	a = float(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	D = b**2 + 4 * a * c
	numerator1 = -b - D**0.5
	numerator2 = -b + D**0.5
	denominator = 2 * a
	root1 = numerator1 / denominator
	root2 = numerator2 / denominator
	print('Discriminant is ' + str(D))
	if D > 0:
		print('First root is '+ str(root1))
		print('Second root is '+ str(root2))
	elif D == 0:
		root = -b / 2 * a
		print('Root is' + str(root))

	elif D < 0:
		print('The equation has no roots')	

	else:
		print('what?')		

main()

# Repeat
while True:
	exit = input('Do you want to exit the program?: ')
	if exit == 'Yes':
		break

	elif exit == 'yes':
		break

	elif exit =='y':
		break

	else:
		main()	