run = True
while run:
  [a, b] = input().split()
  sum = int(a) + int(b)
  if sum != 0:
    print(sum)
  else:
    run = False