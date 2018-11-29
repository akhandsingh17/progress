## Google Phone Screen Interview
## Time Complexity O(log N)

## Find the top ten most frequent IP addresses from a web server log file. A sample line from the log file:
#14716104719,GET,/index.html,132.49.16.172,...,
import re


import sys


class XLogger:

    def __int__(self):
        self.path=None


    def openfile(self,path):
        lst=[]
        f=open(path,'r')
        line=f.readline()
        while line:
            ip=line.split('\t')[0]
            line = f.readline()
            #print '%s\t%s' % (ip, 1)
            lst.append(ip)
        f.close()
        return lst


    def get_top_k_rank(self,arry):
        dct={}
        cnt=0
        for i in arry:
            if i not in dct:
                dct[i]=1
            else:
                cnt+=1
                dct[i]=cnt


        sort_dct=sorted(dct.items(),key=lambda  x: x[1],reverse=True)[:10]

        inv_map={}
        for k, v in dct.iteritems():
            inv_map[v] = inv_map.get(v, [])
            inv_map[v].append(k)
        inv_sort_dct=sorted(inv_map.items(),key=lambda  x: x[0],reverse=True)[:10]

        print sort_dct , '\n\n' ,inv_sort_dct



log=XLogger()
path="/Users/akhans/workspace/python-projects/CodingExercises/output/19950630.23-19950801.00.tsv"
#path="/Users/akhans/workspace/python-projects/CodingExercises/output/file.tsv"
t=log.openfile(path)
d=log.get_top_k_rank(t)
print d