def parse_instruction(line):
    parts = line.strip().split()
    cmd = parts[0]
    if cmd in ('hlf', 'tpl', 'inc'):
        return (cmd, parts[1], None)
    elif cmd == "jmp":
        offset = int(parts[1])
        return (cmd, None, offset)
    elif cmd in ("jie", "jio"):
        reg = parts[1].replace(",", "")
        offset = int(parts[2])
        return (cmd, reg, offset)

def main(instructions):
    registers = {"a": 0, "b":0}
    pc = 0
    while 0 <= pc < len(instructions):
        cmd, reg, offset = instructions[pc]
        print(pc, cmd, reg, offset)
        input(registers)
        if cmd == 'hlf':
            registers[reg] //= 2
        elif cmd == 'tpl':
            registers[reg] *= 3
        elif cmd == 'inc':
            registers[reg] += 1
        elif cmd == 'jmp':
            pc += offset
            continue
        elif cmd == 'jie':
            if registers[reg] % 2 == 0:
                pc += offset
                continue
        elif cmd == 'jio':
            if registers[reg] == 0:
                pc += offset
                continue
        else:
            ValueError(f"unknown instructions {cmd}")
        pc += 1
    return registers
    pass

if __name__ == '__main__':
    with open('input') as f:
        instructions = []
        for line in f.read().strip().splitlines():
            instructions.append(parse_instruction(line))
        registers_after_program = main(instructions)
        print(registers_after_program)

