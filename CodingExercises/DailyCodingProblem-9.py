
'''

Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

'''

# Function to return max sum such that no two elements are adjacent
def find_max_sum(arr):
    prev_one , prev_two,res=0,0,0
    for i in range(len(arr)):
        if i==0:
            res = arr[0]

        if i==1:
            res = max(arr[1],arr[0])

        else:
            res = max(prev_one,prev_two+arr[i])

        prev_two=prev_one
        prev_one=res
    return res

'''
## Add Memorization part ##

def max_sum(arr,i):
    if i==0:
        return arr[0]
    
    if i==1: 
        return max(arr[1],arr[0])
    
    return max(max_sum(arr,i-1),max_sum(arr,i-2)+arr[i])
'''







def main():
    ary1=[2, 4, 6, 2, 5, -1]
    ary2=[5, 1, 1, 5]
    print find_max_sum(ary1)
    print find_max_sum(ary2)

if __name__=='__main__':
    main()