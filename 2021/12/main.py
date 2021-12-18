# %%
import copy
from collections import defaultdict
# %%
with open('input.txt', 'r') as f:
    data = f.read()
data = [line.split("-") for line in data.split('\n')]
# %%
with open('test_input.txt', 'r') as f:
    test_data = f.read()
test_data = [line.split("-") for line in test_data.split('\n')]

with open('test_input_2.txt', 'r') as f:
    test_data2 = f.read()
test_data2 = [line.split("-") for line in test_data2.split('\n')]

with open('test_input_3.txt', 'r') as f:
    test_data3 = f.read()
test_data3 = [line.split("-") for line in test_data3.split('\n')]

# %%

class Node:
    def __init__(self, name):
        self.name = name
        self.large = name.isupper()
        self.paths = []
        self.start_or_end = True if name in ["start", "end"] else False
    
    def add_path(self, node):
        self.paths.append(node)
    
    def __repr__(self):
        return self.name
    
    def __lt__(self, other):
        return (self.name < other)

    def __le__(self, other):
        return (self.name <= other)

    def __gt__(self, other):
        return (self.name > other)

    def __ge__(self, other):
        return (self.name >= other)

    def __eq__(self, other):
        return (self.name == other)

    def __ne__(self, other):
        return not(self.__eq__(self, other))
        
# %%
def create_graph(data):
    nodes = {}

    for node1, node2 in data:
        if node1 not in nodes:
            nodes[node1] = Node(node1)
        if node2 not in nodes:
            nodes[node2] = Node(node2)

        nodes[node1].add_path(nodes[node2])
        nodes[node2].add_path(nodes[node1])
    
    return nodes
# %%
def find_paths(current_node, end_node, path):
    paths = []
    path.append(current_node.name)

    if current_node == end_node:
        return path
    
    for node in current_node.paths:
        if node.name not in path or node.large:
            new_path = find_paths(node, end_node, copy.deepcopy(path))
            if new_path:
                if isinstance(new_path[0], list):
                    for viable_path in new_path:
                        paths.append(viable_path)
                else:
                    paths.append(new_path)
    
    return paths

# %%
test_graph = create_graph(test_data)
paths = find_paths(test_graph["start"], test_graph["end"], [])
assert len(paths) == 10, "Incorrect number of paths: " + str(len(paths))
# %%
test_graph2 = create_graph(test_data2)
paths = find_paths(test_graph2["start"], test_graph2["end"], [])
assert len(paths) == 19, "Incorrect number of paths: " + str(len(paths))
# %%
test_graph3 = create_graph(test_data3)
paths = find_paths(test_graph3["start"], test_graph3["end"], [])
assert len(paths) == 226, "Incorrect number of paths: " + str(len(paths))
# %%
graph = create_graph(data)
paths = find_paths(graph["start"], graph["end"], [])
len(paths)

# %%
def rule_violated(path):
    visits = defaultdict(int)
    small_caves = set()

    for node in path:
        visits[node.name] += 1
        if not node.large:
            small_caves.add(node.name)
    
    small_2_visit = False

    for node in small_caves:
        if visits[node] > 2:
            return True, small_2_visit
        if visits[node] > 1:
            if small_2_visit:
                return True, small_2_visit
            small_2_visit = True
            
    return False, small_2_visit

# %%

DYN_NODES = {}

def find_paths2(current_node, end_node, path):
    path.append(current_node)
    
    if current_node == end_node:
        return path

    violation, triggered = rule_violated(path)
    
    if violation:
        return []
    
    # key = (current_node, triggered)
    sorted_path = ",".join(sorted([node.name for node in path[:-1]]))
    key = (sorted_path, current_node.name)

    # Use cached result
    if key in DYN_NODES:
        paths = DYN_NODES[key]
        paths = [path + node for node in paths if not rule_violated(path + node)[0]]
        return paths

    paths = []
    
    for node in current_node.paths:
        if node.name == "start":
            continue
        new_path = find_paths2(node, end_node, copy.deepcopy(path))

        if new_path:
            if isinstance(new_path[0], list):
                for viable_path in new_path:
                    paths.append(viable_path)
            else:
                paths.append(new_path)
            
            
    # Chache result
    DYN_NODES[key] = [node_path[len(path):] for node_path in paths]

    return paths

graph = create_graph(data)
paths = find_paths2(graph["start"], graph["end"], [])
len(paths)

# %%
DYN_NODES = {}
test_graph = create_graph(test_data)
paths = find_paths2(test_graph["start"], test_graph["end"], [])
assert len(paths) == 36, "Incorrect number of paths: " + str(len(paths))
# %%
DYN_NODES = {}
test_graph2 = create_graph(test_data2)
paths = find_paths2(test_graph2["start"], test_graph2["end"], [])
assert len(paths) == 103, "Incorrect number of paths: " + str(len(paths))
# %%
DYN_NODES = {}
test_graph3 = create_graph(test_data3)
paths = find_paths2(test_graph3["start"], test_graph3["end"], [])
assert len(paths) == 3509, "Incorrect number of paths: " + str(len(paths))
# %%
DYN_NODES = {}
graph = create_graph(data)
paths = find_paths2(graph["start"], graph["end"], [])
len(paths)

# %%
paths
# %%
