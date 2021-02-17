def rotate_90deg_tree(n, init_n):
  star_n = init_n-n+1
  blank_n = n-1
  if n == 1:
    print(f"{' '*blank_n}{'*'*star_n}")
    return 0
  else:
    print(f"{' '*blank_n}{'*'*star_n}")
    rotate_90deg_tree(n-1, init_n)
    print(f"{' '*blank_n}{'*'*star_n}")
    return 1


n = int(input())
init_n = n
rotate_90deg_tree(n, init_n)