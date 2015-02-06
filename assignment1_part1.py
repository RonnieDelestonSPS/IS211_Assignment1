def listDivide(numbers, divide=2):
  even = 0
  for i in numbers:
    if i % divide == 0:
      even +=1
  return even

def ListDivideException():
  raise "There is an error!"

def testListDivide():
  if listDivide([1,2,3,4,5]) == 2:
    pass
  elif listDivide([2,4,6,8,10]) == 5:
    pass
  elif listDivide([30,54,63,98,100], divide=10):
    pass
  elif listDivide([]) == 0:
    pass
  else:
    ListDivideException()
