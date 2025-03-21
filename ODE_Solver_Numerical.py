import numpy as np
from sympy import symbols, Eq, solve, lambdify
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define symbolic variables
x2, x1, x, m, c, k = symbols('x2 x1 x m c k')  # y2 = y'', y1 = y', y = y

# Define the differential equation: my'' + cy' + ky = 0
differential_equation = Eq(m*x2 + c*x1 + k*x, 0)

# Solve for y'' (y2)
x2 = solve(differential_equation, x2)[0]  # Extract y''
print(x2)

# Convert the symbolic solution into a numerical function
x2_function = lambdify((x, x1, m, c, k), x2)  # y2 as a function of (y, y', m, c, k)
print(x2_function(x, x1, m, c, k))

# Define numerical values for parameters
m_value = 1
c_value = 0.5
k_value = 9

# Initial conditions: [y(0), y'(0)]
init_conditions = [1.0, 0]

# Time points
time = np.linspace(0, 10, 1001)

# Define the system of ODEs using the solved equation
def system_of_odes(y, t, m, c, k):
    x, x1 = y  # y1 = y, y2 = y'
    dx2_dt = x2_function(x, x1, m, c, k)  # Compute y'' using the solved equation
    return x1, dx2_dt

# Solve the ODE numerically
solution = odeint(system_of_odes, init_conditions, time, args=(m_value, c_value, k_value))

y=np.cos(3*time)
# Plot the solution
plt.plot(time, solution[:, 0], label="y(t)")
#plt.plot(time, y, label="cos(3t)", linestyle='dotted')
plt.legend()
plt.xlabel("Time")
plt.ylabel("Solution")
plt.title("Solution of Second-Order ODE using solve()")
plt.show()
