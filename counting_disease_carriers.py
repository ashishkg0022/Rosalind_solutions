'''
This problem does not include much of code. But it requires a deep understanding of probability.

Denote -> t for recessive allele and T for dominant allele

Given : proportion of homozygous recessive. [P(tt)]

Required: probability that a randomly selected individual carries at least one copy of the recessive allele

Which equals  ===>   1-P(TT)

We will use these:

P(tt) = P(t)*P(t)
P(T) = 1 - P(t)
P(TT) = P(T)*P(T)

'''
import math

def get_probability(a):
    res = []
    for i in a:

        p_t = math.sqrt(i)
        p_T = 1 - p_t
        p_TT = p_T * p_T
        res.append(str(round(1 - p_TT, 3)))

    res = ' '.join(res)
    return res


# sample output

print(get_probability([0.1, 0.25, 0.5]))

'''
It prints:

0.532 0.75 0.914

'''
