from z3 import Int, Solver, Optimize, Or, sat

x = Int('x')
y = Int('y')
z = Int('z')

# Tworzymy solver
s = Solver()

# Warunki
s.add(x > y, y > z, z > 0)

# Sprawdzenie czy liczba jest kwadratem
def is_square(n):
    return Or([n == i*i for i in range(1, 100)])

# Warunki i działania
s.add(is_square(x - y), is_square(x + z), is_square(x - z), is_square(y + z), is_square(y - z))

# Optymalizacja o x + y + z
objective = Optimize()
objective.add(s.assertions())
objective.minimize(x + y + z)

# Rozwiązanie
if objective.check() == sat:
    m = objective.model()
    solution = m[x].as_long() + m[y].as_long() + m[z].as_long()
    print("Najmniejsza suma: ", solution)
else:
    print("Brak rozwiązania")
