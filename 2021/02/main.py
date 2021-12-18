# %%
with open('input.txt', 'r') as f:
    data = f.read()

# %%
commands = data.split('\n')
fixed_commands = [command.split(" ") for command in commands]
# %%
fixed_commands
# %%
## Challenge 1 ##

horisontal = 0
depth = 0

for task, value in fixed_commands:
    if task == "up":
        depth -= int(value)
    elif task == "down":
        depth += int(value)
    else:
        horisontal += int(value)


# %%
horisontal * depth
# %%
## Challenge 2 ##
horisontal = 0
depth = 0
aim = 0

for task, value in fixed_commands:
    if task == "up":
        aim -= int(value)
    elif task == "down":
        aim += int(value)
    else:
        horisontal += int(value)
        depth += aim * int(value)

# %%
horisontal * depth
# %%
