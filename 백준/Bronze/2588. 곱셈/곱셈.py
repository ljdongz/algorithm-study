a = int(input())
b = int(input())

x = b // 100
y = b % 100 // 10
z = b % 100 % 10


print(a * z)
print(a * y)
print(a * x)
print(a*b)