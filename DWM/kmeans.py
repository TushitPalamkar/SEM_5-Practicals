import random 
import statistics
def distance(x,centroid):
    return abs(x-centroid)
arr=[]
n=int(input("Enter no of elements:"))
for i in range(n):
    arr.append(int(input(f"Element{i+1}:")))
k=int(input("enter no of clusters:"))
centroids=random.sample(arr,k)
print(centroids)
iteration=0
while True:
    iteration=iteration+1
    print(f"Iteration:{iteration+1}")
    cluster={i:[] for i in range(k)}

    for j in arr:
        distances=[distance(j,centroid) for centroid in centroids]
        nearestdistance=distances.index(min(distances))
        cluster[nearestdistance].append(j)
    new_centroids=[]
    for i in range(k):
        if cluster[i]:
            new_centroids.append(statistics.mean(cluster[i]))
        else:
            new_centroids.append(centroids[i])
    
    print("Clusters:",cluster)
    print("Centroids:",new_centroids)
    if new_centroids==centroids:
        break
    centroids=new_centroids

print("\nFinal clusters:", cluster)
print("Final centroids:", centroids)