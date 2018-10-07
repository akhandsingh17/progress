import sys
import re
import random
import string
from collections import Counter
from itertools import permutations , combinations
from itertools import tee , izip, chain


def anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    elif ''.join(sorted(str1))==''.join(sorted(str2)):
        return True
    else:
        return True

def firstrecurrning(str):
    count={}
    cnt=1
    for char in str:
        if char in count.keys():
            cnt=cnt+1
            return char
        else:
            count[char]=1
    return count

def StructureString(str):
    lst=str.split()
    print(' '.join(lst))


def UniqueNumber(n):
    dict={}
    key=0
    while(n!=0):
        key=n%10
        if key in dict.keys():
            return False
        else:
            dict[key]=1
        n=int(n/10)
    return True

def UniqueChar(mystr):
    lst=[]
    for i in range(0,len(mystr)):
        key=mystr[i]
        lst.append(key)

    if len(lst)==len(set(lst)):
        return True
    else:
        return False

def UnionIntersection(lst1,lst2):
    print list(set(lst1).union(set(lst2)))
    print list(set(lst1).intersection(set(lst2)))

def SubsetArray(ary1,ary2):
    print set(ary2).issubset(set(ary1))
    big_lst=[]
    sml_lst=[]
    if len(ary1)>len(ary2):
        big_lst=ary1
        sml_lst=ary2
    else:
        big_lst=ary2
        sml_lst=ary1
    dict={}
    for i in range(0,len(big_lst)):
        key=big_lst[i]
        if key in dict.keys():
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1
    for i in range(0,len(sml_lst)):
        key=sml_lst[i]
        if key in dict.keys() and dict.get(key)>0:
            dict[key]=dict.get(key)-1
        else:
            return False
    return True

def StringPalindrome(palindrom_str):
    if(palindrom_str[::1]==palindrom_str[::-1]):
        return True
    else:
        return False


def singleNumber( A):
    count = Counter(A)
    print dict(count)
    return  list(filter(lambda x: x>1 , dict(count)))
'''
def StringExpansion(str_exp):
    mychar= str_exp[0::2]
    val = str_exp[1::2]
    final_str=''
    for i in range(0,len(mychar)):
        key=mychar[i]
        str = key * int(val[i])
        final_str=final_str+str
    return final_str

'''
def StringExpansion(str_exp):
    fnl_lst=[]
    prev_char=''
    #tmp_cnt= re.findall('\\d+', str_exp)
    for i in range(0,len(str_exp)):
        if ord(str_exp[i])>=48 and ord(str_exp[i])<=57:
            tmp_cnt=int(str_exp[i])
            while tmp_cnt>0:
                fnl_lst.append(prev_char)
                tmp_cnt=tmp_cnt-1

        prev_char=str_exp[i]
    return ''.join(fnl_lst)

def StringCompression(str_comp):
    fnl_lst=[]
    prv_char=str_comp[0]
    cnt=1
    for i in range(1,len(str_comp)):
        cur_char=str_comp[i]
        if cur_char==str_comp:
            cnt=cnt+1
        else:
            fnl_lst.append(prv_char)
            fnl_lst.append(str(cnt))
            cnt=1
        prv_char=str_comp[i]
    fnl_lst.append(prv_char)
    fnl_lst.append(str(cnt))
    return ''.join(fnl_lst)

def compress(s):
    count=0
    for i in range(0,len(s)):
        if s[i] == s[i-1]:
            count += 1
        c = s.count(s[i])
    return str(s[i]) + str(c)

def SingleOccurence(ary):
    fnl_lst=ary
    print list(set(fnl_lst))

def SecondMax(ary):
    lst = list(sorted(set(ary)))
    return lst[len(lst)-2]


def WordInverse(str1):
    fnl_str=[]
    lst = str1.split()
    for words in lst:
        fnl_str.append(words[::-1])
    return ' '.join(fnl_str)

'''
def ReverseNumber(n):
    str1=str(n)
    print str1
    return (str1[::-1])

'''

def ReverseNumber(n):
    found=False
    fnl_lst=[]
    while(n!=0):
        key=n%10
        if key==0 and found==False:
            n=int(n/10)
            continue
        else:
            fnl_lst.append(str(key))
            found=True
        n=int(n/10)
    return ''.join(fnl_lst)

def ReverseAry(ary):
    fnl_lst=[]
    key = len(ary) - 1
    while (key!=-1):
        fnl_lst.append(ary[key])
        key=key-1
    return  fnl_lst


