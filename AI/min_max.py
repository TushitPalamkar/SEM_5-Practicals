def min_max(depth,node_index,is_maximizing,scores,height):
    if depth==height:
        return scores[node_index]
    if is_maximizing:
        return max(min_max(depth+1,node_index*2,False,scores,height),min_max(depth+1,node_index*2+1,False,scores,height))
    else:
        return min(min_max(depth+1,node_index*2+1,True,scores,height),min_max(depth+1,node_index,True,scores,height))
    
scores=list(map(int,input("Enter the scores:(space-seperated):").split()))
tree_height=int(input("Enter the tree height:"))
result=min_max(0,0,True,scores,tree_height)
print(f"Result:{result}")