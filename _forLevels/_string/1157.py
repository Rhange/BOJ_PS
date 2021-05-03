from collections import Counter


def sol_1157():
  string = input().upper()  # 입력받은 문자열 전부 대문자로 바꾸기
  counter = Counter(string) # 카운터 모듈 사용
  sorted_list = sorted(counter.items(), key=lambda x: x[1], reverse=True) # counter dict에 있는 값들을 tuple로 묶은 후에 갯수 내림차순 정렬
  
  if len(sorted_list) == 1: # 만약 들어온 값이 문자 하나라면 그대로 출력
    print(sorted_list[0][0])
  else:
    if sorted_list[0][1] == sorted_list[1][1]:  # 가장 높은 갯수 숫자가 2개(이상) 이라면 '?' 출력
      print('?')
    else: # 그렇지 않다면 0번 인덱스의 알파벳 출력
      print(sorted_list[0][0])


sol_1157()