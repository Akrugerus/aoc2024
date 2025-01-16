from collections import deque


class Runner:
    def __init__(self, data):
        self.data = data

    def group_areas(self):
        total = 0

        self.visited = {}

        for idx in range(len(self.data)):
            for jdx in range(len(self.data[0])):
                node = idx, jdx
                if node in self.visited:
                    continue

                total += self.find_group(node)
        print(total)
        return total

    def get_val(self, node):
        return self.data[node[0]][node[1]]

    def search_node(self, node):
        new_nodes = []
        if node[0] > 0:
            new_nodes.append((node[0] - 1, node[1]))
        if node[0] < len(self.data) - 1:
            new_nodes.append((node[0] + 1, node[1]))
        if node[1] > 0:
            new_nodes.append((node[0], node[1] - 1))
        if node[1] < len(self.data[0]) - 1:
            new_nodes.append((node[0], node[1] + 1))
        return new_nodes

    def find_group(self, node):
        q = deque()
        q.append(node)
        group_ch = self.get_val(node)

        edges = 0
        nodes = 0
        while len(q) != 0:
            node = q.pop()
            if node in self.visited:
                continue
            nodes += 1
            self.visited[node] = True
            # print(f"found {node}")
            new_nodes = self.search_node(node)
            edges += 4 - len(new_nodes)
            for n in new_nodes:
                if self.get_val(n) != group_ch:
                    edges += 1
                    continue
                q.append(n)

        print(f"{group_ch} is {nodes} {edges}")
        return nodes * edges


if __name__ == "__main__":
    with open("day12/sample.txt") as file:
        runner = Runner(file.read().splitlines())
        assert runner.group_areas() == 1930

    with open("day12/input.txt") as file:
        runner = Runner(file.read().splitlines())
        print(runner.group_areas())
