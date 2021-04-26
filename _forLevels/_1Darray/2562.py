array = []
max_n = 0

for _ in range(9):
    n = int(input())
    if n > max_n:
        max_n = n
    array.append(n)

print(max_n)
print(array.index(max_n) + 1)