t = int(input())

while t > 0:
  t -= 1
  n, s = map(int, input().split())
  arr = list(map(int, input().split()))
  mx, mi = max(arr), min(arr)

  if s > mx:
    print(s-mi)
  elif s < mi:
    print(mx-s)
  else:
    if abs(mi - s) > abs(mx - s):
      print(abs(mx - s)*2 + abs(mi - s))
    else:
      print(abs(mx - s) + abs(mi - s)*2)

  
