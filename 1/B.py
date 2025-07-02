n = int(input())
import math
alpArr = [
   'a',  'b',  'c',  'd',  'e',  'f', 'g' , 'h',  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

intArr = {
   'a': 1,  'b': 2,  'c': 3,  'd': 4,  'e': 5,  'f': 6, 'g' : 7, 'h': 8,  'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}


def checkType(x):
  y = False
  for i in x:
    if i.isdigit():
      y = True
    else:
      if y:
        return False
  return True

def convertNewToOld(x):
  isOneOrTwo = 'one'
  ans = ''
  a, b = "", ''
  for i in x:
    if i.isdigit():
      if isOneOrTwo == 'one':
        a += i
      else:
        b += i
    else:
      if isOneOrTwo == 'one' and i == 'C':
        isOneOrTwo = 'two'
  a, b = int(a), int(b)
  while b > 0:
    b -= 1
    rem = b % 26
    ans = alpArr[rem].upper() + ans
    b = b // 26
  ans = ans + str(a)
  return ans

def convertOldToNew(x):
  c = ""
  r = ""
  for i in x:
    if i.isdigit():
      r += i  
    else:
      c += i
  
  ans = 'R' + r + 'C'
  tc = 0
  for i in range(len(c)):
    tc +=  intArr[c[len(c) - 1 - i].lower()] * math.pow(26, i)

  return ans + str(int(tc))

while n > 0:
  n -= 1
  x = input()
  y = checkType(x) 

  if y: 
    print(convertOldToNew(x))
  else:
    print(convertNewToOld(x))
