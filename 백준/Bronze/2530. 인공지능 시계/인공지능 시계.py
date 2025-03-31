A, B, C = map(int, input().split())
D = int(input())

# 현재 시간 → 초로 변환
current_time = A * 3600 + B * 60 + C

# 요리 시간 더하기
current_time += D

# 시, 분, 초로 변환
A = (current_time // 3600) % 24
B = (current_time % 3600) // 60
C = current_time % 60

# 출력
print(A, B, C)