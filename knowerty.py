
def series_of_numbers():

    """ Outputs the number corresponding to a given letter. """

    alphabets = map(chr, range(65,91))
    i, k, val_dict = 1, 0, {}
    try:
        for d, n in enumerate(alphabets):
            if n:
                n = k*2 + i
                k, i = n, i+1
                val_dict[alphabets[d]] = n
    except:
        pass
    return val_dict

def adding_values(s):

    """ Given a string of letters like \'GREP\', computes the sum of the numbers corresponding to all the letters in the string (i.e., G + R + E + P), as given by the above series. """

    values = series_of_numbers()
    total_value = 0
    try:
        for l in list(s):
            if l:
                total_value += values[l]
    except:
        pass
    return total_value

def get_string(num):

    """ Given a large number (that would fit into a standard 32-bit integer), finds the shortest string of letters corresponding to it. """

    values = series_of_numbers()
    min_num = min(values.values(), key = lambda x:abs(x-num))
    for k,v in values.items():
        if int(v) == int(min_num):
            return k
    return k


if __name__ == '__main__':
    sn = series_of_numbers()
    added_val = adding_values('GREP')
    shortest_str = get_string(789448)
    print "\n 1. Outputs the number corresponding to a given letter ----# \n %s \n"%(sn)
    print "\n 2. Given a string of letters like \'GREP\', computes the sum of the numbers corresponding to all the letters in the string (i.e., G + R + E + P), as given by the above series ----# \n %s \n"%(added_val)
    print "\n 3. Given a large number (that would fit into a standard 32-bit integer), finds the shortest string of letters corresponding to it ----# \n %s \n"%(shortest_str)

