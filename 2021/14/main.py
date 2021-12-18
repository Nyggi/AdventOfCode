
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
def get_rules(data):
    rules = {}
    for rule in data[2:]:
        pattern, insert = rule.split(' -> ')
        rules[pattern] = insert
    return rules

# %%
def expand_polymer(polymer, rules, steps):
    polymer_template = polymer

    for step in range(steps):
        print(f"Step {step}")
        new_string = ""
        for i in range(len(polymer_template) - 1):
            match = polymer_template[i] + polymer_template[i+1]
            if match in rules:
                new_string += polymer_template[i]
                new_string += rules[match]
            else:
                new_string += polymer_template[i]
        new_string += polymer_template[-1]
        polymer_template = new_string
    
    return polymer_template
# %%
def calc_diff(polymer):
    counts = defaultdict(int)

    for c in polymer:
        counts[c] += 1

    max_count = max(counts.values())
    min_count = min(counts.values())

    return max_count - min_count
# %%
test_polymer = test_data[0]
test_rules = get_rules(test_data)
test_polymer_result = expand_polymer(test_polymer, test_rules, 10)
assert calc_diff(test_polymer_result) == 1588, "Test failed"
# %%
polymer = data[0]
rules = get_rules(data)
polymer_result = expand_polymer(polymer, rules, 10)
calc_diff(polymer_result)
# %%
polymer = data[0]
rules = get_rules(data)
polymer_result = expand_polymer(polymer, rules, 40)
calc_diff(polymer_result)
# %%

def get_polymer_dict(polymer):
    polymer_dict = defaultdict(int)

    for i in range(len(polymer) - 1):
        key = polymer[i] + polymer[i+1]
        polymer_dict[key] += 1
    
    return polymer_dict
# %%
def expand_polymer_fast(polymer_dict, rules, steps):
    for step in range(steps):
        new_polymer_dict = defaultdict(int)
        for key, count  in polymer_dict.items():
            if key in rules:
                char = rules[key]

                key1 = key[0] + char
                key2 = char + key[1]

                new_polymer_dict[key1] += count
                new_polymer_dict[key2] += count
            
        polymer_dict = new_polymer_dict
    
    return polymer_dict
# %%
def calc_diff_fast(polymer_dict, polymer):
    char_counts = defaultdict(int)

    # Count first char of each key
    for key, count in polymer_dict.items():
        c1, _ = key
        char_counts[c1] += count
    
    # Add the last char
    char_counts[polymer[-1]] += 1

    return max(char_counts.values()) - min(char_counts.values())
# %%
test_polymer_dict = get_polymer_dict(test_polymer)
test_polymer_dict_result = expand_polymer_fast(test_polymer_dict, test_rules, 40)
assert (diff := calc_diff_fast(test_polymer_dict_result, test_polymer)) == 2188189693529, f"Test failed: {diff}"

# %%
polymer = data[0]
rules = get_rules(data)
polymer_dict = get_polymer_dict(polymer)
polymer_dict_result = expand_polymer_fast(polymer_dict, rules, 40)
calc_diff_fast(polymer_dict_result, polymer)

# %%