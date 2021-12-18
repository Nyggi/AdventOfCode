# %%
import copy
# %%
with open('input.txt', 'r') as f:
    data = f.read()
data = [[int(c) for c in line] for line in data.split('\n')]
# %%
with open('test_input.txt', 'r') as f:
    test_data = f.read()
test_data = [[int(c) for c in line] for line in test_data.split('\n')]

# %%
touching = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1),
]
# %%
def calc_flashes(data, steps = 100):
    flashes = 0

    data = copy.deepcopy(data)

    for step in range(steps):
        step_flashes = 0
        # print(step)
        # for row in data:
        #     print(*row)
        squid_flashing = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] = data[i][j] + 1
                if data[i][j] > 9:
                    squid_flashing.append((i, j))
                    data[i][j] = 0
        

        while squid_flashing:
            i, j = squid_flashing.pop()
            step_flashes += 1
            for x, y in touching:
                if i + x >= 0 and i + x < len(data) and j + y >= 0 and j + y < len(data[0]):
                    touch_value = data[i + x][j + y]
                    if touch_value > 0:
                        data[i + x][j + y] = touch_value + 1
                    if data[i + x][j + y] > 9:
                        data[i + x][j + y] = 0
                        squid_flashing.append((i + x, j + y))
        flashes += step_flashes
        if sum(sum(row) for row in data) == 0:
            break

    return flashes, step + 1
# %%
flashes, step = calc_flashes(test_data)
assert flashes == 1656, 'flashes is {}'.format(flashes)
# %%
calc_flashes(data)
# %%
calc_flashes(test_data, steps=1100)
# %%
calc_flashes(data, steps=1100)
# %%
