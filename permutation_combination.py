import itertools

my_list = [1,2,3]

combinations = itertools.combinations(my_list, 3)
for c in combinations:
    print('Combinations are ', c)

permutations = itertools.permutations(my_list, 3)
for p in permutations:
    print('Permutation are ', p)