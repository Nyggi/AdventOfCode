# %%
import numpy as np
from functools import cache
# %%
with open('input.txt', 'r') as f:
    data = f.read()
data = data.split(',')
data = [int(x) for x in data]
# %%
data
# %%
test_data = [16,1,2,0,4,2,7,1,2,14]
# %%
assert np.median(test_data) == 2
# %%
def fuel_cost(crabs, position):
    fuel_cost = 0
    
    for crab in crabs:
        fuel_cost += abs(crab - position)
    
    return fuel_cost
# %%
assert fuel_cost(test_data, 2) == 37
# %%
optimal_position = np.median(data)
fuel_cost(data, optimal_position)

# %%
@cache
def modified_fibonacci(n):
    if n <= 1:
        return n
    else:
        return modified_fibonacci(n-1) + n

# %%
def increasing_fuel_cost(crabs, position):
    fuel_cost = 0
    
    for crab in crabs:
        fuel_cost += modified_fibonacci(abs(crab - position))
    
    return fuel_cost
# %%
optimal_position = np.ceil(np.mean(test_data))
fuel_cost = increasing_fuel_cost(test_data, optimal_position)
assert fuel_cost == 168, fuel_cost
# %%
optimal_position = np.floor(np.mean(data))
increasing_fuel_cost(data, optimal_position)
# %%
