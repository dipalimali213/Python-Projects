num = int(input("Enter a Number : "))
flag = 0
for i in range(2,num):
    if num%i==0:
        flag = 1
        break
if flag==0:
    print(num," is Prime Number.")
else :
    print(num," is not Prime Number.")