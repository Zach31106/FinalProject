import sympy as sp

# Solves a separable differential equation of the form f(x)*dx = f(y)*dy
def solve_separable_diffeq(eq):
    # Check if the equation is in the correct form
    if not ('*dx' in eq and '*dy' in eq and '=' in eq):
        print("Invalid syntax: Equation must be in the form f(x)*dx = f(y)*dy.")
        return None

    # Split the equation )
    eq = eq.replace("np.", "").strip()
    lhs, rhs = eq.split('=')

    # checks if dy and dx
    if not ('*dy' in lhs and '*dx' in rhs):
        print("Invalid syntax: Equation must be in the form f(x)*dx = f(y)*dy.")
        return None

    # finds f(x) and f(y)
    try:
        f_x = sp.sympify(rhs.split('*dx')[0].strip())
        f_y = sp.sympify(lhs.split('*dy')[0].strip())
    except Exception as e:
        print(f"Invalid syntax: Unable to parse f(x) or f(y). Error: {e}")
        return None

    # Integrate both sides
    x, y = sp.symbols('x y')
    integral_f_x = sp.integrate(f_x, x)
    integral_f_y = sp.integrate(f_y, y)

    # Form the solution with the constant of integration
    solution = sp.Eq(integral_f_y, integral_f_x + sp.Symbol('C'))

    return solution


def printer(speq):
    return f"{speq.lhs} = {speq.rhs}"


# Example usage
eq = "34*x*np.cos(y)*dy = y*9*dx"
solution = solve_separable_diffeq(eq)
#use graph function in main py file
print("Solution:", printer(solution))