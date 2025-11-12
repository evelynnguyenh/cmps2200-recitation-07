from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):

    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        node = frontier.pop()
        result.add(node)
    frontier.update(graph[node] - result)
    return result





def connected(graph):
    nodes = set(graph.keys())
    start_node = next(iter(nodes))
    return reachable(graph, start_node) == nodes




def n_components(graph):
    nodes = set(graph.keys())
    visited = set()
    count = 0

    for node in nodes:
        if node not in visited:
            component = reachable(graph, node)
            visited.update(component)
            count += 1
    return count

