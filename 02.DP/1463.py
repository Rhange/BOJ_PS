def make_to_one(n):
  count = 0
  while n != 1:
    target = (n//3)*3
    one_count = n - target
    if target != 0: count += one_count

  return count

n = int(input())
print(make_to_one(n))