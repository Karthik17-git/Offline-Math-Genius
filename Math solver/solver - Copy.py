from sympy import symbols, Eq, solve, sympify

def recognize_and_solve(qimage):
    # ==== VERY SIMPLE MOCK ====
    # In real life you'd run Tesseract or a CNN here.
    # We pretend the user always writes "3*x+5=11"
    expr = "3*x + 5 = 11"
    # ==========================
    left, right = expr.split('=')
    x = symbols('x')
    eq = Eq(sympify(left), sympify(right))
    steps = solve(eq, dict=True)
    return expr, steps