# %%
from dataclasses import dataclass
# %%
with open('input.txt', 'r') as f:
    data = f.read()
data = data.split('\n')

# %%
@dataclass
class Coordinate:
    x: int
    y: int

# %%
@dataclass
class Line:
    start: Coordinate
    end: Coordinate
# %%

data_lines = [line.split("->") for line in data]
lines = []
for from_line, to_line in data_lines:
    from_line = from_line.split(',')
    to_line = to_line.split(',')
    start = Coordinate(int(from_line[0]), int(from_line[1]))
    end = Coordinate(int(to_line[0]), int(to_line[1]))
    line = Line(start, end)
    lines.append(line)
    
# %%
lines
# %%

point_counts = {}

for line in lines:
    if line.start.x == line.end.x:
        if line.start.y > line.end.y:
            y_start = line.end.y
            y_end = line.start.y + 1
        else:
            y_start = line.start.y
            y_end = line.end.y + 1
        for y in range(y_start, y_end):
            point_counts[(line.start.x, y)] = point_counts.get((line.start.x, y), 0) + 1
    elif line.start.y == line.end.y:
        if line.start.x > line.end.x:
            x_start = line.end.x
            x_end = line.start.x + 1
        else:
            x_start = line.start.x
            x_end = line.end.x + 1
        for x in range(x_start, x_end):
            point_counts[(x, line.start.y)] = point_counts.get((x, line.start.y), 0) + 1

# %%
safe_points = [point for point, count in point_counts.items() if count >= 2]
# %%
safe_points
# %%
len(safe_points)
# %% [markdown]
# Challenge 2 add diagonals
# %%
def check_diagonal(line):
    x_distance = abs(line.start.x - line.end.x)
    y_distance = abs(line.start.y - line.end.y)
    return x_distance == y_distance

# %%
test_line = Line(Coordinate(1, 1), Coordinate(3, 3))
check_diagonal(test_line)
# %%
point_counts = {}

for line in lines:
    if line.start.x == line.end.x:
        if line.start.y > line.end.y:
            y_start = line.end.y
            y_end = line.start.y + 1
        else:
            y_start = line.start.y
            y_end = line.end.y + 1
        for y in range(y_start, y_end):
            point_counts[(line.start.x, y)] = point_counts.get((line.start.x, y), 0) + 1
    elif line.start.y == line.end.y:
        if line.start.x > line.end.x:
            x_start = line.end.x
            x_end = line.start.x + 1
        else:
            x_start = line.start.x
            x_end = line.end.x + 1
        for x in range(x_start, x_end):
            point_counts[(x, line.start.y)] = point_counts.get((x, line.start.y), 0) + 1
    elif check_diagonal(line):
        distance = abs(line.start.x - line.end.x)
        x_direction = 1 if line.start.x < line.end.x else -1
        y_direction = 1 if line.start.y < line.end.y else -1

        for i in range(distance + 1):
            point = (line.start.x + i * x_direction, line.start.y + i * y_direction)
            current_point_value = point_counts.get(point, 0)
            point_counts[point] = current_point_value + 1

# %%
safe_points = [point for point, count in point_counts.items() if count >= 2]
# %%
safe_points
# %%
len(safe_points)
# %%
