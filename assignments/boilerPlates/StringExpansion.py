def StringExpansion(str):
    """
    expand the input assuming that encoded string has a valid character followed by an integer value representing
    it's frequency
    :param str:
    :return:
    """
    freq = [i for i in str[1::2]]
    chr = [chr for chr in str[0::2]]
    result = ''
    for i in range (len(chr)):
        result = result + chr[i] * int(freq[i])
    return result

if __name__ == "__main__":
    str_exp = 'a3b1c5a2d2'
    print(StringExpansion(str_exp))