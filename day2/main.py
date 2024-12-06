class Runner:
    def __init__(self, data):
        self.reports = []
        print(data)
        for line in data.splitlines():
            self.reports.append(list(map(int, line.split())))

    def safe_count(self):
        count = 0
        for report in self.reports:
            if self.is_safe(report):
                count += 1
        return count

    def safe_count_with_pd(self):
        count = 0
        for report in self.reports:
            safe = self.is_safe(report)
            i = 0
            while not safe and i < len(report):
                report_copy = report.copy()
                report_copy.pop(i)
                safe = self.is_safe(report_copy)
                i += 1
            if safe:
                count += 1
        return count

    def is_safe(self, report):
        diffs = []
        for i in range(len(report) - 1):
            diff = report[i] - report[i + 1]
            diffs.append(diff)
        if all(map(lambda x: abs(x) < 4, diffs)) and (
            all(map(lambda x: x < 0, diffs)) or all(map(lambda x: x > 0, diffs))
        ):
            print(f"{report} safe")
            return True
        return False


if __name__ == "__main__":
    with open("day2/sample.txt", "r") as file:
        runner = Runner(file.read())
        assert runner.safe_count() == 2
        # The brute force solution for part 2 would be to run our existing check against every subset of each list
        # where a single element is removed
        assert runner.safe_count_with_pd() == 4
    with open("day2/input.txt", "r") as file:
        runner = Runner(file.read())
        print(runner.safe_count())
        print(runner.safe_count_with_pd())
