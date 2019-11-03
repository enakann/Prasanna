from queue import Queue

class Vertex:
    def __init__(self,data):
        self.data=data
        self.visited=False
        self.neighbours=[]

    def add_neighbour(self,vertex):
        self.neighbours.append(vertex)

    def get_neigbours(self):
        return self.neighbours

    def is_visited(self):
        return self.visited

    def set_visited(self):
        self.visited=True

    def __repr__(self):
        return str(self.data)

class DFS:
    def __init__(self,root):
        self.root=root
        self.ls=[]
        #self.root.set_visited()
        self.ls.append(self.root)

    def get_vertices(self):
        while self.ls:
            vertex=self.ls.pop()
            print(vertex)

            for v in vertex.get_neigbours()[::-1]:
                if not v.is_visited():
                    v.set_visited()
                    self.ls.append(v)

    def get_vertices_recursive(self,node):
        if not node.visited:
            node.visited=True
            print(node)

            for vertex in node.get_neigbours():
                self.get_vertices_recursive(vertex)


class BFS:
    def __init__(self,root):
        self.q=Queue()
        self.root=root
        self.root.set_visited()
        self.q.put(root)

    def get_vertices(self):
        while not self.q.empty():
            vertex=self.q.get()
            print(str(vertex) + '-',end='')

            for v in vertex.get_neigbours():
                if not v.is_visited():
                    v.set_visited()
                    self.q.put(v)


def main():
    a=Vertex('A');b=Vertex('B');c=Vertex('C');d=Vertex('D');e=Vertex('E')


    a.add_neighbour(b)
    a.add_neighbour(c)
    b.add_neighbour(d)
    d.add_neighbour(e)

    dfs=DFS(a)
    print("using stack")
    #dfs.get_vertices()
    print("Using recursion")
    dfs.get_vertices_recursive(a)

def main2():
    v1=Vertex(1)
    v2=Vertex(2)
    v3=Vertex(3)
    v4=Vertex(4)
    v5=Vertex(5)



    v1.add_neighbour(v2)
    v1.add_neighbour(v4)
    v4.add_neighbour(v5)
    v2.add_neighbour(v3)

    bfs=DFS(v1)

    bfs.get_vertices()

if __name__ == '__main__':
    main()
