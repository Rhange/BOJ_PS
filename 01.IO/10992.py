def amazing_tree(n, init_n):
  blank_n = init_n - n
  btw_blank_n = 2*(n-2)+1
  last_floor_star_n = 2*(n-1)+1 
  if n == 1:
    print(f"{' '*blank_n}*")
    return 1
  else:
    amazing_tree(n-1, init_n)
    if n == init_n:
      print(f"{'*'*last_floor_star_n}")
    else:
      print(f"{' '*blank_n}*{' '*btw_blank_n}*")
    return 0

n = int(input())
init_n = n
amazing_tree(n, init_n)