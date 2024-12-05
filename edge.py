#Класс для создания ребра, у которого есть вес и вершина

class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight
