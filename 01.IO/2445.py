def amazing_star_shape(n, init_n):
  stars = '*'*(init_n-n+1)
  blank = ' '*(n-1)*2
  if n == 1:
    print(f"{stars}{blank}{stars}")
    return 0
  else:
    print(f"{stars}{blank}{stars}")
    amazing_star_shape(n-1, init_n)
    print(f"{stars}{blank}{stars}")
    return 0

n = int(input())
init_n = n
amazing_star_shape(n, init_n)