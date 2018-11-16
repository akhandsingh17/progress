'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def DailyCodingProblem1(ary,k):

    dict={}
<<<<<<< HEAD
    fnl_lst=[]
    for i in range(0,len(ary)):
        key=ary[i]
=======

    fnl_lst=[]
    for i in range(0,len(ary)):
        key=ary[i]

>>>>>>> 8ed09322e978703bdb73bb3b6dd6372e9fbb8532
        diff=k-key
        if diff in dict.keys():
            tup=(diff,key)
            fnl_lst.append(tup)
        else:
            if key not in dict.keys():
                dict[key]=i
    return fnl_lst

<<<<<<< HEAD

def findpair(arr,k):
    dct={}
    fnl_lst=[]
    for i in arr:
        if i not in dct:
            dct[k+i]=[i]
            dct[k-i]=[i]
        else:
            fnl_lst.extend(map(lambda x:[x,i],dct[i]))
            if i+k not in dct:
                dct[i+k]=[i]
            if i-k not in dct:
                dct[i-k]=[i]

    return fnl_lst


def main():

    ary=[10, 15, 3, 7, -11, 2]
    k= 17
    print(DailyCodingProblem1(ary,k))
    print(findpair(ary,k))
=======
def DailyCodingProblem1_recur(ary, k):

    fnl_lst=[]
    tmp=[]

    Combinations_recur(ary,fnl_lst,tmp,k)

    return fnl_lst

def Combinations_recur(ary,fnl_lst,tmp,k):

    if len(tmp)==2:
        sum=0
        for l in tmp:
            sum=sum+l
        if sum==k:
            if sorted(tmp) not in fnl_lst:
                fnl_lst.append(sorted(tmp.copy()))

    for i in range(0,len(ary)):
        if ary[i]>k:
            break
        tmp.append(ary[i])
        Combinations_recur(ary[i+1:], fnl_lst, tmp, k)
        tmp.pop()

def main():

    ary=[10, 15, 3, 7]
    k=17
    print(DailyCodingProblem1(ary,k))
    print(DailyCodingProblem1_recur(ary, k))
>>>>>>> 8ed09322e978703bdb73bb3b6dd6372e9fbb8532

if __name__=='__main__':
    main()