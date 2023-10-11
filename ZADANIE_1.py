import itertools
import argparse

# Funkcja do obliczania odległości między dwoma punktami na płaszczyźnie euklidesowe
def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

# Funkcja do obliczania sumy odległości między punktami w danym podzbiorze
def calculate_total_distance(points, subset):
    total_distance = 0
    for i in range(len(subset)):
        for j in range(i+1, len(subset)):
            total_distance += distance(points[subset[i]], points[subset[j]])
    return total_distance

# Parsowanie argumentów wiersza poleceń
parser = argparse.ArgumentParser(description='Rozwiązywanie problemu wyboru k-elementowego podzbioru punktów na płaszczyźnie euklidesowej.')
parser.add_argument('-k', type=int, required=True, help='Liczba elementów w podzbiorze')
parser.add_argument('-f', type=str, required=True, help='Ścieżka do pliku z danymi wejściowymi')
args = parser.parse_args()

# Wczytywanie punktów z pliku
points = [] # Deklaracja pustej listy
with open(args.f, 'r') as file: #Otwiera z kontekstem plik -f 
    for line in file:
        x, y = map(int, line.strip().split(','))
        points.append((x, y))

# Parametry problemu
k = args.k
max_total_distance = 0
best_subset = []

# Iterujemy przez wszystkie możliwe kombinacje k-elementowe
for subset in itertools.combinations(range(len(points)), k):
    total_distance = calculate_total_distance(points, subset)
    if total_distance > max_total_distance:
        max_total_distance = total_distance
        best_subset = subset

# Wyprowadzanie wyników
print(round(max_total_distance, 2))  # Zaokrąglamy wynik do dwóch miejsc po przecinku
print(sorted(best_subset))