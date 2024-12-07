class Puzzle:
    def __init__(self, data: str):
        self.list_one = []
        self.list_two = []
        for line in data.split("\n"):
            num1, num2 = line.split()
            self.list_one.append(int(num1))
            self.list_two.append(int(num2))

    def distance(self):
        list_one = sorted(self.list_one)
        list_two = sorted(self.list_two)
        out = 0
        for i in range(len(list_one)):
            dist = abs(list_one[i] - list_two[i])
            print(f"{dist} between {list_one[i]} {list_two[i]}")
            out += dist
        return out

    def similarity_score(self):
        occurrences = {}
        for num in self.list_two:
            occurrences[num] = occurrences.get(num, 0) + 1
        out = 0
        for num in self.list_one:
            out += num * occurrences.get(num, 0)
        return out


if __name__ == "__main__":
    with open("day1/sample.txt", "r") as file:
        p1 = Puzzle(file.read())
        assert p1.distance() == 11
        assert p1.similarity_score() == 31

    with open("day1/input.txt", "r") as file:
        p1 = Puzzle(file.read())
        print(p1.distance())
        print(p1.similarity_score())
