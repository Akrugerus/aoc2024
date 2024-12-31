class Runner:
    def __init__(self, data):
        self.data = data.strip()
        self.disk = []
        self.file_locations = {}
        self.file_ids = self.data[::2]
        self.spaces = []
        for idx, ch in enumerate(self.data):
            if idx % 2 == 0:
                self.file_locations[idx // 2] = len(self.disk)
                # print(f"stored {idx//2} at {len(self.disk)}")
                for _ in range(int(ch)):
                    self.disk.append(idx // 2)
            else:
                if int(ch) != 0:
                    self.spaces.append((len(self.disk), int(ch)))
                for _ in range(int(ch)):
                    self.disk.append(-1)

    def compress_naive(self):
        disk = self.disk.copy()
        r_pointer = len(disk) - 1
        l_pointer = 0
        while l_pointer < r_pointer:
            if disk[l_pointer] == -1:
                while disk[r_pointer] == -1:
                    r_pointer -= 1
                disk[l_pointer] = disk[r_pointer]
                r_pointer -= 1
            l_pointer += 1
        disk = disk[: l_pointer + 1]
        return disk

    def compress_defrag(self):
        locations = self.file_locations.copy()
        # start, length
        spaces = self.spaces.copy()
        # print(disk)
        for file_id in range(len(self.file_ids) - 1, -1, -1):
            # print(file_id)
            file_length = int(self.file_ids[file_id])
            file_start = locations[file_id]
            # File found, search for space starting from the left
            print(f"file start {file_start}")
            for idx in range(len(spaces)):
                space = spaces[idx]
                if space[0] > file_start:
                    break
                if space[1] < file_length:
                    continue
                locations[file_id] = space[0]
                if file_length == space[1]:
                    spaces.pop(idx)
                else:
                    spaces[idx] = (space[0] + file_length, space[1] - file_length)
                break
        return locations

    def frag_hash(self):
        disk = self.compress_naive()
        total = 0
        for idx, file_id in enumerate(disk):
            total += idx * file_id
        return total

    def defrag_hash(self):
        locations = self.compress_defrag()
        total = 0
        for file_id in locations:
            loc = locations[file_id]
            for idx in range(loc, loc + int(self.file_ids[file_id])):
                total += idx * file_id
        return total


if __name__ == "__main__":
    with open("day9/sample.txt") as file:
        runner = Runner(file.read())
        assert runner.frag_hash() == 1928
        assert runner.defrag_hash() == 2858

    with open("day9/input.txt") as file:
        runner = Runner(file.read())
        print(runner.frag_hash())
        print(runner.defrag_hash())
