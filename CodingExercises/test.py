
def DailyCodingProblem2(str):
    lst= str.split()
    dct={}
    cnt=1
    for word in lst:
        if word.istitle():
            if word not in dct.keys():
                dct[word]=1
            else:
                cnt+=1
                dct[word]=cnt
    return dct


def main():
    str= "Michael Jackson likes to eat at McDonalds. Michael created Jackson"
    print DailyCodingProblem2(str)


if __name__ == "__main__":
    main()

