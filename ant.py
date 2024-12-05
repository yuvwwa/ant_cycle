import random
from math import inf

class Ant:
    def __init__(self, graph, imp_pheromones, length_way, lower_rate, pheromone_boost, count_ants):
        self.graph = graph
        self.pheromones = self.func_pheromones() #Функция феромоны
        self.imp_pheromones = imp_pheromones 
        self.length_way = length_way
        self.lower_rate = lower_rate
        self.pheromone_boost = pheromone_boost
        self.count_ants = count_ants
        self.min_length = inf
        self.best_path = []

    #Функция для феромонов, в которой мы создаем словарь, где ключи - вершины, а значения это начальное значение феромонов
    def func_pheromones(self):
        pheromones = {}
        for node in self.graph.list:
            pheromones[node]={}
            for edge in self.graph.get_neighbors(node):
                pheromones[node][edge.node] = 1.0
        return pheromones
    
    #Функция для выбора следующей вершины
    def choose_next_node(self, current_node, visited):
        neighbors = self.graph.get_neighbors(current_node)
        probability = []

        for edge in neighbors:
            #Если вершина не посещена, то мы вычисляем у какой следующей вершины приоритет важнее 
            # по феромонам и эвристике (чем меньше длина пути, чем она выше)
            # а также length_way определяет насколько важна длина пути в сравнении с феромонами
            if edge.node not in visited:
                pheromone = self.pheromones[current_node][edge.node] **self.imp_pheromones #Возведение в степень помогает нам нам понять, насколько важен этот путь
                heuristis = (1.0/edge.weight) **self.length_way
                probability.append((edge.node, pheromone * heuristis))
            
        if not probability: 
            return None
            
        total = sum(prob[1] for prob in probability) # Находим общую вероятность
        probability = [(node, prob/total) for node, prob in probability] #Нормализуем вероятность: хотим получить 1

        r = random.random()
        res = 0
            
        for node, prob in probability:
            res+=prob
            if r <= res:
                return node
    
    #испаряем феромоны
    def lower_pheromones(self):
        for node in self.pheromones:
            for neighbor in self.pheromones[node]:
                self.pheromones[node][neighbor] *= (1 - self.lower_rate)

    #Обновление феромонов
    def updates_pheromones(self, path, path_length):
        for i in range (len(path) -1):
            from_node = path[i]
            to_node = path[i+1]
            self.pheromones[from_node][to_node] += self.pheromone_boost / path_length

    #получаем вес с соседями вершины
    def edge_weight(self, from_node, to_node):
        neighbors = self.graph.get_neighbors(from_node)
        for edge in neighbors:
            if edge.node == to_node:
                return edge.weight
        return inf

    #получаем общую длину пути
    def total_path_length(self, path):
        total = 0
        for i in range(len(path)- 1):
            from_node = path[i]
            to_node = path[i+1]
            weight = self.edge_weight(from_node, to_node)
            if weight == inf:
                return inf
            total += weight
        return total

    def run(self, start_node, iterations):
        path_lengths = []
        for _ in range(iterations):
            for _ in range(self.count_ants):
                #назначаем все нужные переменные(путьб посещенные вершины, текущая вершина)
                path = [start_node]
                visited = {start_node}
                current_node = start_node

                #Посещыем все вершины графа, используя функцию choose_next_node, если следующей вершины нет, то там проход дальше невозможен, либо тупик. Обновляем переменные
                while len(visited) < len(self.graph.list):
                    next_node = self.choose_next_node(current_node, visited)
                    if next_node is None:
                        break
                    path.append(next_node)
                    visited.add(next_node)
                    current_node = next_node

                if len(path) == len(self.graph.list):
                    path_length = self.total_path_length(path)
                    if path_length < self.min_length:
                        self.min_length = path_length
                        self.best_path = path
                    self.updates_pheromones(path, path_length)
            self.lower_pheromones()
            path_lengths.append(self.min_length)

        plt.plot(range(iterations), path_lengths)
        plt.xlabel('Итерация')
        plt.ylabel("Длина пути")
        plt.title("Зависимость длины пути от итерации")
        plt.grid(True)
        plt.show()

        print ("Кратчайший путь: ", " ".join(str(node) for node in self.best_path))
        print ("Длина пути: ", self.min_length)
