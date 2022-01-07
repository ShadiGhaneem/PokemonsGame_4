from DWGraph import DWGraph


class Calc_Pos:
    def __init__(self, edge, Graph):
        self.edges = edge
        self.graph = Graph
        self.fun = {}
        self.init_fun()

    def init_fun(self):
        edges = self.graph.get_all_edges()
        for e in edges:
            src_x = self.graph.getNode(e.src).pos[0]
            src_y = self.graph.getNode(e.src).pos[1]
            dest_x = self.graph.getNode(e.dest).pos[0]
            dest_y = self.graph.getNode(e.dest).pos[1]
            a = dest_y - src_y
            b = src_x - dest_x
            c = a * src_x + b * src_y
            m = []
            m.append(a)
            m.append(b)
            m.append(c)
            self.fun[e] = m

    def get_line(self, pok):
        x = pok.pos.x
        y = pok.pos.y
        for e in self.fun.keys():
            m = self.fun[e]
            if m[0] * x + m[1] * y == m[2]:
                return e
        return None
