import itertools

def rotate(arr,d,n):
    fnl_lst=[]
    fnl_lst.append(arr[d:])
    fnl_lst.append(arr[:d])
    return list(itertools.chain(*fnl_lst))

def main():
    arr=[1,2,3,4,5,6,7]
    d=2
    n=len(arr)
    print rotate(arr,d,n)

if __name__=='__main__':
    main()


