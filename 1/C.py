# // wrong solution
# pure geometry question

import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())

s1 = math.pow(math.pow((y2 - y1), 2) + math.pow((x2 - x1), 2), 0.5)
s2 = math.pow(math.pow((y3 - y2), 2) + math.pow((x3 - x2), 2), 0.5)
s3 = math.pow(math.pow((y1 - y3), 2) + math.pow((x1 - x3), 2), 0.5)

if s1 == s2 == s3:
  print(0.5*(math.pow(s1,2)))
elif s1 == s2:
  print(math.pow(s1, 2))
elif s2 == s3:
  print(math.pow(s2, 2))
elif s3 == s1:
  print(math.pow(s1, 2))
else:
  mx = max(s1, s2, s3)
  print(math.pow(mx, 2))