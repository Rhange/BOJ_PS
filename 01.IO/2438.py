def print_star_pyramid(n):
  if n == 1:
    print('*')
    return 0
  else:
    print_star_pyramid(n-1)
    print('*'*n)
    return 0


n = int(input())
print_star_pyramid(n)