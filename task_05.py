import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.id = str(uuid.uuid4())
        self.left = None  
        self.right = None

def build_tree():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(18)
    return root

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree, pos, colors, labels):
    plt.figure(figsize=(10,6))
    nx.draw(tree, pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.pause(1)

def color_generator(num_steps):
    cmap = mcolors.LinearSegmentedColormap.from_list("", ["#001f3f", "#7FDBFF"])
    color_steps = [mcolors.to_hex(cmap(i / (num_steps - 1))) for i in range(num_steps)]
    return color_steps

def visualize_traversal (root, traversal_type='DFS'):
    graph = nx.DiGraph()
    pos = {root.id: (0,0)}
    add_edges(graph, root, pos)

    labels = {node[0]: node[1]['label'] for node in graph.nodes(data=True)}

    traversal = []
    if traversal_type == 'DFS':
        stack = [root]
        while stack:
            node = stack.pop()
            traversal.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    elif traversal_type == "BFS":
        queue = deque([root])
        while queue:
            node = queue.popleft()
            traversal.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    color_steps = color_generator(len(traversal))
    for i, node in enumerate(traversal):
        colors = ["#DDDDDD"] * len(graph.nodes())  
        node_colors = {node.id: color_steps[i] for i, node in enumerate(traversal)}
        colors = [node_colors.get(n, "#DDDDDD") for n in graph.nodes()]
        labels = {n: graph.nodes[n]['label'] for n in graph.nodes()}

        draw_tree(graph, pos, colors, labels)

root = build_tree()
print("Візуалізація обходу в глибину (DFS):")
visualize_traversal(root, traversal_type="DFS")

print("Візуалізація обходу в ширину (BFS):")
visualize_traversal(root, traversal_type="BFS")