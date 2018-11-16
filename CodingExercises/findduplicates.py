'''

Given an array of n elements which contains elements from 0 to n-1, with any of these numbers appearing any number of times.
Find these repeating numbers in O(n) and using only constant memory space.
For example, let n be 7 and array be {1, 2, 3, 1, 3, 6, 6}, the answer should be 1, 3 and 6.

'''

class duplicates:

    def __int__(self):
        self.lst=None

    def finddup(self,lst):
        n=len(lst)

        print("The repeating elements are: ")

        for i in range(0,n):
            if lst[abs(lst[i])] > 0:
                lst[abs(lst[i])] = - lst[abs(lst[i])]
            else:
                print abs(lst[i])


lst=[1, 2, 3, 1, 3, 6, 6]
dup = duplicates()
dup.finddup(lst)


