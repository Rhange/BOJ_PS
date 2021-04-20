import sys


def fast_input():
    return sys.stdin.readline().rstrip()

#* 처음 들어오는 값은 '10 5'(수열 갯수, 기준값)
count, n = map(int, fast_input().split())
#* 두번째 들어오는 값은 수열 '1 10 4 9 2 3 8 5 7 6'
nums = map(int, fast_input().split())

#* 수열에 있는 각 숫자들에 대해 
for num in nums:
  #* n 보다 작으면 출력
    if num < n:
      #* '공백'으로 띄워져서 출력
        print(num, end=" ")
