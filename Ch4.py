def computePay(hours, rate) :
  if (hours > 40) :
    overtime = (hours - 40 ) * (rate * 1.5)
    compensation = overtime + (40 * rate)
    print(compensation)
  else :
    print(hours*rate)

computePay(45, 10)

def computeGrade(score) :
  try :
    if (score < 0 or score > 1.0) :
      print('Bad Score')
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
  except :
    print('Bad Score')

computeGrade(0.95)
computeGrade('perfect')
computeGrade(10.0)
computeGrade(0.75)
computeGrade(0.5)