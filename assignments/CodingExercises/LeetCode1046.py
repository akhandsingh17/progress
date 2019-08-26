'''
1046. Last Stone Weight
Easy
We have a collection of rocks, each rock has a positive integer weight.
Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
'''

def LeetCode1046(ary):

    while len(ary)>1:
        ary=sorted(ary,reverse=True)
        if ary[0]==ary[1]:
            ary.pop(0)
            ary.pop(0)
        else:
            diff=ary[0]-ary[1]
            ary.pop(0)
            ary.pop(0)
            ary.insert(0,diff)
    return ary

def main():

   ary=[2,7,4,1,8,1]
   print(LeetCode1046(ary))

if __name__=='__main__':
    main()