# %%
import pandas as pd

# %%
with open('input.txt', 'r') as f:
    data = f.read()


# %%
data_list = data.split('\n')
# %%

increases = 0

for i in range(0, len(data_list) - 1):
    if data_list[i] < data_list[i+1]:
        increases += 1

# %%
## I'm not sure if this is the correct answer, but it's the answer I got
increases + 1

# %%
df = pd.read_csv('input.txt', header=None)
# %%
df
# %%
windowed_sum = df.rolling(3).sum().dropna()
windowed_sum
# %%
increases = 0

for i in range(0, len(windowed_sum) - 1):
    if windowed_sum.iloc[i][0] < windowed_sum.iloc[i+1][0]:
        increases += 1
# %%
increases
# %%
