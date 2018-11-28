

'''

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

'''



# A Dynamic Programming based
# Python 3 implementation to count decodings

# A Dynamic Programming based
# function to count decodings

def helper(data,k,memo):

    result=[]
    if len(data)==0:
        return 0


    if k == 0:
        return 1

    s=len(data)-k
    if data[s]== 0 :
        return 0

    if memo[k] :
        return memo[k]

    result = helper(data, k-1,memo)
    if k>= 2 and int(data[s:s+2]) <= 26:
        result+=helper(data,k-2,memo)
    memo[k]=result
    return result


def countDecodingDP(data,memo):
    k=len(data)
    return helper(data,k,memo)


def main():
    digits='10'
    k=len((digits))
    memo=[None]*(k+1)
    print countDecodingDP(digits,memo)

if __name__ == "__main__":
    main()

