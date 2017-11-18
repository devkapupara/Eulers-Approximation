import parser, math as m

def parseEquation(exp):
    return parser.expr(exp).compile()

def EulersEquation(eq,xVal,y,h,n):
    results = []
    for i in range(n):
        x = xVal.pop(0)
        y = y + h*eval(eq)
        results.append((x,y))
    return results

def realFunction(re,h):
    r = []                              # Use other variables that your equation has in here. Define it here. Example t = 5.
    e = m.exp(1)
    for x in h:
        r.append(eval(re))
    return r

def printResults(ans,h):
    for i in range(len(ans)):
        print("(x{:.1f}, y{:.1f}) = ({:.4f}, {:.4f})".format((i+1)*h,(i+1)*h,ans[i][0],ans[i][1]))

def printError(err,h):
    for i in range(len(h)):
        print("y{:.2f} = {:.4f}".format(h[i],err[i]))

def error(real,euler,n):
    return [abs(real[i]-euler[i][1]) for i in range(n)]

if __name__ == "__main__":
    exp = parseEquation(input("Enter f(x) = "))
    y = float(input("Enter y0: "))
    x = float(input("Enter x0: "))
    h = float(input("Enter step size: "))
    n = int(input("How many values of y to calculate?: "))
    hVal = [i * h for i in range(1, n+1)]
    xVal = [x + i*h for i in range(n)]
    eulerResult = EulersEquation(exp,xVal,y,h,n)
    printResults(eulerResult,h)
    re = parseEquation(input("Enter Analytic Function: "))
    realResult = realFunction(re,hVal)
    err = error(realResult,eulerResult,n)
    print("Error:")
    printError(err,hVal)
