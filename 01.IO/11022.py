n = int(input())    # 들어올 입력 갯수
for i in range(n):
    [a, b] = map(int, input().split())  # map 함수를 사용하여 받은 값을 바로 정수로 변환
    print(f"Case #{i+1}: {a} + {b} = {a+b}")