def old_runs(puzzle_input):
    main_character = None
    character_length = 0
    for character in str(puzzle_input):
        if character != main_character:
            yield (main_character, character_length)
            main_character = character
            character_length = 1
        else:
            character_length += 1
    yield (main_character, character_length)

def runs(puzzle_input):
    main_character = None
    character_length = 0
    result = []
    for character in str(puzzle_input):
        if character != main_character:
            if main_character is not None:  # Ensure we don't append the first None value
                result.append(str(character_length) + main_character)
            main_character = character
            character_length = 1
        else:
            character_length += 1
    result.append(str(character_length) + main_character)  # Append the last run
    return ''.join(result)

def p1(puzzle_input=1113222113):
    """ find the length of the puzzle input put through 40 iterations of the pattern,
        where each run of digits with the number-of-digits followed by the digit itself.
        Example: 11122233 becomes 3_1-3_2-2_3 = 313223
        1. Get runs of a number
        2. apply the pattern iteratively
        3. get the length of the final result.
    """
    for _ in range(40):
        #print('iteration: ', _ + 1)
        # 10/20/24 This takes a lot of computational power where it causes a crash
        # reference chatgpt.py, which gives the correct answer instantly, to ammend main.py

        puzzle_input = runs(puzzle_input)
    print("answer for part 1:", len(puzzle_input))

def p2(puzzle_input='1113222113'):
    for _ in range(50):
        #print('iteration: ', _ + 1)
        puzzle_input = runs(puzzle_input)
    print("answer for part 2:", len(puzzle_input))

if __name__ == '__main__':
    p1()
    p2()
