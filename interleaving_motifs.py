
def shortest_common_supersequence(a, b):
    '''
    we will use concept of dp using a 2D matrix
    '''
    dp = [[0]*(len(b)+1) for i in range(0, len(a)+1)] # initialise a 2d array

    for i in range(0, len(a)+1):
        for j in range(0, len(b)+1):

            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    res = []
    i, j = len(a), len(b)

    while i > 0 and j > 0:
        if (a[i - 1] == b[j - 1]):
            res.append(a[i - 1]) 
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]: 
    
            res.append(b[j - 1])
            j -= 1 
        else:

            res.append(a[i - 1]) 
            i -= 1

    while i > 0:
        res.append(a[i-1])
        i -= 1
    while j > 0:
        res.append(b[j-1])
        j -= 1

    str = ''.join(reversed(res))
    return str



## sample output

print(shortest_common_supersequence("ATCTGAT", "TGCATA"))

'''
It prints:

ATGCATGAT

'''






