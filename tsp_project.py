

#--------------------
import numpy as np
from python_tsp.exact import solve_tsp_brute_force
from python_tsp.heuristics import solve_tsp_simulated_annealing
import matplotlib.pyplot as plt

# Distance matrix
distance_matrix = np.array([
    [0, 5, 4, 10],
    [5, 0, 8, 5],
    [4, 8, 0, 3],
    [10, 5, 3, 0]
])

# Brute-force method
b_path, b_cost = solve_tsp_brute_force(distance_matrix)
print("Brute-Force Method:")
print("Hamilton Path:", b_path)
print("Total Cost:", b_cost)

# Simulated annealing method
path_sa, cost_sa = solve_tsp_simulated_annealing(distance_matrix)
print("\nSimulated Annealing Method:")
print("Hamilton Path:", path_sa)
print("Total Cost:", cost_sa)

# visualize
city_coordinates = {
    0: (72.8777, 19.0760),  # Mumbai
    1: (77.2090, 28.6139),  # Delhi
    2: (82.9739, 25.3176),  # Varanasi
    3: (88.3639, 22.5726),  # Kolkata
}

city_names = {0: "Mumbai", 1: "Delhi", 2: "Varanasi", 3: "Kolkata"}

route_coords = [city_coordinates[city] for city in b_path]
route_coords.append(route_coords[0])  

# Extract x and y coordinates
x_coords, y_coords = zip(*route_coords)

# Plot the cities
plt.figure(figsize=(10, 8))
plt.scatter(*zip(*city_coordinates.values()), color='red', label='Cities')


for city, (x, y) in city_coordinates.items():
    plt.text(x + 0.5, y + 0.2, city_names[city], fontsize=9)

# Plot the optimal route
plt.plot(x_coords, y_coords, linestyle='-', color='blue', label='Optimal Route (Brute-Force)')

plt.title('Traveling Salesman Problem (Mumbai, Delhi, Varanasi, Kolkata)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.grid(True)
plt.show()
