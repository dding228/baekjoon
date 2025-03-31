s = int(input())
tot=0
cnt =0
for i in range(1,s+1):
    tot += i
    if tot <= s:
        cnt+=1
    else:
        break

print(cnt)

