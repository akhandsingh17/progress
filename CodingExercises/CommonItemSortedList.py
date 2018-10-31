## {1: 1, 2: 1, 3: 1, 4: 1, 9: 1, 10: 1, 20: 1}



# Python program to find intersection of
# two sorted arrays
# Function prints Intersection of arr1[] and arr2[]
# m is the number of elements in arr1[]
# n is the number of elements in arr2[]

def printIntersection(arr1, arr2):
    m=len(arr1)
    n=len(arr2)
    i,j = 0,0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j+= 1
        else:
            print(arr2[j])
            j += 1
            i += 1

def main():
    input1 =[1, 3, 4, 5, 7]
    input2 =[2, 3, 5, 6]

    print printIntersection(input1,input2)

if __name__=='__main__':
    main()


