import itertools


some_set = [item for item in input("Enter the list items: ").split()]

data = itertools.combinations(some_set, 3)

subsets = list(data)

print(subsets)
