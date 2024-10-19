# def hill_climb(objective_function,solution):
#     current_solution=solution
#     current_value=objective_function(current_solution)

#     while True:
#         neighbours=generate_neighbours(current_solution)
#         best_neighbour=None
#         best_value=current_value
#         for neighbour in neighbours:
#             neighbour_value=objective_function(neighbour)
#             if neighbour_value>best_value:
#                 best_value=neighbour_value
#                 best_neighbour=neighbour
#         if best_neighbour is None:
#             break
#         current_solution=best_neighbour
#         current_value=best_value
    
    # return current_solution,current_value
def hill_climb(objective_function,solution):
    current_solution=solution
    current_value=objective_function(current_solution)
    print(f"Initial Solution:{current_solution} | Initial Value:{current_value}")
    while True:
        neighbours=generate_neighbours(current_solution)
       
        best_neighbour=None
        best_value=current_value
        for neighbour in neighbours:
            neighbour_value=objective_function(neighbour)
            if neighbour_value>best_value:
                best_value=neighbour_value
                best_neighbour=neighbour
        if best_neighbour is None:
            break
        current_solution=best_neighbour
        current_value=best_value
        
        
    return current_solution,current_value
def generate_neighbours(solution):
    return [solution+1,solution-1]
def objective_function(x):
    return -x**2+10*x+5
initial_solution = int(input('Enter an initial solution (integer): '))
result, value = hill_climb(objective_function, initial_solution)

print(f'Optimal solution: {result}, Objective value: {value}')