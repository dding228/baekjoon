a,b,c = map(int,input().split())
d = int(input())

time = (a +(b+(c+d)//60)//60)% 24
mi = (b+(c+d)//60) % 60
sec= (c+d) % 60

print(time, mi, sec)
