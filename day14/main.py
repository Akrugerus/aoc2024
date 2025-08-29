class Pos:
    def __init__(self, line, bounds):
        p, v = line.split(" ")
        p_x, p_y = p.split("=")[1].split(",")
        v_x, v_y = v.split("=")[1].split(",")
        self.pX, self.pY, self.vX, self.vY = int(p_x), int(p_y), int(v_x), int(v_y)
        self.bounds = bounds

    def move(self):
        self.pX += self.vX
        self.pY += self.vY

        if self.pX < 0:
            self.pX += self.bounds[0]
        if self.pX >= self.bounds[0]:
            self.pX -= self.bounds[0]
        if self.pY < 0:
            self.pY += self.bounds[1]
        if self.pY >= self.bounds[1]:
            self.pY -= self.bounds[1]

    def print(self):
        print(self.pX, self.pY)
        print(self.vX, self.vY)

    def quadrant(self) -> int:
        if self.pX < (self.bounds[0] // 2) and self.pY < (self.bounds[1] // 2):
            return 1
        if self.pX < (self.bounds[0] // 2) and self.pY > (self.bounds[1] // 2):
            return 2
        if self.pX > (self.bounds[0] // 2) and self.pY < (self.bounds[1] // 2):
            return 3
        if self.pX > (self.bounds[0] // 2) and self.pY > (self.bounds[1] // 2):
            return 4

        return -1


class Runner:
    def __init__(self, data, bounds):
        lines = data.strip().split("\n")
        self.positions = [Pos(line, bounds=bounds) for line in lines]

    def run(self, seconds: int):
        for i in range(seconds):
            for pos in self.positions:
                pos.move()

            for pos in self.positions:
                pos.print()

        d: dict[int, int] = {}
        for pos in self.positions:
            d[pos.quadrant()] = d.get(pos.quadrant(), 0) + 1

        d[-1] = 1
        out = 1
        for val in d.values():
            print(f"val{val}")
            out *= val

        print(out)
        return out


if __name__ == "__main__":
    with open("day14/sample.txt") as file:
        runner = Runner(file.read(), bounds=(11, 7))
        assert runner.run(100) == 12

    with open("day14/input.txt") as file:
        runner = Runner(file.read(), bounds=(101, 103))
        print(runner.run(100))
