# %%
import numpy as np
from collections import defaultdict

# %%
with open('input.txt', 'r') as f:
    data = f.read()
data = data.split(',')
# %%
data
# %%
len(data)
# %%
fishs = np.array([int(value) for value in data])

for day in range(256 + 1):
    print(day, len(fishs))
    indicies = np.where(fishs == 0)
    
    fish_to_decrease = np.where(fishs > 0)
    fishs[fish_to_decrease] -= 1
    
    fishs[indicies] = 6
    fishs = np.append(fishs, np.array([8] * len(indicies[0])))
    
# %%
def calculate_fish_count(data):
    fish_count = defaultdict(int)

    fishs = np.array([int(value) for value in data])

    for fish in fishs:
        fish_count[fish] += 1

    for day in range(256):
        tmp_fish_count = defaultdict(int)
        for fish_age, count in fish_count.items():
            if fish_age == 0:
                tmp_fish_count[8] += count
                tmp_fish_count[6] += count
            else:
                tmp_fish_count[fish_age - 1] += count
        
        fish_count = tmp_fish_count.copy()

    total_count = 0

    for fish_age, count in fish_count.items():
        total_count += count
    
    return total_count

# %%
test_data = "3,4,3,1,2".split(',')
assert calculate_fish_count(test_data) == 26984457539
# %%
calculate_fish_count(data)
# %%
