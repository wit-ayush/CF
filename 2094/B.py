t = int(input())

while t > 0:
  t -= 1
  n, m, l, r = map(int, input().split())
  la, ra = 0, 0
  for i in range(m):
    if i % 2 != 0:
      if ra < r:
        ra += 1
      else:
        ra = r
        if la > l:
          la -= 1
        else:
          la = l
    else:
      if la > l:
        la -= 1
      else:
        la = l
        if ra < r:
          ra += 1
        else:
          ra = r
  print(la, ra)