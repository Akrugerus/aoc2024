class Runner:
    def __init__(self, data):
        vals = [int(v) for v in data.split()]
        self.vals = vals
        self.memo = {0: [1]}
        self.height_memo = {}
        self.lookups = 0
        self.calcs = 0

    def simulate_stone(self, v):
        cache = self.memo.get(v, None)
        # Rule 1 is cached in init
        if cache:
            self.lookups += 1
            return self.memo[v]
        # Rule 2
        elif len(str(v)) % 2 == 0:
            val = str(v)
            val_len = len(val)
            left = val[: val_len // 2]
            right = val[val_len // 2 :]
            new = [int(left), int(right)]
        # Rule 3
        else:
            n = v * 2024
            new = [n]
        self.calcs += 1
        self.memo[v] = new
        return new

    def do_blinks(self, num):
        out = 0
        for val in self.vals:
            self.height = 0
            self.reached_tail = False
            out += self.length_at_height(val, num)
        print(out)
        return out

    def length_at_height(self, val, height):
        # DFS and memoize the length at each height for a given value
        memo = self.height_memo.get((val, height), None)
        if memo:
            return memo
        children = self.simulate_stone(val)
        if height == 1:
            self.height_memo[(val, height)] = len(children)
            return len(children)
        out = 0
        for child in children:
            out += self.length_at_height(child, height - 1)
        self.height_memo[(val, height)] = out
        return out


if __name__ == "__main__":
    with open("day11/sample.txt") as file:
        runner = Runner(file.read())
        assert runner.simulate_stone(125) == [253000]
        assert runner.simulate_stone(17) == [1, 7]
        length = runner.do_blinks(25)
        assert length == 55312

    with open("day11/input.txt") as file:
        runner = Runner(file.read())
        length = runner.do_blinks(25)
        print(length)
        length = runner.do_blinks(75)
        print(length)
