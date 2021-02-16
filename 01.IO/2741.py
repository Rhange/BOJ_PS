def print_1_to_n(n):
  count = 1
  while count < n+1:
    print(count)
    count += 1
  return 0

n = int(input())
print_1_to_n(n)


# import sys
# sys.setrecursionlimit(10**5)
# def print_1_to_n(n):
#   if n == 1:
#     print(1)
#     return
#   print_1_to_n(n-1)
#   print(n)
#   return

# n = int(input())
# print_1_to_n(n)