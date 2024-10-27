import heapq

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, u, v, weight):
        if u not in self.nodes:
            self.nodes[u] = []
        if v not in self.nodes:
            self.nodes[v] = []

        self.nodes[u].append((v,weight))
        self.nodes[v].append((u,weight))

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0

    min_heap = [(0, start)]
    visited = set()

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph.nodes[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

graph = Graph()
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 10)
graph.add_edge('C', 'D', 3)
graph.add_edge('D', 'E', 4)

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(f"Найкоротші шляхи від вершини {start_node}: {shortest_paths}")