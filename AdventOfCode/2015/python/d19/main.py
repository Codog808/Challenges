import re
from collections import deque

class d19:
    def __init__(self, file_path):
        elements_raw, self.puzzle = open(file_path).read().strip().split("\n\n")
        self.elements = []
        self.replacements = []
        for item in elements_raw.strip().splitlines():
            element, replacement = item.strip().split(" => ")
            self.elements.append((element, replacement))
            self.replacements.append((replacement, element))

    def p1(self):
        distinct_molecules = set()
        print("converting molecules with replacements")
        for element, replacement in self.elements:
            for match in re.finditer(element, self.puzzle):
                start, end = match.span()
                new_molecule = self.puzzle[:start] + replacement + self.puzzle[end:]
                distinct_molecules.add(new_molecule)
        print("\tAnswer to part 1:", len(distinct_molecules), "Distinct Molecules")

    def p2(self):
        print("Strating part 2")
        print("\tConverting down to e's")
        queue = deque([(self.puzzle, 0)])
        seen = set()
        current_level = 0

        while queue:
            current_molecule, steps = queue.popleft()
            print(f"\tCurrent molecule: {current_molecule[:50]}... (length: {len(current_molecule)}), Steps: {steps}")

            if current_molecule == "e":
                print("\t\tAnswer to part 2:", steps)
                return steps
            
            if steps > current_level:
                current_level = steps
                print(f"\tProcessing level {current_level}. Queue cleared for next level.")

            next_queue = []
            for replacement, element in self.replacements:
                for match in re.finditer(replacement, current_molecule):
                    start, end = match.span()
                    new_molecule = current_molecule[:start] + element + current_molecule[end:]
                    if new_molecule not in seen:
                        seen.add(new_molecule)
                        next_queue.append((new_molecule, steps + 1))
            
            queue.extend(next_queue)
            if len(queue) > 50000:
                queue = deque(sorted(queue, key=lambda x: len(x[0]))[:25000])
if __name__ == '__main__':
    d = d19('input')
    d.p1()
    d.p2()


