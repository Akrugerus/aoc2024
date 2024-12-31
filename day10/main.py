from collections import deque


def add_node(one, two):
    return one[0] + two[0], one[1] + two[1]


class Runner:
    def __init__(self, data):
        self.data = data
        print(self.data)

    def trailhead_score(self):
        total = 0
        for idx in range(len(self.data)):
            for jdx in range(len(self.data[idx])):
                node = idx, jdx
                if self.fetch_value(node) == 0:
                    total += self.find_trails(node)
        return total

    def fetch_value(self, node):
        return int(self.data[node[0]][node[1]])

    def find_next(self, node):
        val = self.fetch_value(node)
        if node[0] > 0:
            next = add_node(node, (-1, 0))
            if self.fetch_value(next) == val + 1:
                yield next

        if node[0] < len(self.data) - 1:
            next = add_node(node, (1, 0))
            if self.fetch_value(next) == val + 1:
                yield next

        if node[1] > 0:
            next = add_node(node, (0, -1))
            if self.fetch_value(next) == val + 1:
                yield next

        if node[1] < len(self.data[0]) - 1:
            next = add_node(node, (0, 1))
            if self.fetch_value(next) == val + 1:
                yield next

    def find_trails(self, first, distinct=False):
        trails = 0
        visited = {}
        q = deque()
        q.append(first)
        while not len(q) == 0:
            node = q.pop()
            visited[node] = True
            if self.fetch_value(node) == 9:
                trails += 1
                continue
            for next_pos in self.find_next(node):
                if distinct or next_pos not in visited:
                    q.append(next_pos)
        return trails

    def trailhead_rating(self):
        total = 0
        for idx in range(len(self.data)):
            for jdx in range(len(self.data[idx])):
                node = idx, jdx
                if self.fetch_value(node) == 0:
                    total += self.find_trails(node, distinct=True)
        return total


if __name__ == "__main__":
    with open("day10/sample.txt") as file:
        runner = Runner(file.read().splitlines())
        assert runner.trailhead_score() == 36
        assert runner.trailhead_rating() == 81
    with open("day10/input.txt") as file:
        runner = Runner(file.read().splitlines())
        print(runner.trailhead_score())
        print(runner.trailhead_rating())
