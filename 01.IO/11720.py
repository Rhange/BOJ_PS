n = int(input())  # 처음 입력값은 숫자 개수
nums = input()  # 다음으로 들어오는 입력값은 문자열 형태의 수
total = 0 # 합 초기값
for num in nums:  # string은 char의 list
    total = total+int(num)  # convert char type to integer
print(total)