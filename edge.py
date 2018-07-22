class edge:
    def __init__(self, from_node:str, to_node:str, cost:int):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

    def __repr__(self):
        return self.from_node+":"+self.to_node+"("+str(self.cost)+")"
    def __str__(self):
        return "{}-{}->{}".format(self.from_node, self.to_node, self.cost)
