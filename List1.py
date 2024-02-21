# 3 dạng toán cơ bản trên mảng 1 chiều 
# Dạng 1: Liệt kê, đếm các phần tử thỏa mãn trong List
from math import *
def nt(n):
    if n <2:
        return False
    for i in range(2, isqrt(n)+1):
        if n%i ==0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    for x in a:
        if nt(x):
            print (x, end = ' ')
# Dạng 2: Tìm max, min

min_val, max_val = 10**18, -10**18
for x in a:
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x
print(min_val,max_val)

#Dạng 3: Kiểm tra các cặp phần tử trong List thỏa mãn điều kiện gì đó
# ==>> Dùng 2 vòng forr