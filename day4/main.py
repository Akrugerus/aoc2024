import re


class Runner:
    def __init__(self, data):
        self.lines = data.strip().split("\n")

    def desc_vec(self, i, j, size):
        out = ""
        while i < size and j < size:
            out += self.lines[i][j]
            i += 1
            j += 1
        return out

    def asc_vec(self, i, j, size):
        out = ""
        while i >= 0 and j < size:
            out += self.lines[i][j]
            i -= 1
            j += 1
        return out

    def xmas_search(self):
        total = 0
        # Rows
        print("rows")
        for text in self.lines:
            total = total + self.line_search(text)

        # Columns
        print("cols")
        for i in range(len(self.lines[0])):
            text = ""
            for line in self.lines:
                text += line[i]
            total = total + self.line_search(text)

        # Assuming a square
        # Diagonal desc
        print("desc diag")
        for text in self.diag_desc():
            total = total + self.line_search(text)

        # Diagonal asc
        print("asc diag")
        for text in self.diag_asc():
            total = total + self.line_search(text)

        return total

    def diag_desc(self):
        diag_size = len(self.lines[0])

        # Climb the left side of the matrix
        for j in range(diag_size):
            yield self.desc_vec(0, j, diag_size)

        # Cross the top of the matrix, exclude the middle to avoid overlap
        for i in range(1, diag_size):
            yield self.desc_vec(i, 0, diag_size)

    def diag_asc(self):
        diag_size = len(self.lines[0])

        # Cross the top
        for i in range(diag_size):
            yield self.asc_vec(i, 0, diag_size)

        # Climb the right
        for j in range(1, diag_size):
            yield self.asc_vec(diag_size - 1, j, diag_size)

    def line_search(self, text):
        forwards = len(re.findall(r"XMAS", text))
        backwards = len(re.findall(r"SAMX", text))
        print(f"{text} {forwards} {backwards}")
        return forwards + backwards


class Runner2:
    def __init__(self, data):
        self.width = data.index("\n")
        self.data = data

    def x_mas_search(self):
        width = self.width - 1
        patterns = [
            rf"M.S.{{{width}}}A.{{{width}}}M.S",
            rf"S.M.{{{width}}}A.{{{width}}}S.M",
            rf"M.M.{{{width}}}A.{{{width}}}S.S",
            rf"S.S.{{{width}}}A.{{{width}}}M.M",
        ]
        matches = 0

        for pattern in patterns:
            pat = re.compile(pattern, flags=re.DOTALL)
            pos = 0
            while m := pat.search(self.data, pos):
                pos = m.start() + 1
                print(pat.pattern)
                print(m[0])
                matches += 1

        print(matches)
        return matches


if __name__ == "__main__":
    with open("day4/sample.txt") as file:
        runner = Runner(file.read())
        assert runner.xmas_search() == 18

    with open("day4/input.txt") as file:
        runner = Runner(file.read())
        print(runner.xmas_search())

    with open("day4/sample.txt") as file:
        runner = Runner2(file.read())
        assert runner.x_mas_search() == 9

    with open("day4/input.txt") as file:
        runner = Runner2(file.read())
        print(runner.x_mas_search())
