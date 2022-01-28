from collections import deque


def search(name):
    search_graph = deque()
    search_graph += graph[name]
    searched = []
    while len(search_graph) > 0:
        person = search_graph.popleft()
        if person not in searched:
            if is_seller(person):
                print(person + " sprzedaje mango!")
                return True
            else:
                if graph.get(person):
                    search_graph += graph[person]
                searched.append(person)
    return False


def is_seller(name):
    return name[-1] == "m"


graph = {}
graph["ty"] = ["bartek", "jola"]
graph["bartek"] = ["zosia", "patrycja"]
graph["zosia"] = ["patrycjam", "gosia"]
search("ty")