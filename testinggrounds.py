import itertools

# player_choice = itertools.cycle([1, 2])

# for i in range(10):
#     print(next(player_choice))

x = [1, 2, 3, 4]
n = itertools.cycle(x)
y = iter(x)

for i in y:
    print(i)
