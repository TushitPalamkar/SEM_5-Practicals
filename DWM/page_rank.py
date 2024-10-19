def page_rank(graph,max_iterations,damping_factor=0.85):
    num_pages=len(graph)
    pr={page:1/num_pages for page in graph}
    for _ in range(max_iterations):
        new_pr={}
        for page in graph:
            incoming_pr=sum(pr[i]/len(graph[i]) for i in graph if page in graph[i])
            new_pr[page]=(1-damping_factor)*damping_factor+incoming_pr
        pr=new_pr
    for page,rank in pr.items():
        print(f"{page}:{rank}")
    return pr

def get_graph_input():
    graph={}
    while True:
        page=input("Enter the page:")
        if not page:
            break
        links=input(f"Enter the links associated with {page}:").split(',')
        graph[page]=[link.strip() for link in links if link.strip()]
    return graph
print("Enter the graph structure:")
graph=get_graph_input()
iter=int(input("Iterations:"))
result=page_rank(graph,iter)
for page,rank in result.items():
    print(f"{page}:{rank}")

