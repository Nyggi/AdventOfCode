# %%
import math
from collections import deque
import numpy as np
# %%
with open('input.txt', 'r') as f:
    data = f.read()
data = [[int(c) for c in line] for line in data.split('\n')]
# %%
with open('test_input.txt', 'r') as f:
    test_data = f.read()
test_data = [[int(c) for c in line] for line in test_data.split('\n')]
# %%

checks = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
]

# %%
def calc_risk(data):
    memoid = np.ones((len(data), len(data[0])), dtype=np.int32) * math.inf

    queue = deque()

    memoid[0][0] = 0
    queue.append((0, 0))

    while len(queue) > 0:
        i, j = queue.popleft()
        
        for x, y in checks:
            check_x = i + x
            check_y = j + y
            
            if check_x < 0 or check_y < 0 or check_x >= len(data) or check_y >= len(data[i]):
                continue
            
            visit_cost = memoid[i][j] + data[check_x][check_y]
            
            if visit_cost < memoid[check_x][check_y]:
                memoid[check_x][check_y] = visit_cost
                queue.append((check_x, check_y))

    return memoid[-1][-1]

        
# %%
assert calc_risk(test_data) == 40, "Test failed"
# %%
calc_risk(data)
# %%
def calc_expanded_table(data):
    expanded_data = []
    for i in range(5):
        to_add = []
        for j in range(5):
            tmp_arr = (np.array(data) + i + j)
            tmp_arr[tmp_arr > 9] = tmp_arr[tmp_arr > 9] % 10 + 1
            to_add.append(tmp_arr)
        rows = [[] for _ in range(len(data))]
        for sector in to_add:
            for i, row in enumerate(sector):
                rows[i].extend(row)
        expanded_data.extend(rows)

    return expanded_data
# %%
expanded_test_data = calc_expanded_table(test_data)
assert calc_risk(expanded_test_data) == 315, "Test failed"
# %%
expanded_data = calc_expanded_table(data)
calc_risk(expanded_data)
# %%
