#, wires## ERROR EERO ERORER, 9.2.24: FInd a way to create a circuit given a messed up series of instructions. 
#   Remember where each connection goes and then connect up.
#   Chatgpt a way to figure this out. Circuit designing programs are able to decipher this.

### GOOD GOOD, 9.4.24; it was recursive to find the value of the wire
# get signal is a chatgpt example of what I should do; Replicate and Understand.
cache = {}
def get_signal(wire, wires):
    if wire.isdigit():
        return int(wire)
    if wire in cache:
        return cache[wire]
    expr = wires[wire]
    tokens = expr.split()
    
    if len(tokens) == 1:
        val = get_signal(tokens[0], wires)
    elif len(tokens) == 2:
        # NOT operation
        val = ~get_signal(tokens[1], wires) & 0xFFFF
    elif len(tokens) == 3:
        op1, op, op2 = tokens
        if op == "AND":
            val = get_signal(op1, wires) & get_signal(op2, wires)
        elif op == "OR":
            val = get_signal(op1, wires) | get_signal(op2, wires)
        elif op == "LSHIFT":
            val = (get_signal(op1, wires) << int(op2)) & 0xFFFF
        elif op == "RSHIFT":
            val = get_signal(op1, wires) >> int(op2)
    cache[wire] = val
    return val

class d07:
    def __init__(self, filename):
        self.wires = {target: expr for line in open(filename).read().split("\n") if line for expr, target in [line.strip().split(' -> ')]}
        self.cache = {}
    def simulate(self, target):
        """ 
        expression -> Target 
        if expression contains dependent inputs:
            input_target0 + input_target1 -> target
            find expression -> input_target0
        else:
            therefore if it does not contain dependent inputs it must contain independent inputs, or acutal values
            integer -> target

        return INT

        Simulate is a recursive function, where it looks for an actual value and calculates all the previous values that is connected to an actual value. """
        # There is a pre-requisite of being given a target and its inputs, finding the value of those inputs by then making them a target and recursive go through until an actual value is met.
        # returning actual values is where the recursivity ends and where these operations with dependent inputs can finally have an output returned.
        if target.isdigit():
            return int(target)
        if target in self.cache:
            return self.cache[target]
        terms = self.wires[target].split()
        terms_len = len(terms)
        val = 100
        if terms_len == 1:
            val = self.simulate(terms[0])
        elif terms_len == 2:
            val = ~self.simulate(terms[1]) & 0xFFFF
        elif terms_len == 3:
            ip1, op, ip2 = terms
            if op == "AND":
                val = self.simulate(ip1) & self.simulate(ip2)
            elif op == "OR":
                val = self.simulate(ip1) | self.simulate(ip2)
            elif op == "LSHIFT":
                val = self.simulate(ip1) << int(ip2) & 0xFFFF
            elif op == "RSHIFT":
                val = self.simulate(ip1) >> int(ip2)
        self.cache[target] = val
        return val

    def p1(self):
        answer = self.simulate('a')
        print('answer for part 1:', answer)

    def p2(self):
        self.wires['b'] = str(self.simulate('a'))
        self.cache = {}
        answer = self.simulate('a')
        print('answer for part 2:', answer)

if __name__ == '__main__':
    d = d07('input')
    d.p1()
    d.p2()
