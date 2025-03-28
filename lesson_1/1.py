from itertools import permutations


def str_to_int(s: str) -> int:
    return ord(s)-ord('a')+1 # 1-индексация

class Graph:
    def __init__(self, edges: dict[int, list[int]] | dict[str, list[str]]):
        self.n = len(edges)
        type_of_keys = set(type(key) for key in edges.keys())
        if type_of_keys == {int,}: # если пришел словарь с числами, то просто его копируем
            self.edges = edges
        elif type_of_keys == {str,}: # а если пришли буквы, то их надо преобразовать
            self.edges = dict()
            for key in edges.keys():
                self.edges[str_to_int(key)] = [str_to_int(to) for to in edges[key]]
        else:
            print("такое не умеем")




# O(n!) check
def check(graph1:Graph, graph2: Graph):
    if graph1.n != graph2.n:
        return

    for perm in permutations(graph2.edges.keys()):
        # перемешиваем вершины второго графа, то есть сейчас i-ая вершина 1-ого графа становится с номером perm[v]
        good_perm = True
        for fr in graph1.edges:
            for to in graph1.edges[fr]: # двумя for смотрим все ребра в первом графе
                new_fr = perm[fr-1] # кем становится вершина fr (-1 потому что в 1-индексации вводим)
                new_to = perm[to-1] # кем становится вершина to

                flag = new_to in graph2.edges[new_fr] # (new_fr, new_to) in graph2?

                if not flag:
                    good_perm = False
                    break
            if not good_perm:
                break
        if good_perm:
            print(*[chr(ord('a') + perm[i]-1) for i in range(len(perm))])


first_edges = {
    1:[4,5,6,8],
    2:[3,4,5,6,7,9],
    3:[2,5],
    4:[1,2,6,7,9],
    5:[1,2,3,6,9],
    6:[1,2,4,5,8],
    7:[2,4],
    8:[1,6],
    9:[2,4,5],
}

second_edges = {
    'm' : ['n', 'r'],
    'n' : ['m', 'p', 'r', 's', 't', 'v'],
    'r' : ['m', 'n', 'p', 'k', 'v'],
    'p' : ['s', 'n', 'r'],
    's' : ['n', 't', 'p', 'k', 'v'],
    't' : ['s', 'n'],
    'k' : ['s', 'r', 'l', 'v'],
    'l' : ['k', 'v'],
    'v' : ['k', 'n', 'r', 'l', 's'],
}

check(Graph(first_edges), Graph(second_edges))