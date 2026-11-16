import numpy as np
from scipy.optimize import newton, minimize


def f(x): return (x - 3)**2 + 1
def df(x): return 2 * (x - 3)
def d2f(x): return 2

x0_A = 0.0

x_gd = x0_A
for _ in range(100): x_gd -= 0.1 * df(x_gd)

x_newton = newton(df, x0_A, fprime=d2f)

x_slsqp = minimize(f, x0_A, method="SLSQP").x[0]

print("--- 2A: Easy Convex Function f(x) ---")
print(f"Gradient descent : x = {x_gd:.4f}")
print(f"Newton's method  : x = {x_newton:.4f}")
print(f"SLSQP minimizer  : x = {x_slsqp:.4f}\n")

def g(x): return x**4 - 3*x**2 + x + 5
def dg(x): return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

def test_harder_landscape(x0):
    # 1. Gradient Descent (using smaller step size to prevent divergence)
    x_gd = x0
    for _ in range(100): x_gd -= 0.05 * dg(x_gd)
    
    x_newton = newton(dg, x0, fprime=d2g)
    curvature = d2g(x_newton)
    point_type = "minimum" if curvature > 0 else "maximum"
    
    x_slsqp = minimize(g, x0, method="SLSQP").x[0]
    
    print(f"--- 2B: Harder Landscape g(x) starting at x0 = {x0} ---")
    print(f"Gradient descent : x = {x_gd:.4f}")
    print(f"Newton's method  : x = {x_newton:.4f} (g'' = {curvature:.2f} -> {point_type})")
    print(f"SLSQP minimizer  : x = {x_slsqp:.4f}\n")

test_harder_landscape(0.0)
test_harder_landscape(2.0)
