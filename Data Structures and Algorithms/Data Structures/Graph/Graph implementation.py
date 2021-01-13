class Graph:
    def __init__(self,routes,sp):
        self.routes=routes
        self.flight_routes={}
        for start, end in self.routes:
            if start in self.flight_routes:
                self.flight_routes[start].append(end)
            else:
                self.flight_routes[start]=[end]
        print(self.flight_routes)

    def get_paths(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.flight_routes:
            return []
        paths=[]
        for node in self.flight_routes[start]:
            if node not in path:
                new_path=self.get_paths(node,end,path)
                for p in new_path:
                    paths.append(p)
        return paths

    def path_distance(self,routes_with_distance):
        self.route_dist={}
        for start,end,distance in routes_with_distance:
            if start not in self.route_dist:
                self.route_dist[start]=[(end,distance)]
            else:
                self.route_dist[start].append((end,distance))
        print(self.route_dist)

flight_routes=[("Mumbai","Boston"),
                        ("Mumbai","Paris"),
                        ("Mumbai","Dubai"),
                        ("Paris","New York"),
                        ("Paris","Dubai"),
                        ("Dubai","New York"),
                        ("New York","Toronto"),
                        ("Boston","Hartford"),
                        ("Hartford","New York")]

flight_routes_dist=[("Mumbai","Boston",5000),
                        ("Mumbai","Paris",4000),
                        ("Mumbai","Dubai",500),
                        ("Paris","New York",3000),
                        ("Paris","Dubai",2000),
                        ("Dubai","New York",6000),
                        ("New York","Toronto",400),
                        ("Boston","Hartford",200),
                        ("Hartford","New York",100)]

graph=Graph(flight_routes,flight_routes_dist)
print()
print(graph.get_paths("Mumbai","New York"))
print()
graph.path_distance(flight_routes_dist)


