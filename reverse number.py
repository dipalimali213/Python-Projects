num = int(input("Enter a Number : "))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print("Reverse Number : ", reverse)