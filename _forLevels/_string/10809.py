word = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
for c in alphabets:
  print(word.find(c), end=' ')

#! str.index()는 없을 경우 에러를 출력함.
#* str.find()는 없을 경우 -1를 출력함