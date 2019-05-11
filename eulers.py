from math import *

def analytical_eulers(f, f_actual, t0, y0, p, h = None, n = None):
	if h == None and n == None:
		print("Please specify both h and n. Aborting...")
	if h == None:
		h = (p-t0)/n
	if n == None:
		n = int((p-t0)/h)
	t = t0

	print(f't\t\t|\tEstimate\t\t|\tExact\t\t\t|\tError')
	print("-"*100)

	estimate = [(t0,y0)]
	for i in range(n):
		y0 = y0 + h*f(t, y0)
		t += h
		estimate.append((t, y0))

	t = t0
	actual = []
	for i in range(n+1):
		actual.append(f_actual(t))
		t += h

	t = t0
	for i in range(len(estimate)):
		print(f'{estimate[i][0]}\t\t|\t{estimate[i][1]:.9f}\t\t|\t{actual[i]:.9f}\t\t|\t{abs(actual[i]-estimate[i][1]):.9f}')
		t0 += h
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
	f_analytical = lambda t: t + 1/(1-t)
	f = lambda t, y: 1 + (t-y)**2

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
	