hours = input('How many hours did you work?\n')
rate = input('What is your hourly rate?\n')
compensation = 0;

try :
  hours = int(hours)
  rate = int(rate)
  if (hours > 40) :
    overtime = hours - 40
    compensation = (40 * rate) + (overtime * (rate * 1.5))
    print(compensation)
  else :
    compensation = hours * rate
    print(compensation)
except :
  print('Please input a valid number.\n')



score = input('Score: ')
score = float(score)

if (score < 0 or score > 1.0) :
  print('Error')
else :
  if (score >= 0 and score < 0.6) :
    print('F')
  elif (score >= 0.6 and score < 0.7) :
    print('D')
  elif (score >= 0.7 and score < 0.8) :
    print('C')
  elif (score >= 0.8 and score < 0.9) :
    print('B')
  else :
    print('A')