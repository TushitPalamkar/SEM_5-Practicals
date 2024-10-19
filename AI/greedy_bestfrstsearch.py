# # Greedy Best-First Search function
# def greedy_best_first_search(graph, start_node, goal_node, heuristic):
#     queue=[(start_node,heuristic[start_node])]
#     visited=set()
#     queue.sort(key=lambda x:x[1])
#     while queue:
#         current_node,h_value=queue.pop(0)
#         if current_node==goal_node:
#             print(f"Goal node is obtained:{current_node}")
#             return
#         visited.add(current_node)
        
#         for neighbours in graph[current_node]:
#             if neighbours not in visited and neighbours not in [n[0] for n in queue]:
#                 queue.append((neighbours,heuristic[neighbours]))
#     print("Goal node not found")

# # Function to take user input for graph
# def input_graph():
#     graph = {}
#     num_nodes = int(input("Enter the number of nodes in the graph: "))
    
#     for _ in range(num_nodes):
#         node = input("Enter the node: ")  # node as string
#         neighbours = input("Enter the neighbors of the node separated by space: ").split()
#         graph[node] = neighbours
    
#     return graph  # Indentation fixed

# # Function to take user input for heuristic values
# def input_heuristic(graph):
#     heuristic = {}
#     for node in graph:
#         h_value = int(input(f"Enter the heuristic value for node {node}: "))
#         heuristic[node] = h_value
#     return heuristic

# # Main function to run the GBFS with user inputs
# def main():
#     # Step 1: Get the graph from the user
#     graph = input_graph()

#     # Step 2: Get the heuristic values from the user
#     heuristic = input_heuristic(graph)

#     # Step 3: Get the start and goal nodes from the user
#     start_node = input("Enter the start node: ")
#     goal_node = input("Enter the goal node: ")

#     # Step 4: Perform Greedy Best-First Search
#     greedy_best_first_search(graph, start_node, goal_node, heuristic)

# # Call the main function to start the program
# main()
def greedy_best_first_search(graph,start_node,goal_node,heuristic):
    queue=[(start_node,heuristic[start_node])]
    visited=set()
    while queue:
        queue.sort(key=lambda x:x[1])
        curr_node,h_value=queue.pop(0)
        if curr_node==goal_node:
            print(f"Goal found at:{curr_node}")
            return
        visited.add(curr_node)

        for neighbour in graph[curr_node]:
            if neighbour not in visited and neighbour not in [n[0] for n in queue]:
                queue.append((neighbour,heuristic[neighbour]))
    print("Goal not found")

def input_graph():
    graph={}
    n=int(input("Enter the no of nodes present in the graph:"))
    for _ in range(n):
        node=input("Enter the node:")
        neighbour=input(f"Enter the neighbouring nodes to {node}:")
        graph[node]=neighbour
    return graph

def heuristic_input(graph):
    heuristic={}
    for node in graph:
        val=int(input("Enter the value of the heuristic node:"))
        heuristic[node]=val
    return heuristic

def main():
    graph=input_graph()
    heuristic=heuristic_input(graph)
    start_node=input("Enter the start node:")
    goal_node=input("Enter the goal node:")
    greedy_best_first_search(graph,start_node,goal_node,heuristic)