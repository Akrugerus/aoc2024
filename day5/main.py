class Runner:
    def __init__(self, data):
        rules, updates = data.split("\n\n")
        print(updates)
        rules = rules.split()
        self.rules = {}
        for rule in rules:
            self.rules[rule] = True
        updates = updates.split()
        self.updates = [p.split(",") for p in updates]

        self.incorrect_updates = []

    def ordered(self, update):
        for i in range(len(update) - 1):
            for j in range(i + 1, len(update)):
                falsy_rule = f"{update[j]}|{update[i]}"
                if self.rules.get(falsy_rule, False):
                    return False
        return True

    def mid_sum(self):
        out = 0
        for update in self.updates:
            if self.ordered(update):
                print(update)
                mid = len(update) // 2
                out += int(update[mid])
            else:
                self.incorrect_updates.append(update)
        return out

    def correct_update(self, update):
        for i in range(len(update) - 1):
            for j in range(i + 1, len(update)):
                falsy_rule = f"{update[j]}|{update[i]}"
                if self.rules.get(falsy_rule, False):
                    hold = update[i]
                    update[i] = update[j]
                    update[j] = hold

        return update

    def incorrect_mid_sum(self):
        out = 0
        for update in self.incorrect_updates:
            mid = len(update) // 2
            out += int(self.correct_update(update)[mid])
        return out


if __name__ == "__main__":
    with open("day5/sample.txt") as file:
        runner = Runner(file.read())
        assert runner.mid_sum() == 143
        assert runner.incorrect_mid_sum() == 123

    with open("day5/input.txt") as file:
        runner = Runner(file.read())
        print(runner.mid_sum())
        print(runner.incorrect_mid_sum())
