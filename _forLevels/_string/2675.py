def sol_2675():
  sample_cnt = int(input()) # 테스트 케이스 개수

  for _ in range(sample_cnt): # 테스트 케이스 개수만큼 반복
    answer = '' # 각 테스트 케이스의 답을 담을 변수 초기화
    repeat_cnt, string = input().split()  # 반복할 숫자, 테스트 문자열 할당
    repeat_cnt = int(repeat_cnt)  # 문자 타입의 숫자를 int 타입으로 변환
    for c in string:  # 각각의 문자에 대해서
      answer += c*repeat_cnt  # 반복횟수를 곱해준 다음 answer에 뒤에서부터 붙여준다.
    print(answer)


sol_2675()