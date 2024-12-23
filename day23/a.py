from tqdm import tqdm

graph = set()
nodes = set()
for line in open('day23/input.txt', 'r').readlines():
    edge = line.strip().split('-')
    nodes.add(edge[0])
    nodes.add(edge[1])
    graph.add((edge[0], edge[1]))
    graph.add((edge[1], edge[0]))

nodes = sorted(list(nodes))
triple = set()

for idx, n1 in enumerate(nodes):
    for jdx, n2 in enumerate(nodes[idx+1:]):
        for n3 in nodes[idx+jdx+2:]:
            if (n1,n2) in graph and (n2,n3) in graph and (n1,n3) in graph:
                triple.add((n1,n2,n3))

t_connections = 0
for triple in triple:
    n1, n2, n3 = triple
    if n1.startswith('t') or n2.startswith('t') or n3.startswith('t'):
        t_connections += 1
print(t_connections)
