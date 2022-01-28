def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost <lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

graph = {}
graph["start"] = {}
graph["start"]["A"] = 6
graph["start"]["B"] = 2
#print(graph)
graph["A"] = {}
graph["A"]["meta"] = 1
#print(graph)
graph["B"] = {}
graph["B"]["A"] = 3
graph["B"]["meta"] = 5
graph["meta"] = {}
print("graph: ", graph)

infinity = float("inf")
costs = {}
costs["A"] = 6
costs["B"] = 2
costs["meta"] = infinity
print("costs: ", costs)

parents = {}
parents["A"] = "start"
parents["B"] = "start"
parents["meta"] = None
print("parents: ", parents)

processed = []

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(processed)