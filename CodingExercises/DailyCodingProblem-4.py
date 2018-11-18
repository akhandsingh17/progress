
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

def solution(A):#Our original array

    m = max(A) #Storing maximum value
    if m < 1:

        # In case all values in our array are negative
        return 1
    if len(A) == 1:

        #If it contains only one element
        return 2 if A[0] == 1 else 1

    l = [0] * m
    for i in range(len(A)):
        if A[i] > 0:
            if l[A[i] - 1] != 1:

                #Changing the value status at the index of our list
                l[A[i] - 1] = 1
    for i in range(len(l)):

        #Encountering first 0, i.e, the element with least value
        if l[i] == 0:
            return i+1
            #In case all values are filled between 1 and m
    return i+2



def main():
    ary= [3, 4, -1, 1]
    print solution(ary)

if __name__ == "__main__":
    main()