from queue import PriorityQueue, Queue
from functools import total_ordering

#Class to represent a node
@total_ordering
class Node:

    def createTimeToWork(self, uuid):
        return self.stage_time + ord(uuid) - ord('A') + 1

    def addDependent(self, dependent):
        self.edges.add(dependent)
        dependent.unfulfilled_dependencies += 1

    def hasNoDependencies(self):
        return self.unfulfilled_dependencies <= 0

    # Precondition, uuid is only one character
    def __hash__(self):
        return ord(self.uuid)

    def __eq__(self, other):
        return self.uuid == other.uuid

    def __lt__(self, other):
        return self.uuid < other.uuid

    def __repr__(self):
        return f"{self.uuid} {self.time_left}"

    def __init__(self, uuid):
        self.uuid = uuid
        self.edges = set() # Edges are directed
        self.unfulfilled_dependencies = 0
        self.stage_time = 60
        self.time_left = self.createTimeToWork(self.uuid)


#Class to represent a graph
class Graph:

    def __init__(self, elves):
        self.graph = {} #dictionary mapping uuid to nodes
        self.worker_limit = elves + 1;

    # function to add an edge to graph
    def addEdge(self,u,v):
        if u not in self.graph:
            self.graph[u] = Node(u)

        if v not in self.graph:
            self.graph[v] = Node(v)

        self.graph[u].addDependent(self.graph[v])


    def getRootNodes(self):
        return set([v for k, v in self.graph.items() if v.hasNoDependencies()])

    # The function to do Topological Sort.
    def topologicalSort(self):
        # Over here, PQ should sort nodes by lexicographical ordering of uuid
        pq = PriorityQueue(0)
        worker_list = []

        for n in self.getRootNodes():
            pq.put(n)

        result = ""
        time_working = 0
        while not pq.empty() or not len(worker_list) == 0:

            while not pq.empty() and not len(worker_list) >= self.worker_limit:
                worker_list.append(pq.get())

            worker_list.sort(key= lambda node : node.time_left)
            time_to_work = worker_list[0].time_left
            time_working += time_to_work
            # creates a shallow copy of worker_list so there's no concurrent r/w issues
            for node in worker_list.copy():
                # work on all nodes in the worker queue
                node.time_left -= time_to_work

                if (node.time_left <= 0):
                    result += node.uuid
                    # add all finished nodes into the pq
                    for dependent in node.edges:
                        dependent.unfulfilled_dependencies -= 1
                        if dependent.hasNoDependencies():
                            pq.put(dependent)
                    worker_list.remove(node)


        print(result)
        print(time_working)

def parser(l):
    ll = l.split()
    return (ll[1], ll[7])

def main():
    filename = "input.txt"
    file = open(filename, "r")
    raw = file.readlines()
    parsed = [parser(l) for l in raw]

    g = Graph(4)

    for from_vertex, to_vertex in parsed:
        g.addEdge(from_vertex, to_vertex)


    g.topologicalSort()


if __name__ == "__main__":
    main()
