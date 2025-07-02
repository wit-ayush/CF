t = int(input())

while t > 0:
  t -= 1
  x = input()
  ans = ""
  for i in range(len(x)-1,-1,-1):
    if x[i] == " ":
      ans = x[i+1] + ans
  print(x[0] + ans)