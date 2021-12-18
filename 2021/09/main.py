# %%
from queue import Queue
from collections import defaultdict
# %%
with open('input.txt', 'r') as f:
    data = f.read()
data = [[int(c) for c in line] for line in data.split('\n')]
# %%
with open('test_input.txt', 'r') as f:
    test_data = f.read()
test_data = [[int(c) for c in line] for line in test_data.split('\n')]

# %%
test_data
# %%
checks = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
]

# %%
def calc_risk(data):
    total_risk = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            current_value = data[i][j]
            
            low_point = True

            for x, y in checks:
                check_x = i + x
                check_y = j + y

                if check_x < 0 or check_y < 0 or check_x >= len(data) or check_y >= len(data[i]):
                    continue

                value_to_check = data[check_x][check_y]
                

                if value_to_check <= current_value:
                    low_point = False
                    break
            
            if low_point:
                total_risk += current_value + 1
            
    return total_risk

# %%
calc_risk(test_data)
# %%
calc_risk(data)
# %%
def add_neighbours(data, neirbourgs_to_check, x, y):
    for x_, y_ in checks:
        check_x = x + x_
        check_y = y + y_

        if check_x < 0 or check_y < 0 or check_x >= len(data) or check_y >= len(data[x]):
            continue

        if data[check_x][check_y] != 9:
            neirbourgs_to_check.put((check_x, check_y))

# %%
def calc_bassins(data):
    bassins = []
    touched_points = set()

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 9:
                continue
            if data[i][j] in touched_points:
                continue
            checked_neighbours = {}
            neirbourgs_to_check = Queue()
            neirbourgs_to_check.put((i, j))
            while not neirbourgs_to_check.empty():
                x, y = neirbourgs_to_check.get()
                touched_points.add((x, y))
                if (x, y) in checked_neighbours:
                    continue
                checked_neighbours[(x, y)] = True
                add_neighbours(data, neirbourgs_to_check, x, y)
            bassins.append(set(checked_neighbours.keys()))

    return bassins
# %%
def calc_total_bassin_size(bassins):
    unique_bassins = defaultdict(list)
    for bassin in bassins:
        if bassin not in unique_bassins[len(bassin)]:
            unique_bassins[len(bassin)].append(bassin)

    bassins_to_add = 3

    total_bassin_size = 1

    for bassin_length in sorted(unique_bassins.keys(), reverse=True):
        for bassin in unique_bassins[bassin_length]:
            if bassins_to_add == 0:
                break
            total_bassin_size *= bassin_length
            bassins_to_add -= 1

    return total_bassin_size
# %%
test_bassins = calc_bassins(test_data)
test_total_bassin_size = calc_total_bassin_size(test_bassins)
test_total_bassin_size
# %%
bassins = calc_bassins(data)
total_bassin_size = calc_total_bassin_size(bassins)
total_bassin_size
# %%
