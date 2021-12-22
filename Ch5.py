def iterativeInput():
  total = 0
  count = 0
  avg = 0
  while True :
    num = input('Enter a number: ')
    if (num == 'done') :
      print(total,' ',count,' ',avg)
      break
    try :
      total = total + int(num)
      count = count + 1
      avg = total / count
      continue
    except :
      print('Invalid Input')

def maxMinInput():
  max = None
  min = None
  while True :
    num = input('Enter a number: ')
    if (num == 'done') :
      print('Max: ',max)
      print('Min: ',min)
      break
    try :
      num = int(num)
      if (max is None or num > max) :
        max = num
      if (min is None or num < min) :
        min = num
      continue
    except :
      print('Invalid Input')