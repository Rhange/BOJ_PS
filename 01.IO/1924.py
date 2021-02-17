def findDay2007(str):
  DAYS = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
  COUNT_OF_DAYS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
  }

  total_count = 0
  month, day = map(int, str.split())
  for i in range(1, month):
    total_count += COUNT_OF_DAYS[i]
  
  total_count += day
  index = total_count % 7
  print(DAYS[index])

n = input()
findDay2007(n)