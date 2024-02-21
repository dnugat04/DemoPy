#Số fibonacci: Kiểm tra 1 số có phải là số fibo, in ra số fibo thứ n, hoặc in ra n số fibo đầu tiên
import math
def fibo(n):
    print (' 0 1 ', end = ' ')
    fn1, fn2 = 1,0
    for i in range (2,n):
        fn = fn1+fn2
        print(fn, end = ' ')
        fn2,fn1 = fn1,fn
if __name__ == '__main__':
    print(fibo(10))