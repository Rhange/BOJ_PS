n = int(input())
scores = list(map(int, input().split(' ')))
max_score = max(scores)

fake_avg = 0
for num in scores:
  fake_avg += (num/max_score)*100/n

print(fake_avg)