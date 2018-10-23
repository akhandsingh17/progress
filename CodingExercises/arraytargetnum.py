def findpair(ary,k):
    dct={}
    fnl_lst=[]
    for i in ary:
        if i not in dct:
            dct[i+k]=[i]
            dct[i-k]=[i]
        else:
            fnl_lst.extend(map(lambda x:[x,i],dct[i]))
            if i+k not in dct:
                dct[i+k]=[i]
            if i-k not in dct:
                dct[i+k]=[i]
    return fnl_lst


def main():

    arr=[2,5,8,3,7,6,1,9]
    k=7
    print findpair(arr,k)

if __name__=='__main__':
    main()


