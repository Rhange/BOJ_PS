def double_pyramid(n, init_n):
  star_n = 2*n-1
  blank_n = init_n - n
  if n == 1:
    print(f"{' '*blank_n}{'*'*star_n}")
    return 1
  else:
    print(f"{' '*blank_n}{'*'*star_n}")
    double_pyramid(n-1, init_n)
    print(f"{' '*blank_n}{'*'*star_n}")
    return 0


n = int(input())
init_n = n
double_pyramid(n, init_n)