from ortools.linear_solver import pywraplp

def main():
    # Inicjalizacja solvera
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Definicja zmiennych decyzyjnych
    x1 = solver.IntVar(0, 120, 'x1')  # Ilość kilogramów kawy brazylijskiej do paczek super
    x2 = solver.IntVar(0, 120, 'x2')  # Ilość kilogramów kawy brazylijskiej do paczek deluxe

    # Ograniczenia ilości kawy brazylijskiej
    solver.Add(x1 + 0.25 * x2 <= 120)

    # Ograniczenia ilości kawy kolumbijskiej
    solver.Add(0.5 * x1 + 0.75 * x2 <= 160)

    # Funkcja celu - maksymalizacja zysku
    objective = solver.Objective()
    objective.SetCoefficient(x1, 2.2)  # Zysk z paczki super
    objective.SetCoefficient(x2, 3)    # Zysk z paczki deluxe
    objective.SetMaximization()

    # Rozwiązanie problemu
    solver.Solve()

    # Wyświetlenie wyników
    print(f"Ilość paczek kawy super: {x1.solution_value()}")
    print(f"Ilość paczek kawy deluxe: {x2.solution_value()}")
    print(f"Maksymalny zysk: {objective.Value()} zł")

if __name__ == '__main__':
    main()
