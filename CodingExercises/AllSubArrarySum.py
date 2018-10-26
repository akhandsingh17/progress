# Print all subarrays with 0 sum
# Given an array, print all subarrays in the array which has sum 0.

def AllSubArraySum(ary,k):

    dict={}
    fnl_lst=[]
    for i in ary:
        if i not in dict:
            dict[k-i]=[i]
        else:
            fnl_lst.extend(map(lambda x:[x,i],dict[i]))
            if k-i not in dict:
                dict[k-i]=i
    return fnl_lst

def main():
    
    ary=[6, 3, -1, -3, 4, -2, 2,4, 6, -12, -7]
    k=0
    print(AllSubArraySum(ary,k))

if __name__=='__main__':
    main()