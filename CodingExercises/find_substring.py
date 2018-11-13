## Microsoft Onsite ##

## Given a string find the substring - Time Complexity --> O(NxM)

def find_sequence(in_str,search):
    output = False
    for i in range(0,len(in_str)):
        if search == in_str[i:i+len(search)]:
            output=True
        else:
            continue
    return output


def main():
    in_str= 'abcbed'
    search= 'ab'
    print find_sequence(in_str,search)


if __name__=='__main__':
    main()