def ReplaceString(tmp_str):
    lst=tmp_str.split('$')
    found=False
    fnl_lst=[]
    for i in range(0,len(lst)):
        if lst[i]=='' and found==False:
            continue
        elif lst[i]!='' and found==False:
            found = True
            fnl_lst.append(lst[i])
        elif lst[i] == '' and found == True:
            continue
        else:
            fnl_lst.append(' ')
            fnl_lst.append(lst[i])
    return ''.join(fnl_lst)

def RemoveDuplicates(ary):
    fnl_lst=[]
    return list(set(ary))

'''
def PlusOne(ary,n):
    fnl_lst=[]
    for i in range(0,len(ary)):
        key=ary[i]+n
        fnl_lst.append(key)
    return fnl_lst
'''



def PlusOne(ary,n):
    fnl_lst=[]
    for i in range(0,len(ary)):
        fnl_lst.append(str(ary[i]))
    num = ''.join(fnl_lst)
    return int(num)+n


def OddPosition(ary):
    return ary[1::2]

def EvenPosition(ary):
    fnl_lst=[]
    for i in range(0,len(ary)):
        key=i
        if key%2==0:
            fnl_lst.append(ary[key])
        else:
            continue
    return  fnl_lst

def NumberPalindrome(num):
    str1=str(num)
    str2=(str(num)[::-1])
    if str1 == str2:
        return True
    else:
        return False

#def MostRecurringElement(ary):


'''
def MinAbsDiff(ary):
    a,b=tee(ary)
    next (b,None)
    return izip(a,b)
'''


def reversal(tup):
    lst=[]
    key=len(tup)-1
    for i in range(0,len(tup)):
        lst.append(tup[key])
        key=key-1
    return lst

def jointup(lst):
    temp=lst[0]
    for i in range (1,len(lst)):
        temp = temp+lst[i]
    return temp

def wordcount(str):
    count=Counter(str)
    return  dict(count)

def tup_sort(lst):
    return max(lst, key=lambda x:sum(x))


def Median(ary):
    inp = sorted(ary)
    if (len(ary)%2)==0:
        i = len(ary)/2
        return (int(inp[i])+int(inp[i+1]))/2
    else:
        i=int(len(ary)/2)
        return inp[i]

def AddingNumber(n):
    total=0
    while (n!=0):
        key=n%10
        total = key + total
        n = int(n/10)
    return total

def AddingTwoNumbers(num1,num2):

    print(num1,num2)
    print num1+num2
    if num1>num2:
        big_num=num1
        sml_num=num2
    else:
        big_num=num2
        sml_num=num1

    carry=0
    fnl_lst=[]
    while big_num!=0:
        if sml_num!=0:
            val=big_num%10+sml_num%10+carry
            sml_num=int(sml_num/10)
        else:
            val=big_num%10+carry
        big_num=int(big_num/10)

        carry=int(val/10)
        fnl_lst.append(str(val%10))

    if carry>0:
        fnl_lst.append(str(carry))

    return ''.join(reversed(fnl_lst))


def CummulativeSum(ary):
    sum=0
    for i in range(0,len(ary)):
        key=ary[i]
        sum=sum+key
    return sum

def ReplaceNone(str):
    str1 = str.split()
    lst=[]
    for words in str1:
        lst.append(words)
    return 'NONE'.join(lst)

def IPaddress(str):
    lst=str.split('.')
    if len(lst)!=4:
        return False
    else:
        for i in range(0,len(lst)):
            try:
                if int(lst[i])>=0 and int(lst[i])<=255:
                    continue
                else:
                    return False
            except:
                return False
    return True

