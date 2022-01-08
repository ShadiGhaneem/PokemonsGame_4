from DWGraph import DWGraph
# this class we implement to help us to find each pokemon edge position by linear equation

class Calc_Pos:
    def __init__(self, edge, Graph):
        self.edges = edge
        self.graph = Graph
        self.fun = {}
        self.init_fun()

    def init_fun(self):
        edges = self.graph.get_all_edges()
        for e in edges:
            src_x = self.graph.getNode(e.src.key).pos[0]
            src_y = self.graph.getNode(e.src.key).pos[1]
            dest_x = self.graph.getNode(e.dest.key).pos[0]
            dest_y = self.graph.getNode(e.dest.key).pos[1]
            a = dest_y - src_y
            b = src_x - dest_x
            c = a * src_x + b * src_y
            m =[]
            m.append(a)
            m.append(b)
            m.append(c)
            self.fun[e] = m

    def get_line(self, pok):
        x = pok.pos.x
        y = pok.pos.y
        eps = 0.0000001
        for e in self.fun.keys():
            m = self.fun[e]
            if m[0] * x + m[1] * y <= m[2]+eps and m[0] * x + m[1] * y >= m[2]-eps:
                return e


    # def get_dist(self , p1 ,p2):
    #     x1=p1[0]
    #     y1=p1[0]
    #     x2=p2.x
    #     y2=p2.y
    #     w = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
    #     return w
    #
    #
    # def find_line(self , pok):
    #     eps = 0.0000001
    #     for e in self.fun.keys():
    #        e_w= ((((e.src.pos[0] - e.dest.pos[0]) ** 2) + ((e.src.pos[1] - e.dest.pos[1]) ** 2)) ** 0.5)
    #        # print(e.src.pos , e.dest.pos ,pok.pos)
    #        if self.get_dist(e.src.pos , pok.pos) + self.get_dist(e.dest.pos , pok.pos) <= e.weight+eps and self.get_dist(e.src.pos , pok.pos) + self.get_dist(e.dest.pos , pok.pos) >= e.weight-eps:
    #            return e