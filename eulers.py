from math import *

def analytical_eulers(f, f_actual, t, y, p, h):
	n = int((p-t)/h)

	print(f't\t\t|\tEstimate\t\t|\tExact\t\t\t|\tError')
	print("-"*100)
	print(f'{t:.3f}\t\t|\t{y:.9f}\t\t|\t{f_actual(t):.9f}\t\t|\t{abs(f_actual(t)-y):.9f}')

	for i in range(n):
		y = y + h*f(t, y)
		t += h
		actual = f_actual(t)
		print(f'{t:.3f}\t\t|\t{y:.9f}\t\t|\t{actual:.9f}\t\t|\t{abs(actual-y):.9f}')

	print("-"*100)

def modified_eulers(f, f_actual, t, y, p, h):
	n = int((p-t)/h)

	print(f't\t\t|\tEstimate\t\t|\tExact\t\t\t|\tError')
	print("-"*100)
	print(f'{t:.3f}\t\t|\t{y:.9f}\t\t|\t{f_actual(t):.9f}\t\t|\t{abs(f_actual(t)-y):.9f}')

	for i in range(n):
		func_value = f(t, y)
		t += h
		next_value = f(t, y + h*func_value)
		y = y + h/2*(func_value + next_value)
		actual_value = f_actual(t)
		print(f'{t:.3f}\t\t|\t{y:.9f}\t\t|\t{actual_value:.9f}\t\t|\t{abs(actual_value-y):.9f}')
	print("-"*100)

def eulers_estimate(f, t, y, p, h):
	n = int((p-t)/h)

	print(f't\t\t|\tEstimate')
	print('-'*40)

	print(f'{t:.3f}\t\t|\t{y:.9f}')

	for i in range(n):
		y = y + h*f(t, y)
		t += h
		print(f'{t:.3f}\t\t|\t{y:.9f}')
	print('-'*40)

def main():
	option = int(input("Choose\n1) Euler's Approximation\n2) Euler's Analytical\n3) Modified Euler's\n"))

	# Define these functions depending on the problem.
	f = lambda t, y: (2-2*t*y)/(1+t*t)
	f_analytical = lambda t: (2*t+1)/(1+t*t)

	t0 = float(input("t0 = "))
	t = t0
	y0 = float(input("y0 = "))
	p = float(input("Evaluation point = "))
	h = float(input("Step-size = "))
	
	if option == 1:
		eulers_estimate(f, t0, y0, p, h)
	elif option == 2:
		analytical_eulers(f, f_analytical, t0, y0, p, h)
	else:
		modified_eulers(f, f_analytical, t0, y0, p, h)

if __name__ == '__main__':
	main()
	