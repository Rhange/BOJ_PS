def print_star_pyramid2(n, init_n):
  if n == 1:
    print(f"{' '*(init_n-n)}*")
    return 0
  else:
    print_star_pyramid(n-1, init_n)
    print(f"{' '*(init_n-n)}{'*'*n}")
    return 0


n = int(input())
init_n = n
print_star_pyramid2(n, init_n)