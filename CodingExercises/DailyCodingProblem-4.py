
'''

Good morning! Here's your coding interview problem for today.
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and
constant space. In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.

'''

def firstmissingnum(ary):
    for i in ary:
        if i < 0:
            ary.remove(i)
        else:
            continue

    for i in range(len(ary)):
        print ary[(ary[i]-1)]


def main():
    ary= [3, 4, -1, 1]
    print firstmissingnum(ary)

if __name__ == "__main__":
    main()