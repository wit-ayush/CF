t = int(input())

def check_subString(s):
  lent = len(s)
  map_cac = {}
  for i in range(1, lent-1):
    if map_cac.get(s[i], 0) == 0:
      map_cac[s[i]] = 1
    else:
      print('Yes')
      return
  
  if map_cac.get(s[0], 0) == 0 and map_cac.get(s[lent-1], 0) == 0:
    print("No")
  else:
    print("Yes")

while t > 0:
  t -= 1
  n = int(input())
  s = input()

  if len(s) == 3:
    if s[1] == s[0] or s[1] == s[2]:
      print("Yes")
    else:
      print("NO")

  else:
    check_subString(s)


  
