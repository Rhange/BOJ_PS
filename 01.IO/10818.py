def find_min_max(n, nums):
  min = nums[0]
  max = nums[0]
  for i in range(1, n):
    if nums[i] < min:
      min = nums[i]
    if nums[i] > max:
      max = nums[i]
  print(f"{min} {max}")


n = int(input())
nums = list(map(int, input().split()))
find_min_max(n, nums)