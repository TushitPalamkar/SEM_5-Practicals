import math
from collections import Counter


class Node:
    def __init__(self, attribute=None, value=None, results=None, branches=None):
        self.attribute = attribute
        self.value = value
        self.results = results
        self.branches = branches or {}


def entropy(data):
    counts = Counter(row[-1] for row in data)
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in counts.values() if count > 0)


def information_gain(data, attribute_index):
    base_entropy = entropy(data)
    weighted_entropy = 0
    for value in set(row[attribute_index] for row in data):
        subset = [row for row in data if row[attribute_index] == value]
        weighted_entropy += len(subset) / len(data) * entropy(subset)
    return base_entropy - weighted_entropy


def id3(data, attributes):
    if len(set(row[-1] for row in data)) == 1:
        return Node(results=data[0][-1])
   
    if not attributes:
        return Node(results=Counter(row[-1] for row in data).most_common(1)[0][0])
   
    best_attribute_index = max(range(len(attributes)), key=lambda i: information_gain(data, i))
    best_attribute = attributes[best_attribute_index]
   
    tree = Node(attribute=best_attribute)
    remaining_attributes = attributes[:best_attribute_index] + attributes[best_attribute_index+1:]
   
    for value in set(row[best_attribute_index] for row in data):
        subset = [row for row in data if row[best_attribute_index] == value]
        subtree = id3(subset, remaining_attributes)
        tree.branches[value] = subtree
   
    return tree


def print_tree(node, indent=""):
    if node.results is not None:
        print(f"{indent}{target_attribute}: {node.results}")
    else:
        print(f"{indent}{node.attribute}:")
        for value, branch in node.branches.items():
            print(f"{indent}  {value}:")
            print_tree(branch, indent + "    ")


def classify(tree, instance):
    if tree.results is not None:
        return tree.results
    value = instance[tree.attribute]
    if value not in tree.branches:
        return None
    return classify(tree.branches[value], instance)


# Get user input for dataset structure
num_attributes = int(input("Enter the number of attributes: "))
attributes = [input(f"Enter name of attribute {i+1}: ") for i in range(num_attributes)]
target_attribute = input("Enter the name of the target attribute: ")
attributes.append(target_attribute)


num_rows = int(input("Enter the number of rows in the dataset: "))


# Get user input for dataset
print(f"Enter {num_rows} rows of data, with values separated by spaces:")
data = []
for _ in range(num_rows):
    row = input().strip().split()
    if len(row) != len(attributes):
        print(f"Error: Expected {len(attributes)} values, but got {len(row)}. Please try again.")
        row = input().strip().split()
    data.append(row)


# Build the decision tree
tree = id3(data, attributes[:-1])


# Print the decision tree
print("\nDecision Tree:")
print_tree(tree)
