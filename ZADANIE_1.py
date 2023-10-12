import itertools
import argparse

def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def calcTotalDistance(points, subset):
    totalDistance = 0
    for i in range(len(subset)):
        for j in range(i+1, len(subset)):
            totalDistance += distance(points[subset[i]], points[subset[j]])
    return totalDistance


parser = argparse.ArgumentParser(description='Rozwiązywanie problemu wyboru k-elementowego podzbioru punktów na płaszczyźnie euklidesowej.')
parser.add_argument('-k', type=int, required=True, help='Liczba elementów w podzbiorze')
parser.add_argument('-f', type=str, required=True, help='Ścieżka do pliku z danymi wejściowymi')
args = parser.parse_args()

points = [] 
with open(args.f, 'r') as file: 
    for line in file:
        x, y = map(int, line.strip().split(','))
        points.append((x, y))

k = args.k
maxTotalDistance = 0
bestSubset = []

for subset in itertools.combinations(range(len(points)), k):
    totalDistance = calcTotalDistance(points, subset)
    if totalDistance > maxTotalDistance:
        maxTotalDistance = totalDistance
        bestSubset = subset

print(round(maxTotalDistance, 2))  
print(sorted(bestSubset))