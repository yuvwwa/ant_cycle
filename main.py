from graph import Graph
from ant import Ant

graph = Graph()

graph.add_edge('a', 'b', 3)
graph.add_edge('a', 'f', 1)
graph.add_edge('b', 'a', 3)
graph.add_edge('b', 'g', 3)
graph.add_edge('b', 'c', 8)
graph.add_edge('c', 'g', 1)
graph.add_edge('c', 'd', 1)
graph.add_edge('c', 'b', 3)
graph.add_edge('d', 'f', 1)
graph.add_edge('d', 'c', 8)
graph.add_edge('g', 'a', 3)
graph.add_edge('g', 'f', 4)
graph.add_edge('g', 'd', 5)
graph.add_edge('g', 'b', 3)
graph.add_edge('g', 'c', 3)
graph.add_edge('f', 'a', 3)
graph.add_edge('f', 'd', 3)

result = Ant(graph, imp_pheromones = 1, length_way = 2, lower_rate = 0.5, pheromone_boost = 100, count_ants = 10)
result.run(start_node = "a", iterations = 100)
