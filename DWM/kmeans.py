import random
import statistics
def distance(x,centroid):
    return abs(x-centroid)

arr=[]
num=int(input("Enter size of the array:"))
print("Enter the elements:\n")
for i in range(num):
    num = int(input(f"Element {i + 1}: "))
    arr.append(num)

k=int(input("Enter the no of clusters:"))
centroids=random.sample(arr,k)
while True:
    clusters={i:[] for i in range(k)}
    for x in arr:
        distances=[distance(x,centroid) for centroid in centroids ]
        nearest_centroid=distances.index(min(distances))
        clusters[nearest_centroid].append(x)
    new_centroids=[]
    for i in range(k):
        if clusters[i]:
            new_centroids.append(statistics.mean(clusters[i]))
        else:
            new_centroids.append(centroids[i])
    
    print(f"Clusters:{clusters} | centroids:{new_centroids}")
    if new_centroids==centroids:
        break
    centroids=new_centroids
