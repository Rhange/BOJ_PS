def step_by_step_tree(n, init_n):
  blank_n = init_n - n
  if n == 1:
    print(f"{' '*blank_n}*")
    return 1
  else:
    step_by_step_tree(n-1, init_n)
    print(f"{' '*blank_n}", end='')
    for i in range(n):
      if i == n-1:
        print('*')
      else:
        print('* ', end='')

n = int(input())
init_n = n
step_by_step_tree(n, init_n)