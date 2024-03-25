#1.write a recursive fun to cal the sum of n natural nos

def rec_num(n):
    if(n==1):
        return 1
    else:
        return n+rec_num(n-1)

print(rec_num(4))
