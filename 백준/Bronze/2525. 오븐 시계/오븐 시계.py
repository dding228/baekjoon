a,b = map(int,input().split())
c = int(input())

time = (a + (b+c)//60) % 24
mi = (b+c) % 60

print(time, mi)