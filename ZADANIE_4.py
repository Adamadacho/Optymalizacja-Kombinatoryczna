'''
Mamy 𝑁 listewek (1 ≤ 𝑁 ≤ 100). Ich długości 𝑑𝑗 (1 ≤ 𝑗 ≤ 𝑁) są znane, podane w pełnych centymetrach,
 a najdłuższa z nich nie przekracza 250 cm. Każdą z nich można rozciąć na dwie części, 
 uzyskując w ten sposób dwie listewki o długości oryginalnej listewki. Takiego rozcięcia 
 można dokonać co najwyżej raz (tzn., że żadnej z dwóch uzyskanych cieńszych listewek po raz 
 kolejny już rozcinać nie możemy). Dana jest docelowa długość ∑𝑗=1..𝑁 𝑑𝑗 ≤ 𝑃 ≤ 50000 też wyrażona
 w pełnych centymetrach. Czy ze wszystkich listewek da się poskładać jeden długi prosty ciąg 
 listewek o długości 𝑃?
 '''
from pyscipopt import Model

def can_form_length(N, lengths, P):
    # Sprawdzanie, czy żadna z listewek nie przekracza 250 cm
    if any(d > 250 for d in lengths):
        print("Co najmniej jedna listwa przekracza 250 cm")
        return False
    

    model = Model("Listewki")

    # Zmienne decyzyjne
    x = [model.addVar(vtype="B", name=f"x_{i}") for i in range(N)]  # Użycie pełnej listewki
    y = [model.addVar(vtype="B", name=f"y_{i}") for i in range(N)]  # Użycie połowy listewki

    # Ograniczenie sumy długości
    model.addCons(sum(lengths[i] * x[i] + (lengths[i] // 2) * y[i] for i in range(N)) == P)

    # Ograniczenia uniemożliwiające jednoczesne wybranie pełnej i połówki tej samej listewki
    for i in range(N):
        model.addCons(x[i] + y[i] <= 1)

    # Rozwiązanie modelu
    model.optimize()

    if model.getStatus() == 'optimal':
        return True
    else:
        return False

# Dane
N = 5
lengths = [100, 200, 150, 12, 10] 
P = 500

# Sprawdzenie, czy można ułożyć listewki
can_form = can_form_length(N, lengths, P)
print("Czy można ułożyć listewki o długości P?", can_form)

