def read_input(original):
    '''
    This function is only for this problem. Reading fasta has to be written more carefully,
    but this problem does not need much.
    '''
    string = []
    for line in original:
        if line.startswith('>'):
            pass
        else:
            string.append(line.split('\n')[0])

    return string

def get_profile(mat):

    profile_dict = {'A': [0]*len(mat[0]), 'C': [0]*len(mat[0]), 'G': [0]*len(mat[0]), 'T': [0]*len(mat[0])} # for different rows of profile matrix

    for string in mat:
        for i in range(0, len(string)):
            profile_dict[string[i]][i] += 1

    return profile_dict

def get_consensus(profile_dict):
    consensus = ''
    keys = list(profile_dict.keys())
    for i in range(0, len(profile_dict[keys[0]])):
        max_count = 0
        max_key = keys[0]
        for key in keys:
            if profile_dict[key][i] > max_count:
                max_count = profile_dict[key][i]
                max_key = key

        consensus += max_key
    return consensus



# sample output

file = open('input_1.txt').readlines()
string = read_input(file)
profile_dict = get_profile(string)
consensus = get_consensus(profile_dict)
print(consensus)
for key in ['A', 'C', 'G', 'T']:
    print(key + ": " + " ".join(str(x) for x in profile_dict[key]))
