def increment_password(old_password):
    i = len(old_password) - 1
    password = list(old_password)
    while i >= 0:
        if password[i] == "z":
            password[i] = "a"
            i -= 1
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return ''.join(password)

def rule_one(new_password):
    if len(new_password) == 8:
        for character in new_password:
            if not character.islower():
                return False
            return True
    return False

def rule_two(new_password):
    for i in range(len(new_password) - 2):
        if ord(new_password[i]) + 1 == ord(new_password[i + 1]) and ord(new_password[i + 1]) + 1 == ord(new_password[i + 2]):
            return True
    return False

def rule_three(new_password):
    return 'i' not in new_password and 'o' not in new_password and 'l' not in new_password

def rule_four(new_password):
    pairs = set()
    i = 0
    while i < len(new_password) - 1:
        if new_password[i] == new_password[i + 1]:
            pairs.add(new_password[i])
            i += 2
        else:
            i += 1
    return len(list(pairs)) >= 2

def p1(old_password):
    """
    Santa has to find a new password as corporate policy dictates a cyclical change of.
        Rules
            1. passwords must be exactly eight lowercase letters
    - Santa finds a new password by incrementing his old password string until it is valid
        - xy, xz, ya, ... zy, zz, aa, ...
        - it is a circular pattern
            2. password must include an increasing straight of 3 consecutives.
            3. cannot contain i, o, or l
            4. two different, non-overlapping pairs of letters
                (aa, bb) or (zz, rr)
    """
    password = old_password
    while True:
        password = increment_password(password)
        print(password)
        if rule_one(password):
            if rule_three(password):
                if rule_four(password):
                    if rule_two(password):
                        break
    return password


if __name__ == "__main__":
    part1_answer = p1("cqjxjnds")
    p1(part1_answer)

    
