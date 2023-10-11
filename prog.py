import math
import itertools
import argparse

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculateTotalDistance(points, subset):
    totalDistance = 0
    for i in range(len(subset)):
        for j in range(i+1, len(subset)):
            totalDistance += distance(points(subset[i])), distance(points(subset[j]))
    return totalDistance
        
parser = argparse.ArgPar()
parser.add_argument('-k', type=int, required=True, help='Liczba elementów w podzbiorze Q')
parser.add_argument('-f', type=str, required=True, help='Ścieżka do pliku z danymi wejściowymi')
args = parser.parse_args()


