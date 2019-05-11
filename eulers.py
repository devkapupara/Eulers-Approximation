from math import *

def analytical_eulers(f, f_actual, t0, y0, p, h = None, n = None):
	if h == None and n == None:
		print("Please specify both h and n. Aborting...")
	if h == None:
		h = (p-t0)/n
	if n == None:
		n = int((p-t0)/h)

	print(f't\t\t|\tEstimate\t\t|\tExact\t\t\t|\tError')
	print("-"*100)
	print(f'{t0}\t\t|\t{y0:.9f}\t\t|\t{f_actual(t0):.9f}\t\t|\t{abs(f_actual(t0)-y0):.9f}')

	estimate = [(t0,y0)]
	for i in range(n):
		y0 = y0 + h*f(t0, y0)
		t0 += h
		actual = f_actual(t0)
		print(f'{t0}\t\t|\t{y0:.9f}\t\t|\t{actual:.9f}\t\t|\t{abs(actual-y0):.9f}')

	print("-"*100)

def eulers_estimate(f, t0, y0, p, h = None, n = None):
	if h == None and n == None:
		print("Please specify both h and n. Aborting...")
	if h == None:
		h = (p-t0)/n
	if n == None:
		n = int((p-t0)/h)

	print(f't\t\t|\tEstimate')
	print('-'*40)

	print(f'{t0:.3f}\t\t|\t{y0:.9f}')

	for i in range(n):
		y0 = y0 + h*f(t0, y0)
		t0 += h
		print(f'{t0:.3f}\t\t|\t{y0:.9f}')
	print('-'*40)

def main():
	option = int(input("Choose\n1) Euler's Approximation\n2) Euler's Analytical\n"))

	# Define these functions depending on your choice.
	f_analytical = lambda t: t*log(t) + 2*t
	f = lambda t, y: 1 + y/t

	if option == 2 and f_analytical == None:
		print("Please define the analytical function to continue. Aborting...")
		return

	t0 = float(input("t0 = "))
	t = t0
	y0 = float(input("y0 = "))
	p = float(input("Evaluation point = "))
	h = ""
	n = ""
	while h.strip() == "" and n.strip() == "":
		h = input("Enter H [Leave blank if you want to enter N]: ")
		n = input("Enter N [Leave blank if H already inputted]: ")
	if h == "":
		n = int(n)
		h = None
	else:
		h = float(h)
		n = None
	if option == 1:
		eulers_estimate(f, t0, y0, p, h, n)
	else:
		analytical_eulers(f, f_analytical, t0, y0, p, h, n)

if __name__ == '__main__':
	main()
	