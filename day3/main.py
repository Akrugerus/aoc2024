import re


class Runner:
    def __init__(self, data):
        self.lines = data.split()

    def get_mult_total(self):
        total = 0
        for line in self.lines:
            for a in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line):
                one, two = a[4:-1].split(",")
                total += int(one) * int(two)
                print(a)
                print(one)
                print(two)
        return total


if __name__ == "__main__":
    with open("day3/sample.txt", "r") as file:
        runner = Runner(file.read())
        assert runner.get_mult_total() == 161

    with open("day3/input.txt", "r") as file:
        runner = Runner(file.read())
        print(runner.get_mult_total())
