class Game:
    def __init__(self, data):
        a, b, prize = data.strip().split("\n")
        a1, b1 = a.split(":")[1].strip().split(",")
        a2, b2 = b.split(":")[1].strip().split(",")
        self.a1 = int(a1.split("+")[1].strip())
        self.a2 = int(b1.split("+")[1].strip())
        self.a_cost = 1
        self.b1 = int(a2.split("+")[1].strip())
        self.b2 = int(b2.split("+")[1].strip())
        self.b_cost = 3
        prize_x, prize_y = prize.split(":")[1].strip().split(",")
        self.prize_x = int(prize_x.split("=")[1].strip())
        self.prize_y = int(prize_y.split("=")[1].strip())

    def print(self):
        print("Button a x:", self.a1, " y:", self.b1)
        print("Button b x:", self.a2, " y:", self.b2)
        print("Prize x:", self.prize_x, " y:", self.prize_y)


class Runner:
    def __init__(self, data):
        games = data.split("\n\n")
        self.games = [Game(g) for g in games]

    def run(self):
        total_cost = 0
        for game in self.games:
            a = [[game.a1, game.b1], [game.a2, game.b2]]
            b = [game.prize_x, game.prize_y]
            i = ((game.prize_x * game.b2) - (game.prize_y * game.b1)) / (
                (game.a1 * game.b2) - (game.b1 * game.a2)
            )
            j = ((game.prize_y * game.a1) - (game.prize_x * game.a2)) / (
                (game.a1 * game.b2) - (game.b1 * game.a2)
            )
            print(i, j)
            if not i.is_integer() or not j.is_integer():
                print("This game is not winnable")
                game.print()
                continue
            print(i)
            print(game.a_cost)
            print(j)
            print(game.b_cost)
            total_cost += (i * game.b_cost) + (j * game.a_cost)
            print(total_cost)

        return total_cost


if __name__ == "__main__":
    with open("day13/sample.txt") as file:
        runner = Runner(file.read())
        assert runner.run() == 480

    with open("day13/input.txt") as file:
        runner = Runner(file.read())
        print(runner.run())

    with open("day13/input.txt") as file:
        runner = Runner(file.read())
        for game in runner.games:
            game.prize_x += 10000000000000
            game.prize_y += 10000000000000
        print(runner.run())
