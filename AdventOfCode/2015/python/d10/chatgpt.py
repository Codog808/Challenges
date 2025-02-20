import itertools

def look_and_say(sequence):
    result = []
    for digit, group in itertools.groupby(sequence):
        count = len(list(group))  # Count the number of occurrences
        result.append(f"{count}{digit}")  # Append the count and the digit
    return ''.join(result)

def apply_look_and_say_n_times(start_sequence, n):
    current_sequence = start_sequence
    for _ in range(n):
        current_sequence = look_and_say(current_sequence)
    return current_sequence

# Starting sequence
puzzle_input = "1113222113"
# Apply the look-and-say process 40 times
result_sequence = apply_look_and_say_n_times(puzzle_input, 40)
# Output the length of the final result
result_length = len(result_sequence)

print("Length of the result after 40 iterations:", result_length)

