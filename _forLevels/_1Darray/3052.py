count_array = [0]*42
for _ in range(10):
  count_array[int(input())%42] += 1

count = 0
for n in count_array:
  count += 1 if n != 0 else 0

print(count)