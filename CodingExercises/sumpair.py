def findsumpair(ary,k):
    dct={}
    fnl_lst=[]
    for i in ary:
        if i not in dct:
            dct[k-i]=[i]
        else:
            fnl_lst.extend(map(lambda x:[x,i],dct[i]))
            if k-i not in dct:
                dct[k-i]=[i]
    return fnl_lst


def main():

    arr=[2,5,8,3,7,6,1,9,-1]
    k=7
    print findsumpair(arr,k)

if __name__=='__main__':
    main()

