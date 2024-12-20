from itertools import product


class Runner:
    def __init__(self, data):
        data = data.splitlines()
        self.lines = [line.split(":") for line in data]

    def run(self):
        total = 0
        print(self.lines)
        for line in self.lines:
            answer, parts = line
            answer = int(answer.strip())
            parts = parts.strip().split()
            num_parts = len(parts)
            perms = product(["*", "+"], repeat=num_parts - 1)
            for perm in perms:
                local_total = parts[0]
                for idx in range(len(perm)):
                    local_total = eval(f"{local_total} {perm[idx]} {parts[idx+1]}")

                if local_total == answer:
                    total += int(answer)
                    print(f"{parts} == {answer}")
                    break
        return total


if __name__ == "__main__":
    with open("day7/sample.txt") as file:
        runner = Runner(file.read())
        assert runner.run() == 3749
    with open("day7/input.txt") as file:
        runner = Runner(file.read())
        print(runner.run())
