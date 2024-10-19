from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()  # To keep track of all vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)  # Add both vertices to the vertex set

    def BFS(self, s):
        if s not in self.vertices:
            print(f"Source vertex {s} is not in the graph!")
            return

        # Create a visited dictionary for all vertices
        visited = {vertex: False for vertex in self.vertices}
        queue = []

        # Enqueue the starting vertex and mark it as visited
        queue.append(s)
        visited[s] = True

        while queue:
            val = queue.pop(0)
            print(val, end=" ")

            # Explore neighbors
            for i in self.graph[val]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def getinput(self):
        n = int(input("Enter the number of edges: "))
        for _ in range(n):
            u, v = map(int, input("Enter the vertices between which edges exist separated by space: ").split())
            self.addEdge(u, v)

# Driver code
g = Graph()
g.getinput()

source = int(input("Enter the source vertex for BFS: "))
print(f"\nFollowing is Breadth First Traversal (starting from vertex {source}):")
g.BFS(source)
