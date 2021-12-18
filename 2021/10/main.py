# %%
import numpy as np
# %%
with open('input.txt', 'r') as f:
    data = f.read()
data = [[c for c in line] for line in data.split('\n')]
# %%
with open('test_input.txt', 'r') as f:
    test_data = f.read()
test_data = [[c for c in line] for line in test_data.split('\n')]

# %%
SYNTAX_ERROR_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

START_TAGS = set(["{", "<", "[", "("])
END_TAGS = set(["}", ">", "]", ")"])

# %%
def get_match(c):
    matcher = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    return matcher[c]
# %%

def calculate_syntax_score(data):
    total_syntax_score = 0

    for row in data:
        stack = []
        for tag in row:
            if tag in START_TAGS:
                stack.append(tag)
            elif tag in END_TAGS:
                tag_to_match = stack.pop()
                if tag != get_match(tag_to_match):
                    # print("Error: unmatched tag {}".format(tag))
                    # print("Row: {}".format(row))
                    # print("Stack: {}".format(stack))
                    total_syntax_score += SYNTAX_ERROR_SCORES[tag]
                    break
            else:
                raise ValueError("Invalid tag {}".format(tag))

    return total_syntax_score

# %%
assert calculate_syntax_score(test_data) == 26397, "Test failed"
# %%
calculate_syntax_score(data)

# %%
COMPLETE_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}
# %%
def calculate_auto_complete_score(data):
    auto_complete_scores = []

    for i, row in enumerate(data):
        stack = []
        corrupt = False
        for tag in row:
            if tag in START_TAGS:
                stack.append(tag)
            elif tag in END_TAGS:
                tag_to_match = stack.pop()
                if tag != get_match(tag_to_match):
                    # print("Error: unmatched tag {}".format(tag))
                    # print("Row: {}".format(row))
                    # print("Stack: {}".format(stack))
                    corrupt = True
                    break
            else:
                raise ValueError("Invalid tag {}".format(tag))
            
        if corrupt:
            continue

        auto_complete_score = 0

        while stack:
            tag_to_match = stack.pop()
            auto_complete_score *= 5
            auto_complete_score += COMPLETE_SCORES[get_match(tag_to_match)]
        auto_complete_scores.append(auto_complete_score)


    return np.median(auto_complete_scores)


# %%
assert calculate_auto_complete_score(test_data) == 288957, "Test failed"
# %%
calculate_auto_complete_score(data)
# %%
