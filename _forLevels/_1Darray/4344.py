import sys

case_n = int(input()) # 테스트 케이스 갯수

# 빠른 input을 위한 함수
def fast_input():
  return sys.stdin.readline().rstrip()

# 테스트 케이스를 하나씩 뽑아내기
for _ in range(case_n):
  problem = list(map(int, fast_input().split(' '))) # 테스트 케이스(문자열)을 리스트화 시키기
  student_n = problem.pop(0)  # 맨 처음 인덱스는 학생 수를 나타낸다.

  avg = sum(problem) / student_n  # 그 반의 평균은 '전체점수 / 학생수'
  over_avg_n = 0  # 평균 점수보다 높은 학생 수 카운팅을 위한 초기값

  # 각 학생수의 점수를 하나씩 빼내기
  for num in problem:
    if num > avg: over_avg_n += 1 # 학생 점수가 평균(avg)보다 높으면 카운트 추가
  print(f"{(over_avg_n/student_n)*100:.3f}%") # 결과 output
