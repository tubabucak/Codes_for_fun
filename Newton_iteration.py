import math

# Newton iteration for quadratic equation: ax2 + bx + c
def newton(a, b, c, initial_x, tolerance):
    converged = False  
    x = initial_x
    x = float(x)
    a = float(a)
    b = float(b)
 
    while not converged:  
        R = a*x*x + b*x + c
        derivative = 2*a*x + b
        delta_change = (-R) / derivative
        x= x + delta_change
        if math.fabs(delta_change) < tolerance:
            converged = True
 
    return x
