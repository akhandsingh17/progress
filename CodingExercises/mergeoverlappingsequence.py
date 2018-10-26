## Merge overlapping sequences
## [(1, 3), (2, 4), (5, 7), (6, 8)]


def MergeSequence(lst):
    sort_tup = sorted(lst,key=lambda x:x[0])
    start=sort_tup[0][0]
    end=sort_tup[0][1]
    fnl_lst=[]

    for i in range(1,len(lst)):
        if end > sort_tup[i][0]:
            end = sort_tup[i][1]
            fnl_lst.append([start,end])
        else:
            start = sort_tup[i][0]
            end = sort_tup[i][1]
    return fnl_lst

def main():

    lst=[[1,3],[2,4],[5,7],[6,8]]
    print MergeSequence(lst)

if __name__=='__main__':
    main()