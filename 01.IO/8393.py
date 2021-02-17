def sum_under_n(n):
  sum = 0
  even_sum_eq = (n+1)*(n//2)
  if n % 2 == 0:
    sum = even_sum_eq
    print(sum)
  else:
    sum = even_sum_eq + (n//2+1)
    print(sum)


n = int(input())
sum_under_n(n)