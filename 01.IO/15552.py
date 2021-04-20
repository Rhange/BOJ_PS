import sys

#* sys.stdin.readline() 을 사용하는 것이 input() 보다 빠르다.
#* 뒤에 rstrip()을 붙여주는 이유는 readline()은 `\n`을 포함하고 있기 때문
def fast_input():
    return sys.stdin.readline().rstrip()

count = int(fast_input())

#* for 문에서 출력할 때, input()을 사용하면 시간초과가 나올 수 있다.
for _ in range(count):
    a, b = map(int, fast_input().split())
    print(a + b)
