# A+B
"""
* Input
1 2

* Output
3
"""

def a_plus_b():
  a, b = map(int, input("두 숫자를 한 칸 띄어 입력하세요. (예) '1 5' : ").split())
  print(a+b)


a_plus_b()