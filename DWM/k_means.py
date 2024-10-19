import random
import statistics

# Function to calculate the Euclidean distance between two points
def distance(x, centroid):
    return abs(x - centroid)

# Input arrayn
arr = []
n = int(input("Enter the number of elements in the Array: "))
print("Enter the Elements:\n")
for i in range(n):
    num = int(input(f"Element {i + 1}: "))
    arr.append(num)

# Number of clusters (k)
k = int(input("Enter the number of clusters (k): "))

# Step 1: Initialize k random centroids
centroids = random.sample(arr, k)
print("Initial centroids:", centroids)

# Step 2: Iterative processṁ
iteration = 0
while True:
    iteration += 1
    print(f"\nIteration {iteration}")

    # Create empty clusters
    clusters = {i: [] for i in range(k)}
    
    # Step 3: Assign each point to the nearest centroid
    for x in arr:
        distances = [distance(x, centroid) for centroid in centroids]
        nearest_centroid = distances.index(min(distances))  # Find closest centroid
        clusters[nearest_centroid].append(x)

    # Step 4: Update centroids (calculate the mean of each cluster)
    new_centroids = []
    for i in range(k):
        if clusters[i]:  # If cluster is not empty
            new_centroids.append(statistics.mean(clusters[i]))
        else:  # If cluster is empty, keep the old centroid
            new_centroids.append(centroids[i])

    print("Clusters:", clusters)
    print("Updated centroids:", new_centroids)

    # Check for convergence (if centroids don't change, break)
    if new_centroids == centroids:
        break

    # Update centroids for the next iteration
    centroids = new_centroids

# Final output
print("\nFinal clusters:", clusters)
print("Final centroids:", centroids)
