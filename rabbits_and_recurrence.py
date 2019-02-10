
def get_rabbit_pairs(n, k):

    rabit_pair_lst = [0, 1]

    while len(rabit_pair_lst) < n + 1:
        rabit_pair_lst.append(rabit_pair_lst[-1] + k*rabit_pair_lst[-2])

    return rabit_pair_lst[-1]


# sample case

print(get_rabbit_pairs(5, 3)) #this displays 19