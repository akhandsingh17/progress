## {1: 1, 2: 1, 3: 1, 4: 1, 9: 1, 10: 1, 20: 1}


def mostfrequent(lst):
    dct={}
    cnt=0
    for i in range(len(lst)):
        if lst[i] not in dct.keys():
            dct[lst[i]]=1
        else:
            cnt+=1
            dct[lst[i]]=cnt
    return sorted(dct.items(), key=lambda x:x[1] , reverse=True)[0][0]

def main():
    lst=[1,3,1,3,2,1]
    print mostfrequent(lst)

if __name__=='__main__':
    main()


