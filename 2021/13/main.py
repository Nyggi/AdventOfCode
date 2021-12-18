# %%
import numpy as np
# %%
with open('input.txt', 'r') as f:
    data = f.read()
data = data.split('\n')
# %%
with open('test_input.txt', 'r') as f:
    test_data = f.read()
test_data = test_data.split('\n')
# %%
def create_coords_and_folds(data):
    coords = []
    folds = []

    for line in data:
        if line.startswith("fold"):
            _, _, value = line.split()
            axis, pos = value.split("=")
            folds.append((axis, int(pos)))
        elif line:
            x, y = line.split(',')
            coords.append((int(x), int(y)))
    
    return coords, folds

# %%
def calc_folds(coords, folds):
    for axis, pos in folds:
        new_coords = []
        for x, y in coords:
            if axis == 'x':
                if x > pos:
                    new_pos = pos - x
                    coord = (pos + new_pos, y)
                    new_coords.append(coord)
                else:
                    new_coords.append((x, y))
            else:
                if y > pos:
                    new_pos = pos - y
                    coord = (x, pos + new_pos)
                    new_coords.append(coord)
                else:
                    new_coords.append((x, y))

        coords = set(new_coords)

    return coords
# %%
test_coords, test_folds = create_coords_and_folds(test_data)
len(calc_folds(test_coords, test_folds[:1]))
# %%
test_coords, test_folds = create_coords_and_folds(test_data)
len(calc_folds(test_coords, test_folds))
# %%
coords, folds = create_coords_and_folds(data)
len(calc_folds(coords, folds[:1]))
# %%
coords, folds = create_coords_and_folds(data)
result_coords = calc_folds(coords, folds)
# %%
max_x = max(result_coords, key=lambda coord: coord[0])[0]
max_y = max(result_coords, key=lambda coord: coord[1])[1]

result_array = np.zeros((max_x + 1, max_y + 1))

for x, y in result_coords:
    result_array[x, y] = 1

# %%
for j in range(result_array.shape[1]):
    for i in range(result_array.shape[0]):
        print(" ", end="") if result_array[i, j] == 0 else print('#', end='')
    print()
# %%
