class Runner:
    turns = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}

    def __init__(self, data):
        self.data = data.splitlines()

    def find_start(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] == "^":
                    self.pos = i, j
                elif self.data[i][j] == "#":
                    self.barriers += 1

    def in_bounds(self, pos):
        return 0 <= pos[0] < len(self.data[0]) and 0 <= pos[1] < len(self.data)

    def turn(self):
        self.movement = self.turns[self.movement]

    def play(self):
        self.movement = -1, 0
        self.visited = {}
        self.barriers = 0
        self.barriers_visited = 0
        self.loop_positions = 0
        self.find_start()
        while True:
            if self.visited.get(self.pos, None) == self.movement:
                raise Exception()
            if self.pos not in self.visited:
                # Store the current position with movement information
                self.visited[self.pos] = self.movement
            # print(self.visited)

            next_pos = self.pos[0] + self.movement[0], self.pos[1] + self.movement[1]
            # print(f"checking {next_pos}")
            if not self.in_bounds(next_pos):
                return
            # print(f"{self.data[next_pos[0]][next_pos[1]]}")
            if self.data[next_pos[0]][next_pos[1]] == "#":
                # print(f"blocked at {next_pos}")
                self.barriers_visited += 1
                # If we hit an obstacle, turn right
                self.turn()
                continue

            # Check for possible loop block
            if (
                next_pos in self.visited
                and self.visited[next_pos] == self.turns[self.movement]
            ):
                # print(f"crossing path at {next_pos}")
                self.loop_positions += 1

            # Proceed
            self.pos = next_pos

    @property
    def distinct_positions(self):
        return len(self.visited)

    def find_loop_positions(self):
        loop_positions = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] in ("#", "^"):
                    continue
                old_line = self.data[i]
                self.data[i] = self.data[i][:j] + "#" + self.data[i][j + 1 :]
                try:
                    self.play()
                    # print("finite game")
                except Exception:
                    # print("found infinite loop")
                    loop_positions += 1
                self.data[i] = old_line
        return loop_positions


if __name__ == "__main__":
    with open("day6/sample.txt") as file:
        runner = Runner(file.read())
        runner.play()
        assert runner.distinct_positions == 41
        assert runner.find_loop_positions() == 6

    with open("day6/input.txt") as file:
        runner = Runner(file.read())
        runner.play()
        print(runner.distinct_positions)
        print(runner.find_loop_positions())
