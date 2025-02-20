class d20:
    def __init__(self, puzzle_input=36_000_000):
        self.puzzle_input = puzzle_input

    def p1(self):
        print("Starting P1...")
        limit = self.puzzle_input // 10
        houses = [0] * (limit + 1)
        for elf in range(1, limit + 1):
            print("\tON ELF:", elf)
            for house in range(elf, limit + 1, elf):
                houses[house] += 10 * elf

        for house, present in enumerate(houses):
            if present >= self.puzzle_input:
                print("\tAnswer to part 1:", house)
                return house
    def p2(self):
        limit = self.puzzle_input // 11
        houses = [0] * (limit + 1)
        for elf in range(1, limit + 1):
            print("\tON ELF:", elf)
            for house in range(elf, min(elf * 50 + 1, limit + 1), elf):
                houses[house] += 11 * elf

        for house, present in enumerate(houses):
            if present >= self.puzzle_input:
                print("\tAnswer to part 2:", house)
                return house
        pass

if __name__ == "__main__":
    d = d20()
    #d.p1()
    d.p2()
