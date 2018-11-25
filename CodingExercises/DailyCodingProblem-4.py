
'''

Good morning! Here's your coding interview problem for today.
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and
constant space. In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.

'''

# positive missing number

def solution(ary):
    m=max(ary)
    if m < 1:
        return 1
    if len(ary)==1:
        return 2 if ary[0] == 1 else 1

    l=[0]*m

    for i in range(len(ary)):
        if ary[i] > 0:
            if l[ary[i]-1] !=1:
                l[ary[i]-1]=1


    for i in range(len(l)):
        if l[i]==0:
            return i+1

    return i+2


def main():
    ary= [3, 4, -1, 1]
    print solution(ary)

if __name__ == "__main__":
    main()
