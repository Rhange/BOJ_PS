def print_10(string):
  if len(string) < 10:
    print(string)
  else:
    front, remainder = string[:10], string[10:]
    print(front)
    print_10(remainder)

print_10(input('아무거나 입력하세요: '))