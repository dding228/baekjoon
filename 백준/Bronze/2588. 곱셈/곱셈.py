a = int(input())
b = int(input())

one = b % 10 # abc-> c
ten = (b//10)%10 # abc -> ab -> b
hun = b //100 # abc -> a

print(a*one)
print(a*ten)
print(a*hun)
print(a*b)