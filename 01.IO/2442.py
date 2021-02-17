def print_star_tree(n):
  for i in range(1, n+1):
    print(f"{' '*(n-i)}{'*'*(2*i-1)}")


n = int(input())
print_star_tree(n)