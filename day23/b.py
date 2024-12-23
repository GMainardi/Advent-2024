import itertools

def is_click(nodes):
    for idx, n1 in enumerate(nodes):
        for n2 in nodes[idx+1:]:
            if n2 not in graph[n1]:
                return False
    return True

def add_nodes(graph, cliques):
    new_cliques = set()
    for clique in cliques:
        for node in graph.keys():
            if node not in clique:
                seq = sorted(list(clique) + [node])
                new_cliques.add(tuple(seq))
    return new_cliques

def find_max_cliques(graph):

    cliques = set(map(lambda x: tuple([x]), graph.keys()))
    
    while len(cliques) > 1:
        cliques = add_nodes(graph, cliques)
        cliques = set(filter(is_click, cliques))

    return list(cliques)

graph = {}
for line in open('day23/input.txt', 'r').readlines():
    edge = line.strip().split('-')
    graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
    graph[edge[1]] = graph.get(edge[1], []) + [edge[0]]

cliques = find_max_cliques(graph)
print(len(cliques[0]))
password = ','.join(sorted(cliques[-1]))
print(password)

