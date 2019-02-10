
def get_sum(n, m):
    sum_ncm = 0
    nCi = 1 #initial
    for i in range(1, m+1):
        sum_ncm += nCi
        nCi *= (n-i+1)
        nCi /= i
        sum_ncm = sum_ncm%1000000

    return pow(2, n, 1000000) - sum_ncm

#sample output

print(get_sum(6 ,3)) #prints 42