import re


class Runner:
    def __init__(self, data):
        # The question means for us to interpret all lines as one
        # and \n characters shouldn't influence the outcome
        self.lines = [data]

    def get_mult_total(self):
        total = 0
        for line in self.lines:
            total += self.get_mul_in_line(line)
        return total

    def get_mul_in_line(self, line):
        total = 0
        for a in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line):
            one, two = a[4:-1].split(",")
            print(one, two)
            total += int(one) * int(two)
        return total

    def get_do_dont_mult_total(self):
        total = 0
        for line in self.lines:
            for do_dont in line.split("do()"):
                do = do_dont.split("don't()")[0]
                total += self.get_mul_in_line(do)
        return total


if __name__ == "__main__":
    with open("day3/sample.txt", "r") as file:
        runner = Runner(file.read())
        assert runner.get_mult_total() == 161

    with open("day3/sample2.txt", "r") as file:
        runner = Runner(file.read())
        assert runner.get_do_dont_mult_total() == 48

    with open("day3/input.txt", "r") as file:
        runner = Runner(file.read())
        print(runner.get_mult_total())
        print(runner.get_do_dont_mult_total())
