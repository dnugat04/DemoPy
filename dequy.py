#bai1: Tính 1+2+..+n
"""
from math import *
def S(n):
    if n==0:
        return 0
    else:
        return n + S(n-1)

if __name__ == '__main__':
    n = int(input())
    print(S(n))
"""
#bài 2: Tính 1^2 + 2^2 + ... n^2
"""from math import *
def S(n):
    if n==1:
        return 1;
    else:
        return n*n + S(n-1)
if __name == '__main__'
 n = int(input())
 print(S(n)) """
# bài 3: Tính -1 +2-3+4+...+(-1)^n * n
from math import *
def S(n):
    if n%2 != 0:
        return -S(n-1) + n
 elif:
  n==1
        return -1
    else:
        return n + S(n-1)
if __name == '__main__'
 n = int(input())
 print(S(n))