def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in xrange(len(A)):
        B.append([0] * n)
        for j in xrange(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B

def UniqueDigits(n):
    lst={}
    while n!=0:
        key=n%10
        if key in lst.keys():
            return False
        else:
            lst[key]=1
        n=int(n/10)
    return True


import random

def fnl(i):
    return random.random()
def ReturnRandom(ary,n):
    return sorted(ary, key=fnl)[:5]

def CheckSubstring(str,sub_str):
    if str.count(sub_str)>0:
        return True
    else:
        return False

def MovieTimes(tup_list):
    sort_list=sorted(tup_list,key=lambda x:x[0])
    fnl_tup=[]
    fnl_tup.append(sort_list[0])
    k=0
    for i in range(1,len(sort_list)):
        if sort_list[i][0]<fnl_tup[k][1] and sort_list[i][1]>fnl_tup[k][1]:
            tmp_tup=(fnl_tup[k][0],sort_list[i][1])
            del fnl_tup[k]
            fnl_tup.append(tmp_tup)
        elif sort_list[i][0]<fnl_tup[k][1] and sort_list[i][1]<fnl_tup[k][1]:
            continue
        elif sort_list[i][0]>fnl_tup[k][1]:
            k=k+1
            fnl_tup.append(sort_list[i])
    sum=0
    for i in range(0,len(fnl_tup)):
        sum=sum+fnl_tup[i][1]-fnl_tup[i][0]
    return sum

def MovieTimesAct2(tup_list):
    sort_list=sorted(tup_list,key=lambda x:x[0])
    fnl_lst=[]
    fnl_lst.append(sort_list[0])
    k=0
    for i in range(1,len(sort_list)):
        if fnl_lst[k][1]>sort_list[i][0]:
            tmp_lst=(fnl_lst[k][0],sort_list[i][1])
            del fnl_lst[k]
            fnl_lst.append(tmp_lst)
        else:
            k=k+1
            fnl_lst.append(sort_list[i])
    print(fnl_lst)
    sum=0
    for i in range(0,len(fnl_lst)):
        sum=sum+fnl_lst[i][1]-fnl_lst[i][0]
    return sum

def MovieTimes1(tup_list):
    s=set()
    for w in tup_list:
        s=s.union(range(*w))
    print len(s)

def ReturnNewString(str):
    new_str=''
    if str.find('bad') > str.find('not'):
        return  str[:str.find('not')]+'good'+str[str.find('bad')+3:]
    else:
        return str

def Top5Words(path):
    f=open(path,'r')
    data=f.read()
    words=re.split(r'\s',data)
    fnl_lst=[]
    for word in words:
        if word == '':
            continue
        else:
            fnl_lst.append(word)
    count = Counter(fnl_lst)
    print count.most_common(5)


def FlattenList(list_of_lists):
    out_lst=[]
    for item in list_of_lists:
        if isinstance(item,(list,tuple)):
            out_lst.extend(FlattenList(item))
        else:
            out_lst.append(item)
    return out_lst



def mostFrequent(lst):
    return Counter(lst).most_common(1)[0][0]

def forloop(n):
    for i in range(0,n):
        return i

def firstNonRecurring(lst):
    for i in range (0,len(lst)):
        key=lst[i]
        if key not in lst[i+1:] and key not in lst[:i]:
            return key

def solution(input):
    n=input
    output = []
    while (n!=0):
        key=n%10
        n=int(n/10)
        output.append(key)
    return output[::-1]

def find_substring(substring, string):
    lsub=len(substring)
    cnt=0
    for i in range(0,len(string)):
        if string[i:i+lsub] == substring:
            cnt=cnt+1
    return cnt

if __name__ == "__main__":

    str1='MARY'
    str2='ARMY'
    #print(anagram(str1,str2))

    stri = '       I work          in Amazon in Seattle       I           life         '
    #print StructureString(stri)

    n=341
    print UniqueNumber(n)

    mystr='akhand'
    #print(UniqueChar(mystr))

    lst1 = [1, 3, 4,3, 5, 7,5]
    lst2 = [2, 3, 5, 6,5]
    #UnionIntersection(lst1,lst2)

    ary1 = [11, 1, 13, 21, 3, 7,1]
    ary2 = [11,3, 7,1,1]
    #print(SubsetArray(ary1, ary2))

    palindrom_str = 'malayalam' #
    #print(StringPalindrome(palindrom_str))

    str_exp = 'a3b1c5a2d2' #
    #print(StringExpansion(str_exp))

    str_comp = 'aabcccccaa'
    print compress(str_comp)
    #print(StringCompression(str_comp))

    ary = [1, 2, 2, 2, 3, 4, 56, 3, 3, 3, 7, 9, 4, 9, 4, 85, 6, 34, 6, 1, 10, 34, 45]
    #print(SingleOccurence(ary))

    ary = [5, 89,89,89, 20, 64, 20, 45,64,64,64, 53]
    #print(SecondMax(ary))

    str1 = 'I am using hackerrank to improve programming'
    #print (WordInverse(str1))

    n= 340500
    #print(ReverseNumber(n))

    ary = [1, 2, 3, 4, 5, 6, 7]
    #print(ReverseAry(ary))

    str1 = '$$$$$Mr$$John$Smith$$$$$$'
    str2 = 'Mr$$John$Smith'
    str3 = '$$$$$Mr$$John$Smith'
    str4 = '$$$$$Mr$$John$$$$Smith$'
    #print(ReplaceString(str1))
    #print(ReplaceString(str2))
    #print(ReplaceString(str3))
    #print(ReplaceString(str4))

    ary = [1, 1, 1, 2, 2, 3, 5, 5, 7, 7, 7, 8, 9, 10, 34, 34, 56, 56, 56]
    #print(RemoveDuplicates(ary))


    #ary = [9, 9, 9, 7]
    n = 9
    #print(PlusOne(ary, n))

    #ary = [0, 1, 2, 3, 4, 5]
    #print(OddPosition(ary))
    #print(EvenPosition(ary))

    num = 112211
    #print(NumberPalindrome(num))
    num = 3344882
    #print(NumberPalindrome(num))


    #print(MostRecurringElement(ary))

    ary = [30, 5, 20, 9]
    lst= min(sorted(ary), key=lambda x: x[1]-x[0])
    print lst[1]-lst[0]

    tup=(1,2,3,4,5,6,7,8,9,10)
    #print reversal(tup)

    lst=[(1,2), (3,4), (8,9)]
    #print jointup(lst)

    ary = (4, 8, 4, 7, 8, 8, 5, 2, 7, 7, 7, 7, 3, 2, 1, 1)
    #tup = MostRecurringElement(ary)
    #print list(filter(lambda x: x[1]>1 ,tup))

    color_dict = {'red':'#FF0000','green':'#008000','black':'#000000','white':'#FFFFFF'}
    #print sorted(color_dict.items(), key=lambda x:x[0])

    str1='w3resource'
    #print wordcount(str1)

    lst1=['a','b','c','d','e','f']
    lst2=['d','e','f','g','h']

    #print(list(set(lst1).difference(set(lst2))))
    #print(list(set(lst2).difference(set(lst1))))
    #print(list(set(lst2).symmetric_difference(set(lst1))))

    lst=[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
    #print(sorted(lst,key=lambda x:x['key']['subkey'], reverse=False))

    lst=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
    #print tup_sort(lst)


    ary1 = [5, 89, 20, 64, 20, 45]
    #print(Median(ary1))

    ary1 = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]
    #print(Median(ary1))

    num = 38
    #print(AddingNumber(num))
    num = 679
    #print(AddingNumber(num))

    num1 = 37
    num2 = 679
    #print(AddingTwoNumbers(num1,num2))


    ary = [1, 1, 1]
    #print(CummulativeSum(ary))

    ary = [1, -1, 3]
    #print(CummulativeSum(ary))

    str = "          Amazon is a     fun place to    fun work and        is     very      fun to be    "
    #print(ReplaceNone(str))


    A=[1 ,2 ,2, 3, 1]
    #print singleNumber(A)

    tup=[(0, 10), (15, 25), (12, 20), (30, 48)]
    #print MovieTimes(tup)
    #print MovieTimes1(tup)
    #print MovieTimesAct2(tup)

    str1='This movie is not so bad!!'
    #print(ReturnNewString(str))

    str1 = 'This dinner is not that bad!'
    #print(ReturnNewString(str))

    str1 = 'This tea is not hot'
    #print(ReturnNewString(str))

    str1 = "It's bad yet not"
    #print(ReturnNewString(str))

    path = '/Users/akhandpratapsingh/Documents/hamlet.txt'
    #print(Top5Words(path))

    lst=[1,2,[1,2,3,[3,3],(5,6,7)],4,5,6,[7,6,4],[8,7,4,5,[6,7,8]]]
    #print(FlattenList(lst))

    color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    #print(color)
    #random.shuffle(color)
    #print(color)



    lst1=[1, 2, 3, 4]
    lst2=[1, 2]
    #print(list(set(lst1)-set(lst2)))

    lst=[[2,4,3],[1,5,6], [9], [7,9,0]]
    fnl_lst=[]
    for item in lst:
        fnl_lst.extend(item)
    #print list(set(fnl_lst))

    lst=[(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),(7, 8), (9, 10)]
    #print list(itertools.chain(*lst))

    dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    dict1=dict

    #print(sorted(dict.items(), key=lambda x:x[1]))

    #print(mostFrequent([0, 1, 4, 4, 3]))
    #print(mostFrequent([1, 0, 2, 2, 1, 2, 1, 1]))
    #print(mostFrequent([1, 2, 2, 3, 1, 2, 2, 1]))

    #print(firstNonRecurring([1, 2, 1]))
    #print(firstNonRecurring([1, 2, 1, 3, 2]))
    #print(firstNonRecurring([1, 2, 1, 3, 3, 4]))
    #print(firstNonRecurring([1, 2, 1, 2]))

    #print forloop(5)

    #print solution(123)

    lst1=[1, 2, 3, 4]
    #print max(lst1)

    #print find_substring('mem', "The cat says memem, meome for melog")
    perm = combinations([1, 2, 3],2)
    #print list(perm)
