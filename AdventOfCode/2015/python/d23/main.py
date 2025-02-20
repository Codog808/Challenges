""" 
1.14: first review; 
    * Figure out what a computer program does, given its instructions
        - 2 registers
        - 6 instructions

"""

def hlf(r):
    return r // 2

def tpl(r):
    return r * 3

def inc(r):
    return r + 1

def jmp(offset, current_index):
    return current_index + offset

def jio(offset, current_index, r):
    if r == 1:
        return current_index + offset
    return current_index + 1

def jie(offset, current_index, r):
    if r % 2 == 0:
        return current_index + offset
    return current_index + 1

instructions = {
    "hlf": hlf,
    "tpl": tpl,
    "inc": inc,
    "jmp": jmp,
    "jie": jie,
    "jio": jio,
}

def main():
    registers = {
        "a": 0,
        "b": 0
    }
    with open("input") as program_instructions_file:
        program = program_instructions_file.read().strip().splitlines()
        current_index = 0
        while current_index < len(program):
            print("index", current_index, "\t|", program[current_index], end='')
            ops = program[current_index].strip().split(" ")
            f = instructions[ops[0]]
            if ops[0] in ['hlf', 'tpl', 'inc']:
                registers[ops[1]] = f(registers[ops[1]])
                current_index += 1
            elif ops[0] in ['jio', 'jie']:
                offset = int(ops[2])
                register = registers[ops[1].replace(",", "")]
                current_index = f(offset, current_index, register)
            elif ops[0] in ['jmp']:
                offset = int(ops[1])
                current_index = f(offset, current_index)
            #input("enter to continue program...")
            print("\t| registers:", "a:", registers['a'], "\t| b:", registers['b'])
            print()
        print("Answer to part 1:", registers['b'])

                

    pass

def main_1():
    registers = {
        "a": 1,
        "b": 0
    }
    with open("input") as program_instructions_file:
        program = program_instructions_file.read().strip().splitlines()
        current_index = 0
        while current_index < len(program):
            print("index", current_index, "\t|", program[current_index], end='')
            ops = program[current_index].strip().split(" ")
            f = instructions[ops[0]]
            if ops[0] in ['hlf', 'tpl', 'inc']:
                registers[ops[1]] = f(registers[ops[1]])
                current_index += 1
            elif ops[0] in ['jio', 'jie']:
                offset = int(ops[2])
                register = registers[ops[1].replace(",", "")]
                current_index = f(offset, current_index, register)
            elif ops[0] in ['jmp']:
                offset = int(ops[1])
                current_index = f(offset, current_index)
            #input("enter to continue program...")
            print("\t| registers:", "a:", registers['a'], "\t| b:", registers['b'])
            print()
        print("Answer to part 1:", registers['b'])

if __name__ == "__main__":
    main()
    main_1()
