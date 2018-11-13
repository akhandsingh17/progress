'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def DailyCodingProblem1(ary,k):

    dict={}
    fnl_lst=[]
    for i in range(0,len(ary)):
        key=ary[i]
        diff=k-key
        if diff in dict.keys():
            tup=(diff,key)
            fnl_lst.append(tup)
        else:
            if key not in dict.keys():
                dict[key]=i
    return fnl_lst


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

if __name__=='__main__':
    main()