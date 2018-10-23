'''

def findsumpair(ary,k):

    lst=set()
    out_lst=[]
    for i in range(0,len(ary)):
        diff=k-ary[i]
        if diff in lst:
            tup=(ary[i],diff)
            out_lst.append(tup)
        else:
            lst.add(ary[i])
    return out_lst

'''
   
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

    arr=[1,2,3,3,5,5,6,8,10]
    k=8

    print findsumpair(arr,k)

if __name__=='__main__':
    main()

