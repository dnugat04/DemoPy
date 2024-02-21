#Đếm chẵn lẻ,tổng chẵn lẻ
from math import *
def chanLe(n):
 dem = 0
 dem1=0
 for i in range(0,n+1):
  if n%2==0:
   return dem+1
  else:
   return dem1 +1

if __name__  == "__main__":
 n = int(input())
 a = list(map(int,input().split()))
for x in a:
 if chanLe(x):
  print(x)