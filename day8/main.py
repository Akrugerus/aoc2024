class Runner:
    def __init__(self, data):
        self.data = data.splitlines()
        assert len(self.data) == len(self.data[0])
        self.nodes = {}
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                ch = self.data[i][j]
                if ch != ".":
                    l = self.nodes.get(ch, [])
                    l.append((i, j))
                    self.nodes[ch] = l

    def find_antinodes(self, i, j):
        x = j[0] - i[0]
        y = j[1] - i[1]
        print(f"{i} {j} has distance {x} {y}")
        n1 = i[0] - x, i[1] - y
        n2 = j[0] + x, j[1] + y
        print(f"{i} {j} has antinodes {n1} {n2}")
        if self.valid_and_in_bounds(n1):
            self.antinodes[n1] = True
        if self.valid_and_in_bounds(n2):
            self.antinodes[n2] = True

    def find_resonant_antinodes(self, i, j):
        self.antinodes[i] = True
        self.antinodes[j] = True
        x, y = j[0] - i[0], j[1] - i[1]
        print(f"{i} {j} has distance {x} {y}")
        n1 = i[0] - x, i[1] - y
        n2 = j[0] + x, j[1] + y
        while self.valid_and_in_bounds(n1):
            self.antinodes[n1] = True
            n1 = n1[0] - x, n1[1] - y
        while self.valid_and_in_bounds(n2):
            self.antinodes[n2] = True
            n2 = n2[0] + x, n2[1] + y

    def valid_and_in_bounds(self, node):
        print(f"checking {node}")
        if 0 <= node[0] < len(self.data) and 0 <= node[1] < len(self.data):
            return True

    def num_antinodes(self):
        # Calculate antinodes
        self.antinodes = {}
        # For each pair of nodes, find the distance vector and subtract it from node 1
        # and add it to node 2 to find the antinodes
        for node_ch in self.nodes:
            print(f"{len(self.nodes[node_ch])} points containing {node_ch}")
            for i in range(len(self.nodes[node_ch]) - 1):
                for j in range(i + 1, len(self.nodes[node_ch])):
                    # i, j is a pair of matching nodes
                    self.find_antinodes(self.nodes[node_ch][i], self.nodes[node_ch][j])

        print(self.antinodes)
        return len(self.antinodes)

    def num_resonant_antinodes(self):
        # Calculate antinodes
        self.antinodes = {}
        # For each pair of nodes, find the distance vector and subtract it from node 1
        # and add it to node 2 to find the antinodes
        for node_ch in self.nodes:
            print(f"{len(self.nodes[node_ch])} points containing {node_ch}")
            for i in range(len(self.nodes[node_ch]) - 1):
                for j in range(i + 1, len(self.nodes[node_ch])):
                    one, two = self.nodes[node_ch][i], self.nodes[node_ch][j]
                    # i, j is a pair of matching nodes
                    self.find_resonant_antinodes(one, two)

        return len(self.antinodes)


if __name__ == "__main__":
    with open("day8/sample.txt") as file:
        runner = Runner(file.read())
        assert runner.num_antinodes() == 14
        assert runner.num_resonant_antinodes() == 34

    with open("day8/input.txt") as file:
        runner = Runner(file.read())
        print(runner.num_antinodes())
        print(runner.num_resonant_antinodes())
