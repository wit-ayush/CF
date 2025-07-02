t=int(input())
stringv=input()

m = {}

i, j = 0,1

while j < t:
  m[stringv[i:j+1]] = m.get(stringv[i:j+1],0) + 1
  i +=1
  j += 1

maxv=0
ans = ''
for key in m.keys():
  if m[key] > maxv:
    ans = key
  maxv = max(maxv, m[key])

if len(ans) > 0:
  print(ans)


