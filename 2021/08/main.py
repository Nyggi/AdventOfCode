# %%
from collections import defaultdict
# %%
with open('input.txt', 'r') as f:
    data = f.read()
data = data.split('\n')
# %%
with open('test_input.txt', 'r') as f:
    test_data = f.read()
test_data = test_data.split('\n')
# %%
def to_sequence(data):
    sequences = []
    for x in data:
        singal_pattern, digits = x.split(" | ")
        entry = {
            "signal_pattern": singal_pattern.split(" "),
            "digits": digits.split(" "),
        }
        sequences.append(entry)
    
    return sequences
# %%
UNIQUE_LENGHTS = [2, 3, 4, 7]

def unique_instances(sequences):
    unique_instances = 0

    for entry in sequences:
        for digit in entry["digits"]:
            if len(digit) in UNIQUE_LENGHTS:
                unique_instances += 1

    return unique_instances
# %%
test_sequences = to_sequence(test_data)
unique_instances(test_sequences)
# %%
sequences = to_sequence(data)
unique_instances(sequences)
# %%
single_test_data = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
single_sequences = to_sequence(single_test_data)
test_entry = single_sequences[0]
test_entry
# %%
def calc_configuration(signal_pattern):
    configuration = {
        "to": set(),
        "bo": set(),
        "lt": set(),
        "lb": set(),
        "rt": set(),
        "rb": set(),
        "mi": set(),
    }

    # 1
    configuration["rt"].update(signal_pattern[2][0])
    configuration["rb"].update(signal_pattern[2][0])

    # print(1, configuration)

    # 7
    seven_pattern = signal_pattern[3][0]
    configuration["to"] = set(seven_pattern).difference(configuration["rb"])

    # print(7, configuration)

    # 4
    four_pattern = signal_pattern[4][0]
    configuration["mi"] = set(four_pattern).difference(configuration["rb"])
    configuration["lt"] = set(four_pattern).difference(configuration["rb"])

    # print(4, configuration)

    # patterns
    zero_pattern = None
    nine_pattern = None
    six_pattern = None

    for pattern in signal_pattern[6]:
        diff_from_mid = configuration["mi"].intersection(pattern)
        intersect_four = set(four_pattern).intersection(pattern)
        if len(diff_from_mid) == 1:
            zero_pattern = pattern
        elif len(intersect_four) == 4:
            nine_pattern = pattern
        else:
            six_pattern = pattern

    # 0
    configuration["bo"] = set(zero_pattern).difference(
        configuration["rb"].union(configuration["rt"].union(configuration["to"]))
    )
    configuration["lb"] = set(zero_pattern).difference(
        configuration["rb"].union(configuration["rt"].union(configuration["to"]))
    )
    configuration["mi"] = configuration["mi"].difference(set(zero_pattern).intersection(configuration["mi"]))
    configuration["lt"] = configuration["lt"].difference(configuration["mi"])

    configuration["bo"] = configuration["bo"].difference(configuration["lt"])
    configuration["lb"] = configuration["lb"].difference(configuration["lt"])

    # print(0, configuration)

    # 6
    configuration["rb"] = configuration["rb"].intersection(six_pattern)
    configuration["rt"] = configuration["rt"].difference(configuration["rb"])

    # print(6, configuration)

    # 9 
    configuration["bo"] = configuration["bo"].intersection(nine_pattern)
    configuration["lb"] = configuration["lb"].difference(configuration["bo"])

    # print(9, configuration)

    return configuration

# %%
DIGITS = {
    "0": set(["to", "bo", "lb", "rb", "rt", "lt"]),
    "1": set(["rb", "rt"]),
    "2": set(["to", "bo", "lb", "rt", "mi"]),
    "3": set(["to", "bo", "rb", "rt", "mi"]),
    "4": set(["rb", "rt", "lt", "mi"]),
    "5": set(["to", "bo", "rb", "lt", "mi"]),
    "6": set(["to", "bo", "lb", "rb", "lt", "mi"]),
    "7": set(["to", "rb", "rt"]),
    "8": set(["to", "bo", "lb", "rb", "lt", "mi", "rt"]),
    "9": set(["to", "bo", "rb", "lt", "mi", "rt"]),
}

# %%
def calc_digit(letter_to_pos, letters):
    positions = set([letter_to_pos[letter] for letter in letters])

    for digit, digit_positions in DIGITS.items():
        if positions == digit_positions:
            return digit
    
    raise Exception("No digit found")
# %%
def calc_message(entry):
    signal_pattern = defaultdict(list)

    for pattern in entry["signal_pattern"]:
        signal_pattern[len(pattern)].append([c for c in pattern])
    
    config = calc_configuration(signal_pattern)
    letter_to_pos = dict((letter.pop(), position) for position, letter in config.items())

    output_digit = ""
    for letter_set in entry["digits"]:
        output_digit += calc_digit(letter_to_pos, letter_set)
    return int(output_digit)
# %%
calc_message(test_entry)
# %%
def calc_sequence(sequences):
    summed_output = 0

    for entry in sequences:
        output = calc_message(entry)
        summed_output += output
    return summed_output
# %%
calc_sequence(test_sequences)
# %%
calc_sequence(sequences)
# %%
