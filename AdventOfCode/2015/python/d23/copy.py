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

def execute_program(instructions, a_init=0, b_init=0):
    registers = {"a": a_init, "b": b_init}
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
            if registers[reg] == 1:
                pc += offset
                continue

        pc += 1  # Move to the next instruction if no jump occurs

    return registers['b']

# Given input instructions
input_instructions = [
    "jio a, +19",
    "inc a",
    "tpl a",
    "inc a",
    "tpl a",
    "inc a",
    "tpl a",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "jmp +23",
    "tpl a",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "inc a",
    "tpl a",
    "inc a",
    "tpl a",
    "inc a",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "inc a",
    "inc a",
    "tpl a",
    "tpl a",
    "inc a",
    "jio a, +8",
    "inc b",
    "jie a, +4",
    "tpl a",
    "inc a",
    "jmp +2",
    "hlf a",
    "jmp -7"
]

# Parse the input instructions
parsed_instructions = [parse_instruction(line) for line in input_instructions]

# Execute the program and get register b's final value
result_b = execute_program(parsed_instructions)
print(result_b)

