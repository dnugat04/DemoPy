a = [1,2,3,4,5]
# duyệt thông qua chỉ số
for i in range(len(a)):
   print(a[i], end = ' ')
for i in range(-1,len(a)*-1 -1,-1):
    print(a[i], end = '\n ')
#duyệt bằng for each
for item in a:
    print(item, end = ' ')

# hàm append() để thêm 1 phần tử vào cuối
a.append("Dung")
print(a)
# hàm insert() để thêm vào 1 vị trí bất kì
a.insert (1,'Nguyen Dinh') 
print(a) #nếu như số nhập vào lớn hơn chỉ số thì nó sẽ thêm vào cuối

#hàm pop() để xóa khỏi list thông qua chỉ số, nếu không chỉ rõ chỉ số thì xóa phần tử cuối cùng
a.pop()

#hàm remove() xóa thông qua GIÁ TRỊ, nếu list có phần tử trong lặp thì xóa phần tử đầu tiên
#nếu giá trị trong list không tồn tại thì sử dụng remove sẽ gây ra lỗi



#hàm clear() xóa mọi phần tử trong list



# Sao chép list
#b = a*3
#print(b)
def sum_digit(n):
    tong = 0
    while n>0:
        tong += n%10
        n //= 10
        return tong

c = [1,222,2223,44,33,532]
d = []
for x in c:
    d.append(sum_digit(x))