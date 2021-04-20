a, b, c = int(input()), int(input()), int(input())

result = str(a*b*c)

count = [0]*10
for n in result:
  count[int(n)] += 1

for c in count:
  print(c)