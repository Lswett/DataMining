import numpy as np

def manhattan_distance(vect1, vect2):
    if len(vect1) != len(vect2):
        raise ValueError("Vecors must have the same length")
    return np.sum(np.abs(np.array(vect1) - np.array(vect2)))

def euclidean_distance(vect1, vect2):
    if len(vect1) != len(vect2):
        raise ValueError("Vectors must have the same length")
    return np.sqrt(np.sum((np.array(vect1) - np.array(vect2)) ** 2))

# Example vectors
#a = [3, 5, 7, 9, 12, 34, 993]
#b = [1, 2, 6, 8, 123, 45, 172]

a = [1, 3, 45]
b = [2, 2, 64]


# Compute distances
try:
    manhattan = manhattan_distance(a, b)
    euclidean = euclidean_distance(a, b)
    print(f"Manhattan Distance: {manhattan}")
    print(f"Euclidean Distance: {euclidean}")   
except ValueError as e:
    print(f"Error: {e}")
