# %%
with open('input.txt', 'r') as f:
    data = f.read()
# %%
data = data.split('\n')

# %%
data
# %%

counts = {}

for col in range(len(data[0])):
    ones = 0
    zeros = 0
    for row in range(len(data)):
        if data[row][col] == '1':
            ones += 1
        else:
            zeros += 1

    counts[col] = (ones, zeros)
# %%
counts
# %%
gamma_rate = ""

for col, count in counts.items():
    if count[0] < count[1]:
        gamma_rate += '1'
    else:
        gamma_rate += '0'
# %%
gamma_rate
# %%
gamma_rate_dec = int(gamma_rate, 2) 
gamma_rate_dec
# %%
epsilon_rate = ""

for col, count in counts.items():
    if count[0] > count[1]:
        epsilon_rate += '1'
    else:
        epsilon_rate += '0'
# %%
epsilon_rate
# %%
epsilon_rate_dec = int(epsilon_rate, 2) 
epsilon_rate_dec
# %%
gamma_rate_dec * epsilon_rate_dec
# %%
#oxygen generator rating
tmp_data = data.copy()

for col in range(len(data[0])):
    ones = 0
    zeros = 0
    for row in tmp_data:
        if row[col] == '1':
            ones += 1
        else:
            zeros += 1

    bit_to_pop = "1" if ones >= zeros else "0"

    tmp_data = [row for row in tmp_data if row[col] != bit_to_pop]
    if len(tmp_data) == 1:
        break

oxygen_generator_rating = tmp_data[0]
oxygen_generator_rating
# %%
oxygen_generator_rating_dec = int(oxygen_generator_rating, 2)
oxygen_generator_rating_dec
# %%
# CO2 scrubber rating
tmp_data = data.copy()

for col in range(len(data[0])):
    ones = 0
    zeros = 0
    for row in tmp_data:
        if row[col] == '1':
            ones += 1
        else:
            zeros += 1

    bit_to_pop = "1" if ones < zeros else "0"

    tmp_data = [row for row in tmp_data if row[col] != bit_to_pop]
    if len(tmp_data) == 1:
        break

CO2_scrubber_rating = tmp_data[0]
CO2_scrubber_rating
# %%
CO2_scrubber_rating_dec = int(CO2_scrubber_rating, 2)
CO2_scrubber_rating_dec
# %%
CO2_scrubber_rating_dec * oxygen_generator_rating_dec
# %%
