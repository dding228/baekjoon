s_num = int(input())  # 첫 번째 입력: 정수 3
score = list(map(int, input().split()))  # 공백으로 구분된 숫자 입력 받기
s_max = max(score)  # 최댓값 찾기

if s_max == 0:
    print(0.0)
else:
    avg = sum((i / s_max) * 100 for i in score) / s_num  # 변환된 점수의 평균 계산
    print(avg)